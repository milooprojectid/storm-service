from sklearn.feature_extraction.text import TfidfVectorizer
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
from typing import Mapping, List

import re
import tqdm
import pandas as pd
import numpy as np

class HadistRetrieval:
    def __init__(self):
        self.stopwords = [line.rstrip('\n\r') for line in open('modules/hadistretrieval/data/stopword_list_TALA.txt')]
        self.stemmer = StemmerFactory().create_stemmer()
        self.hadist = pd.read_csv('modules/hadistretrieval/data/hadist.csv', delimiter=';')
        vectorizer = TfidfVectorizer()
        self.X = vectorizer.fit_transform(self.hadist.Processed)
        self.features = vectorizer.get_feature_names()

    def _text_lower(self, text: str) -> str:
        return text.lower()

    def _remove_entities(self, text: str) -> str:
        return re.sub(r'\[[^]]*\]', '', text)

    def _case_folding(self, text: str) -> str:
        return re.sub(r'[^a-z]', ' ', re.sub("'", '', text))

    def _stemming(self, text: str) ->str:
        return self.stemmer.stem(text)

    def _stopwords_removal(self, text: str) -> str:
        texts_token = text.split()
        not_stopword = []
        for token in texts_token:
            if token not in self.stopwords:
                not_stopword.append(token)
        return ' '.join(not_stopword)

    def _preprocessing(self, text: str) -> str:
        tx_lower = self._text_lower(text)
        tx_remove_entities = self._remove_entities(tx_lower)
        tx_case_folding = self._case_folding(tx_remove_entities)
        tx_stemming = self._stemming(tx_case_folding)
        return self._stopwords_removal(tx_stemming)

    def retrieve(self, sentence: str, n: int = 5) -> List[Mapping[str, str]]:
        sent_prep = self._preprocessing(sentence)
        query = sent_prep.split()
        res = np.zeros(self.X.shape[0])
        not_in_corpus = []
        output: List[Mapping[str, str]] = []

        for keyword in query:
            try:
                res += self.X.toarray()[:,self.features.index(keyword)]
            except:
                not_in_corpus.append(keyword)
                res = np.zeros(self.X.shape[0])

        top_idx = np.argsort(-res)[:n]

        if not sum(res) > 0:
            raise ValueError('dindt match, someting wrong')

        for i in range(len(top_idx)):
            # res[top_idx[i]]
            output.append({
                'source': self.hadist.iloc[top_idx[i]][4],
                'text': self.hadist.iloc[top_idx[i]][2]
            })

        return output
