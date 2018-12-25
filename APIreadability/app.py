from bagofwords import Bagofwords
from flask import Flask, jsonify, render_template, request
from impasse import json_dump
from questionretrieval import parse_links, parse_questions, query_stackoverflow_for_questions

import collections
import os

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

@app.route('/search_api')
def search_api():
    
    API = request.args.get('API', " ", type=str)

    questions = query_stackoverflow_for_questions(API)
    
    # parses the questions from the dictionary obtained from stackoverflow
    # parsed_questions is a dictionary that maps the title of the question
    # to the full question
    parsed_questions = parse_questions(questions)

    # parses the links from the dictionary obtained from stackoverflow
    # links is a dictionary that maps the title of the question to the
    # link to the question
    links = parse_links(questions)

    bw = Bagofwords()
    # Parses the corpus to collect all of the invdividual terms and stores it 
    # into a vocabulary. This vocabulary is a list of strings
    vocabulary = bw.tokenize_corpus(parsed_questions)
    print("Creating Final List")
    # Performs a bag of words algorithm on the corpus of questions based on all of the 
    # terms of the vocabulary.
    # Returns a dictionary which maps a term in the vocabulary to another dictionary
    # which maps a corresponding 
    list_of_scores = bw.create_final_list(vocabulary, parsed_questions)

    # for scores in list_of_scores.keys():
    #     print(scores, ", ", list_of_scores[scores])
    print("Compiling Final list")
    list_of_score_titles = {}
    for score_title in list_of_scores.keys():
        list_of_score_titles[score_title] = len(list_of_scores[score_title])

    list_of_questions = {}
    for score_title in list_of_scores.keys():
        list_questions = []
        for question in list_of_scores[score_title].keys():
            list_questions.append(question)
        list_of_questions[score_title] = list_questions
    print("Jsonify the lists")

    return json_dump(API, links, list_of_questions)

@app.route('/')
def index():
    return render_template('APIdisplay.html')

if __name__ == "__main__":
    app.run()