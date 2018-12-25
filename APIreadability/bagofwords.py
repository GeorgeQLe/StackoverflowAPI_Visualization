# Copyright 2018 George Le

import numpy as np
import re # regular expressions

class Bagofwords:

    # default class constructor
    def __init__(self):
        self.__ignore_words = []

    def add_ignore_words(self, new_ignore_words):
        for word in new_ignore_words:
            self.__ignore_words.append(word)

    # runs tfidf for a single term in a set of document 
    # returns and updates the class' member __vocabulary with the relevant terms
    def bagofwords(self, term, corpus):
        return self.__tfidf(term, corpus)

    # runs tfidf for all words in a given corpus
    def create_final_list(self, vocabulary, corpus):
        scores = {}
        for word in vocabulary:
            if word.isdigit() == False:
                scores[word] = self.__tfidf(word, corpus)
        return scores

    def tokenize_corpus(self, corpus):
        vocabulary = []
        for document in corpus:
            temp = self.__extract_words(document)
            for word in temp:
                if word not in vocabulary:
                    vocabulary.append(word)
        return vocabulary

    def __extract_words(self, sentence):
        words = re.sub("[^\w]", " ", sentence).split()
        words_cleaned = [w.lower() for w in words if w not in self.__ignore_words]
        return words_cleaned

    # parses a document for individual words
    # returns a list of the individual words
    def __tokenize_document(self, document):
        words = []
        for sentence in document:
            w = self.__extract_words(sentence)
            words.extend(w)

        words = sorted(list(set(words)))
        return words

    # calculates the term frequency 
    def __term_frequency(self, term, document):
        if len(document) == 0:
            return 0
        f = self.__count_term_occurances_in_document(term, document)
        return (f / float(len(document)))

    # calculates the inverse document frequency
    def __inverse_document_frequency(self, total_num_documents, num_documents_with_i):
        if num_documents_with_i == 0:
            return 0
        return (total_num_documents / num_documents_with_i)

    # calculates the final tf-idf for a single term
    def __tfidf(self, term, corpus):
        scores = {}
        for document in corpus:
            score = self.__term_frequency(term, document) * self.__inverse_document_frequency(len(corpus), self.__count_documents_with_term(term, corpus))
            if score != 0:
                scores[document] = score
        return scores

    def __count_term_occurances_in_document(self, term, document):
        # counter for the number of occurances of the term in the passed document
        count = 0
        if isinstance(document, list):
            # iterates through a document
            for sentence in document:
                sentence_vocabulary = self.__tokenize_document(sentence)
                for word in sentence_vocabulary:
                    if term == word:
                        count+=1
        elif isinstance(document, str):
            sentence_vocabulary = self.__extract_words(document)
            for word in sentence_vocabulary:
                if term == word:
                    count+=1
        return count

    def __count_documents_with_term(self, term, corpus):
        count = 0
        for document in corpus:
            if self.__count_term_occurances_in_document(term, document) > 0:
                count += 1
        return count