# Copyright 2018 George Le

from stackapi import StackAPI
from datetime import datetime
from bokeh.plotting import figure, output_file, show

site = StackAPI('stackoverflow') 

site.max_pages=1 

questions = site.fetch('questions', fromdate=datetime(2017, 9, 1), todate=datetime(2017, 9, 7), tagged='SFML') 

i = 1

stored_quests = dict()

# accesses the dict that is stored at questions['items]
for lists in questions['items']: 
    print ('Stack Overflow entry: ', i)
    i+=1
    # accesses the keys of the dict
    for keys in lists.keys(): 
        if keys not in ('question_id', 'owner', 'creation_date', 'last_activity_date', 'last_edit_date'):
            print (keys, ': ', lists[keys])
            # stores only the relevant key value pairs into a new dict stored_quests
            stored_quests = { keys: lists[keys] }

# prepare some test data
x = [ 1, 2, 3, 4, 7 ]
y = [ 6, 3, 4, 5, 10 ]
z = 5

# output to static HTML file
output_file("lines.html")

# create a new plot with a title and axis labels
p = figure(title="simple line example", x_axis_label='x', y_axis_label='y')

# add a line renderer with legend and line thickness
p.line(x, y, legend="Temp.", line_width=2)

# add a circle with legend, color, and size
p.circle(z, z, legend="y=x", fill_color="white", size=10)

# show the results
show(p)

# if isinstance(questions['items'][1].keys(), list): 
#  print ('good') 
# else: 
#  print ('bad')