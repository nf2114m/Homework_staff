rd = {
    "serendipity": "Chance",
    "ephemeral": "Temporary",
    "sonder": "Realization",
    "petrichor": "Rain-smell",
    "limerence": "Infatuation",
    "quixotic": "Idealistic",
    "wabi-sabi": "Imperfection",
    "colors":{"red":"255", "blue":"200"
        }
}

s=False
for i in rd.values():
    if isinstance(i,dict):
        s=True
        break
print(s)
