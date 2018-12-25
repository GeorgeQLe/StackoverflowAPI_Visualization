# Copyright 2018 George Le
#
# Pulling information from Stack Overflow
# Bag of Words
from bagofwords import Bagofwords
from questionretrieval import get_API_name, get_start_date, get_end_date, get_search_term_from_user, parse_questions, parse_links, prompt_for_continue, query_stackoverflow_for_questions
from impasse import json_dump

import collections
import sys

def main():

    continue_program = 1
    counter_searches = 0

    while continue_program != -1:
        counter_searches+= 1
        API = get_API_name()

        questions = query_stackoverflow_for_questions(API)
        
        # parses the questions from the dictionary obtained from stackoverflow
        # parsed_questions is a dictionary that maps the title of the question
        # to the full question
        parsed_questions = parse_questions(questions)
        
        for question in parsed_questions:
            print(question)

        # parses the links from the dictionary obtained from stackoverflow
        # links is a dictionary that maps the title of the question to the
        # link to the question
        links = parse_links(questions)

        bw = Bagofwords()
        # Parses the corpus to collect all of the invdividual terms and stores it 
        # into a vocabulary. This vocabulary is a list of strings
        vocabulary = bw.tokenize_corpus(parsed_questions)
        print("Sorting")
        # Performs a bag of words algorithm on the corpus of questions based on all of the 
        # terms of the vocabulary.
        # Returns a dictionary which maps a term in the vocabulary to another dictionary
        # which maps a corresponding 
        list_of_scores = bw.create_final_list(vocabulary, parsed_questions)

        # for scores in list_of_scores.keys():
        #     print(scores, ", ", list_of_scores[scores])

        list_of_score_titles = {}
        for score_title in list_of_scores.keys():
            list_of_score_titles[score_title] = len(list_of_scores[score_title])
        list_of_score_titles_sorted = collections.OrderedDict(sorted(list_of_score_titles.items(), key = lambda t : t[1], reverse = True))

        list_of_questions_sorted = collections.OrderedDict()
        for score_title in list_of_score_titles_sorted.keys():
            list_questions = []
            for question in list_of_scores[score_title].keys():
                list_questions.append(question)
            list_of_questions_sorted[score_title] = list_questions
        print("Finish Sort")

        json_dump(API, links, list_of_questions_sorted)

        # reset continue_program if needed
        if continue_program != 1:
            continue_program = 1

        while continue_program != 0 and continue_program != -1:
            search_term = get_search_term_from_user()

            if search_term in list_of_questions_sorted:
                    print ("There are", len(list_of_questions_sorted[search_term]), "relevant questions to", search_term, "\b.")
                    for score_title in list_of_questions_sorted[search_term]:
                        print(score_title, ": ", links[score_title])
            else:
                print("There are no relevant questions on stack overflow")

            continue_program = prompt_for_continue()

if __name__ == "__main__":
    main()