# Copyright 2018 George Le
from __future__ import print_function
from stackapipull import get_stored_questions, Date

def get_API_name():
    print("Please enter in the name of an API that you are curious about:", end = " ")
    API_input = input()
    return API_input

def get_num_of_days(month):
    if month == 1:
        return 31
    elif month == 2:
        return 28
    elif month == 3:
        return 31
    elif month == 4:
        return 30
    elif month == 5:
        return 31
    elif month == 6:
        return 30
    elif month == 7:
        return 31
    elif month == 8:
        return 31
    elif month == 9:
        return 30
    elif month == 10:
        return 31
    elif month == 11:
        return 30
    elif month == 12:
        return 31

def get_start_date():
    date = Date()
    print("Please enter in the start date you would like to search from (in numbers): ")

    print("Month: ", end = " ")
    month = int(float(input()))

    while type(month) is not int or month < 1 or month > 12:
        print("That is not a valid numeric value for a month. You entered: ", month)
        print("Please enter in a number between 1 and 12: ", end = "")
        month = int(float(input()))
    date.month = month

    print()
    print("Day: ", end = "")
    day = int(float(input()))
        
    while type(day) is not int or day < 1 or day > get_num_of_days(month):
        print("That is not a valid day. You entered: ", day)
        print("Please enter in a number between 1 and ", get_num_of_days(month), ": ", end = "")
        day = int(float(input()))
    date.day = day

    print()
    print("Year: ", end = "")
    year = int(float(input()))

    while type(year) is not int or year < 2010 or year > 2018:
        print("That is not a valid year. You entered: ", year)
        print("Please enter in a year between 2010 to 2018: ", end = "")
        year = int(float(input()))
    date.year = year

    print("You chose the start date: ", date.month, "\b/", date.day, "\b/", date.year, ".")

    return date

def get_end_date():
    date = Date()
    print("Please enter in the end date you would like to search from (in numbers): ")

    print("Month: ", end = "")
    month = int(float(input()))

    while type(month) is not int or month < 1 or month > 12:
        print("That is not a valid numeric value for a month. You entered: ", month)
        print("Please enter in a number between 1 and 12: ", end = "")
        month = int(float(input()))
    date.month = month

    print()
    print("Day: ", end = "")
    day = int(float(input()))
        
    while type(day) is not int or day < 1 or day > get_num_of_days(month):
        print("That is not a valid day. You entered: ", day)
        print("Please enter in a number between 1 and ", get_num_of_days(month), ": ", end = "")
        day = int(float(input()))
    date.day = day

    print()
    print("Year: ", end = "")
    year = int(float(input()))

    while type(year) is not int or year < 2010 or year > 2018:
        print("That is not a valid year. You entered: ", year)
        print("Please enter in a year between 2010 to 2018: ", end = "")
        year = int(float(input()))
    date.year = year

    print("You chose the end date: ", date.month, " ", date.day, " ", date.year, ".")

    return date

def get_search_term_from_user():
    print("Please enter in a search term (lowercase) for the API you chose:", end = " ")
    search_input = input()
    return search_input


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

def query_stackoverflow_for_questions(API_name):
    # dictionary of various key value pairs 
    stored_quests = get_stored_questions(API_name)
    return stored_quests