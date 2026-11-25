from pathlib import Path
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
years = list(range(2008, 2027))
stock = [3133301,3233460,3317376,3188589,3040666,3032923,2961126,2951301,2890031,2769640,2727565,2803429,2761907,2535642,2241691,2202448,2187375,2055727,2079165]
fig, ax = plt.subplots(figsize=(6, 10.6667), facecolor="#101c29")
ax.set_facecolor("#101c29")
fig.text(.12,.91,"DATA AIKE",color="#78d8c4",fontsize=15,weight="bold")
fig.text(.12,.83,"SANTA CRUZ",color="white",fontsize=27,weight="bold")
fig.text(.12,.78,"Existencias ovinas | 2008–2026",color="white",fontsize=12)
ax.plot(years,[v/1e6 for v in stock],color="#78d8c4",linewidth=3)
ax.set_ylabel("Millones de cabezas",color="white")
ax.tick_params(colors="white")
ax.set_xticks([2008,2014,2020,2026])
for spine in ax.spines.values():
    spine.set_visible(False)
ax.grid(alpha=.15)
fig.subplots_adjust(left=.15,right=.90,bottom=.28,top=.72)
fig.text(.12,.18,"2,08 millones",color="white",fontsize=25,weight="bold")
fig.text(.12,.14,"Existencias en 2026",color="#78d8c4",fontsize=12)
fig.text(.12,.06,"Serie histórica recuperada; verificar fuente original.",color="white",fontsize=8)
out = ROOT / "results"
out.mkdir(exist_ok=True)
fig.savefig(out / "sheep_story.png",dpi=180,facecolor=fig.get_facecolor())
plt.close(fig)
