# Copyright 2018 George Le

from stackapipull import get_stored_questions

def query_stackoverflow_for_questions(API_name):
    # dictionary of various key value pairs 
    stored_quests = get_stored_questions(API_name)
    return stored_quests

def parse_questions(stored_quests):
    sentences = []
    for question in stored_quests:
        sentences.append(question['title'])
    return sentences

def parse_links(stored_questions):
    links = {}
    for question in stored_questions:
        links[question['title']] = question['link']
    return links

def get_search_term_from_user():
    print("Please enter in a search term (lowercase) for the API you chose:", end = " ")
    search_input = input()
    return search_input

def get_API_name():
    print("Please enter in the name of an API that you are curious about:", end = " ")
    API_input = input()
    return API_input

def prompt_for_continue():
    print("Would like to search for more terms? (type in quit to quit):", end = " ")
    continue_input = input()

    while (continue_input != "Yes") and (continue_input != "yes") and (continue_input != "No") and (continue_input != "no") and (continue_input != "Quit") and (continue_input != "quit"):
        print("Invalid input. Your input was: ", continue_input, ". Please type in yes to try again, no to search for a new API, or quit to quit", end = " ")
        continue_input = input()
    choice = 1
    if continue_input == "Yes" or continue_input == "yes":
        return choice
    elif continue_input == "No" or continue_input == "no":
        choice = 0
    elif continue_input == "Quit" or continue_input == "quit":
        choice = -1

    return choice