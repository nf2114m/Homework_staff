rd = {
    "serendipity": "Chance",
    "ephemeral": "Temporary",
    "sonder": "Realization",
    "petrichor": "Rain-smell",
    "limerence": "Infatuation",
    "quixotic": "Idealistic",
    "wabi-sabi": "Imperfection"
}

rd2={}

for i in rd.keys():
    rd2.update({rd[i]:i})
print(rd2)
