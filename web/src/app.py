from flask import Flask, render_template, request
import pandas as pd
from bokeh.plotting import figure, curdoc
from bokeh.embed import components
from bokeh.models import ColumnDataSource

app = Flask(__name__)


# # Create the main plot
# def create_figure(x_name):
#     plot = figure(plot_width=400, plot_height=400)
#     plot.circle([1, 2], [3, 4])
#
#     # Set the x axis label
#     plot.xaxis.axis_label = x_name
#
#     # Set the y axis label
#     plot.yaxis.axis_label = 'Count'
#     return plot


data = {'x_values': [1],
        'y_values': [1]}

source = ColumnDataSource(data=data)


def add_data():

    new_data = {'x_values': [2], 'y_values': [2]}
    source.stream(new_data=new_data, rollover=1000)

    return


@app.route('/')
def index():

    x_name = 'x-axislabel'

    plot = figure(plot_width=400, plot_height=400)
    plot.circle(x='x_values', y='y_values', source=source)

    curdoc().add_periodic_callback(add_data, 5000)
    # Embed plot into HTML via Flask Render
    script, div = components(plot)
    return render_template("index.html", script=script, div=div,
                           x_name=x_name)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
