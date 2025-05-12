rd = {
    "serendipity": "Chance",
    "ephemeral": "Temporary",
    "sonder": "Chance",
    "petrichor": "Rain-smell",
    "limerence": "Infatuation",
    "quixotic": "Idealistic",
    "wabi-sabi": "Imperfection"
}

ad = {
    "serendipity": "Chance",
    "ephemeral": "Temporary",
    "sonder": "Chance",
    "petrichor": "Rain-smell",
    "limerence": "Infatuation",
    "quixotic": "Idealistic",
    "wabi-sabi": "Imperfection"
}

s=False

for i in rd.keys():
    if i in ad.keys():
        s=True
print(s)
