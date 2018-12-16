from bokeh.plotting import figure, output_file, show
from bokeh.models import Legend, LegendItem

def CreateBarGraph(output_file_name, graph_name, stored_quests, x_axis_name, y_axis_name, bar_color):
    # output to static HTML file
    output_file(output_file_name)

    # create a new plot with a title and axis labels
    p = figure(title = graph_name, x_axis_label = x_axis_name, y_axis_label= y_axis_name)

    legend_items = []

    i = 0 # counter value of the stored_questions

    print ("Building bar graph")
    # compiling the data based on what pairs you want, build the bar graph from the data
    for val_pair in stored_quests:
        for key in val_pair.keys():
            if key == y_axis_name:
                print (str(i + 1) + " : " + stored_quests[i]['title'])
                p.vbar(x = i + 1, width = 0.5, bottom = 0, top = val_pair[key], color = bar_color)
                legend_items.append(LegendItem())
                legend_items[i].label = str(i + 1) + " : " + stored_quests[i]['title']
                square = p.square(x = 0, y = 0, fill_color = None, line_color = bar_color)
                legend_items[i].renderers = [square]
        i+=1

    legend = Legend(items=legend_items, location= (0, 0))
    legend.click_policy="mute"

    p.add_layout(legend, 'right')

    # show the results
    show(p)