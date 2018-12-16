# Copyright 2018 George Le
#
# Pulling information from Stack Overflow
# Bag of Words

from bagofwords import Bagofwords
from questionretrieval import get_API_name, get_search_term_from_user, parse_questions, parse_links, prompt_for_continue, query_stackoverflow_for_questions

import collections
import json
import os

def main():
    continue_program = 1
    while continue_program != -1:
        API = get_API_name()

        questions = query_stackoverflow_for_questions(API)
        
        parsed_questions = parse_questions(questions)

        links = parse_links(questions)
        for link_title in links.keys():
            print(link_title, ": ", links[link_title])

        # performs a bag of words algorithm on the corpus of questions
        bw = Bagofwords()
        # 
        vocabulary = bw.tokenize_corpus(parsed_questions)
        print("Sorting")
        list_of_scores = bw.create_final_list(vocabulary, parsed_questions)

        # for scores in list_of_scores.keys():
        #     print(scores, ", ", list_of_scores[scores])

        list_of_score_titles = {}
        for score_title in list_of_scores.keys():
            list_of_score_titles[score_title] = len(list_of_scores[score_title])
        list_of_score_titles_sorted = collections.OrderedDict(sorted(list_of_score_titles.items(), key = lambda t : t[1], reverse = True))

        for score_title in list_of_score_titles_sorted.keys():
            print(score_title, " ", list_of_score_titles_sorted[score_title])
        print("Finish Sort")

        list_of_questions_sorted = collections.OrderedDict()
        for score_title in list_of_score_titles_sorted.keys():
            list_questions = []
            for question in list_of_scores[score_title].keys():
                list_questions.append(question)
            list_of_questions_sorted[score_title] = list_questions

        for score_title in list_of_questions_sorted.keys():
            print(score_title, ": ", list_of_questions_sorted[score_title])
            
        with open('links_results.json', 'w') as fp:
            json.dump(links, fp)
        
        with open('questions_results.json', 'w') as fp:
            json.dump(list_of_questions_sorted, fp)

        # reset continue_program if needed
        if continue_program != 1:
            continue_program = 1

        while continue_program != 0 and continue_program != -1:
            search_term = get_search_term_from_user()

            if len(list_of_questions_sorted[search_term]) == 0:
                print("There are no relevant questions on stack overflow for you to look at!")
            else:
                print ("There are", len(list_of_questions_sorted[search_term]), "relevant questions to", search_term, "\b.")
                for score_title in list_of_questions_sorted[search_term]:
                    print(score_title, ": ", links[score_title])

            continue_program = prompt_for_continue()

if __name__ == "__main__":
    main()