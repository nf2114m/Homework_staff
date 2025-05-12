rd = ('serendipity', 'ephemeral', 'sonder', 'petrichor', 'limerence', 'quixotic', 'wabi-sabi')
ad = ('Chance', 'Temporary', 'Chance', 'Rain-smell', 'Infatuation', 'Idealistic', 'Imperfection')

dr={}

for i in range(len(rd)):
    dr.update({rd[i]:ad[i]})
print(dr)
