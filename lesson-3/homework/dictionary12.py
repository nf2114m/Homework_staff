rd = {
    "serendipity": "Chance",
    "ephemeral": "Temporary",
    "sonder": "Realization",
    "petrichor": "Rain-smell",
    "limerence": "Infatuation",
    "quixotic": "Idealistic",
    "wabi-sabi": "Imperfection"
}
n="Chance"

s=0
for i in rd.values():
    if i==n:
        s=s+1
print(s)
