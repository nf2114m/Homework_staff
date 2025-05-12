rd = {
    "serendipity": "Chance",
    "ephemeral": "Temporary",
    "sonder": "Realization",
    "petrichor": "Rain-smell",
    "limerence": "Infatuation",
    "quixotic": "Idealistic",
    "wabi-sabi": "Imperfection"
}
n="sonder"
try:
    rd.pop(n)
    print(rd)
except:
    print("none")
