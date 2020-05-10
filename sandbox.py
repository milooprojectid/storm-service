from modules.hadistretrieval.hadistretrieval import HadistRetrieval

hadist = HadistRetrieval()
result = hadist.retrieve('menagih hutang')

for hadist in result:
    print(hadist['text'] + '\n')
