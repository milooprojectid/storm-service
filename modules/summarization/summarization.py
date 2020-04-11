import numpy as np
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
from nltk.tokenize import sent_tokenize
import re
import os

stopwords = open('modules/summarization/stopwords.txt','r')

class summarization(object):
    
    def __init__(self):
        self.factory = StemmerFactory()
        self.stemmer = self.factory.create_stemmer()
        self.stopwords = [line.rstrip('\n\r') for line in stopwords]
        # self.paragraph = self.paragraph
        # self.data = self.data


    def casefolding(self,sentence):
        """
        Transform words from uppercase into lowercase and remove characters other than letters.

        :param sentence: sentence that will be transform
        :return: lowercase sentence and only contain letters
        """
        sentence = sentence.lower()
        sentence = re.sub(r'[^a-z]', ' ', re.sub("’", '', sentence))
        return sentence
    
    def tokenization(self, sentence):
        """
        Split the sentence into list of token.

        :param sentence: sentence
        :return: list of sentence
        """
        return sentence.split()

    def stopword_removal(self, token):
        """
        Remove stopword in words list using stopword list.

        :param token: list of words
        :return: token that not in stopword list
        """
        temp = []
        for i in range(len(token)):
            if token[i] not in self.stopwords:
                temp.append(token[i])
        return temp

    def stemming(self, tokens):
        """
        Transform words into root words using Nazief-Andriani Stemming algorithm

        :param tokens: list of words
        :return: list of words that has been transform into root words
        """
        for i in range(len(tokens)):
            tokens[i] = self.stemmer.stem(tokens[i])
        return tokens

    def remove_escape(self, d):
        d = d.split('\\')
        d = ' '.join(d)
        return d

    def remove_url(self, d):
        """
        Remove URL in text

        :param d: document
        :return:
        """
        d = d.split()
        i = 0
        while i < len(d):
            if 'https://' in d[i]:
                d.remove(d[i])
                i -= 1
            elif 'http://' in d[i]:
                d.remove(d[i])
                i -= 1
            i += 1

        d = ' '.join(d)
        return d

    def remove_punctuation(self, d):
        d = d.split()
        i = 0
        while i < len(d):
            if len(d) > 0:
                if d[i][0] == 'x' and len(d[i]) == 3:
                    d.remove(d[i])
                    i -= 1
            if len(d) > 0:
                if len(d[i]) == 1:
                    d.remove(d[i])
                    i -= 1
            if len(d) > 0:
                if 'rt' in d[i]:
                    d.remove(d[i])
                    i -= 1
            i += 1
        d = ' '.join(d)
        return d

    def join_input(self, newslist):
        result = ''.join(newslist)
        return result


    def sentence_split(self,paragraph):
        """
        Split the paragraph/documents into sentences.

        :param paragraph: text documents
        :return: list of sentences
        """
        return sent_tokenize(paragraph)


    def word_freq(self,data):
        """
        Count frequency for each words in the documents.

        :param data: text documents
        :return: frequency for each words
        """
        w = []
        for sentence in data:
            for words in sentence:
                w.append(words)
        bag = list(set(w))
        res = {}
        for word in bag:
            res[word] = w.count(word)
        return res


    def fit(self,paragraph):
        """
        Predict Summarization from documents

        :param paragraph : string of news
        :return : sentence of summarization
        """

        # pre = Preprocessing()

        sentence_list = self.sentence_split(paragraph)
        data = []
        for i in range(len(sentence_list)):
            data.append(self.stemming(self.stopword_removal(self.tokenization(self.casefolding(sentence_list[i])))))
        data = (list(filter(None, data)))

        wordfreq = self.word_freq(data)

        ranking = []
        for words in data:
            temp = 0
            for word in words:
                temp += wordfreq[word]
            ranking.append(temp)

        sort_list = sorted(range(len(ranking)), key=ranking.__getitem__, reverse=True)
        n = 1
        sentence = ''
        for i in range(n):
            sentence += '{}'.format(sentence_list[sort_list[i]])
        return sentence


if __name__ == "__main__":
    summary = summarization()
    print(summary.fit('ini coba saja dapet ngga summary dari berita yang telah diambil.'))