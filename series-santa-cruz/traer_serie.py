"""Download a public time series from datos.gob.ar."""
import argparse
import csv
import json
import re
import urllib.parse
import urllib.request

parser = argparse.ArgumentParser()
parser.add_argument("id", nargs="?", default="45.2_ECTDTRG_0_T_46")
parser.add_argument("desde", nargs="?")
args = parser.parse_args()
if not re.fullmatch(r"[A-Za-z0-9_.-]+", args.id):
    parser.error("Invalid series ID")
params = {"ids": args.id, "format": "json", "metadata": "full", "limit": 5000}
if args.desde:
    params["start_date"] = args.desde + "-01-01"
url = "https://apis.datos.gob.ar/series/api/series/?" + urllib.parse.urlencode(params)
with urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent":"data-aike/1.0"}), timeout=60) as response:
    js = json.load(response)
meta = js.get("meta") or []
field = meta[1].get("field", {}) if len(meta) > 1 else {}
with open(args.id + ".csv", "w", newline="", encoding="utf-8-sig") as f:
    writer = csv.writer(f, delimiter=";")
    writer.writerow(["fecha", "valor", "unidad"])
    for fecha, valor in js.get("data", []):
        writer.writerow([fecha, valor, field.get("units", "")])
print(args.id, len(js.get("data", [])), "rows")
