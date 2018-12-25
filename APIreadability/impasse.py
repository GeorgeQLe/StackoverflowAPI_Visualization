from flask import jsonify
import json
import os

def json_dump(API, links, list_of_questions_sorted):
    # filename_links = "links_results"
    # filename_questions = "questions_results"
    # filetype = ".json"

    # filename_links += "_" + API + "_" + filetype
    # filename_questions += "_" + API + "_" + filetype

    # if(os.path.isfile(filename_links)):
    #     os.remove(filename_links)
    # if(os.path.isfile(filename_questions)):
    #     os.remove(filename_questions)

    # with open(filename_links, 'w') as fp:
    #     json.dump(links, fp, indent = 4)           
    # with open(filename_questions, 'w') as fp:
    #     json.dump(list_of_questions_sorted, fp, indent = 4)

    jsonlist = []

    jsonlist.append(links)
    jsonlist.append(list_of_questions_sorted)
    
    return jsonify(jsonlist)