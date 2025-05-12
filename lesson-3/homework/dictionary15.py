rd = {
    "serendipity": "Chance",
    "ephemeral": "Temporary",
    "sonder": "Realization",
    "petrichor": "Rain-smell",
    "limerence": "Infatuation",
    "quixotic": "Idealistic",
    "wabi-sabi": "Imperfection"
}

l=["a","b","c"]
s=["d","e","f"]

rd={}

for i in range(len(l)):
    rd.update({l[i]:s[i]})
print(rd)
