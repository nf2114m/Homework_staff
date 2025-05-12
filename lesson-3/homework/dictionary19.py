rd = {
    "serendipity": "Chance",
    "ephemeral": "Temporary",
    "sonder": "Chance",
    "petrichor": "Rain-smell",
    "limerence": "Infatuation",
    "quixotic": "Idealistic",
    "wabi-sabi": "Imperfection"
}
s=0
for i in rd.values():
    if list(rd.values()).count(i)==1:
        s=s+1
print(s)

