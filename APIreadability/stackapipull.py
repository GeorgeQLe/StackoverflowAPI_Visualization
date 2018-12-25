# Copyright 2018 George Le

from stackapi import StackAPI
from datetime import datetime

class Date():

    def __init__(self, day = 1, month = 1, year = 1970):
        self.day = day
        self.month = month
        self.year = year

def get_stored_questions(API_name, Start_date = Date(1, 1, 2010), End_date = Date(12, 18, 2018)):
    site = StackAPI('stackoverflow')

    site.max_pages = 1 

    questions = site.fetch('questions', fromdate=datetime(2010, 1, 1), todate=datetime(2018, 12, 18), tagged=API_name) 

    stored_quest = dict()
    stored_quests = list()

    # accesses the dict that is stored at questions['items]
    for lists in questions['items']:
        # stores only the relevant key value pairs into a new dict stored_quests
        stored_quest = {
            "title": lists.get("title"),
            "score": lists.get("score"),
            "is_answered": lists.get("is_answered"),
            "tags": lists.get("tags"),
            "question_id": lists.get("question_id"),
            "link": lists.get("link")
        }
        stored_quests.append(stored_quest)
            
    return stored_quests

def get_stored_answers(id):
    site = StackAPI('stackoverflow')

    site.max_pages = 1

    answers = site.fetch('answers', id)

    return answers