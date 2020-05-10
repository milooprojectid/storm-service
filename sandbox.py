from modules.hadistretrieval.hadistretrieval import HadistRetrieval

hadist = HadistRetrieval()
result = hadist.retrieve('berhubungan badan')

for hadist in result:
    print(hadist['text'] + '\n')