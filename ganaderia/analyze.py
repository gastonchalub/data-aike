from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

root = Path(__file__).resolve().parent
data = pd.read_csv(root / "datos/santa_cruz_bovinos_por_departamento.csv").set_index("departamento")
assert len(data) == 7 and data.index.is_unique
summary = pd.DataFrame({"reported_stock": data.sum(), "departments_reporting": data.count()})
summary["complete_stock"] = summary.reported_stock.where(summary.departments_reporting == 7)
print(summary)
changes = data[["2008", "2019"]].copy()
changes["change_pct"] = (changes["2019"] / changes["2008"] - 1) * 100
print(changes)
ax = changes[["2008", "2019"]].sort_values("2019").plot.barh(figsize=(9,5))
ax.set(xlabel="Cabezas", title="Santa Cruz: existencias bovinas por departamento")
ax.figure.tight_layout()
out = root.parent / "results"
out.mkdir(exist_ok=True)
ax.figure.savefig(out / "bovinos_departamentos.png", dpi=180)
summary.to_csv(out / "bovinos_serie.csv")
