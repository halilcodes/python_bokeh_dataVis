from random import randrange

from bokeh.io import curdoc
from bokeh.models import ColumnDataSource
from bokeh.plotting import figure

# create figure
f = figure(x_range=(0, 11), y_range=(0, 11))

# create ColumnDataSource
source = ColumnDataSource(dict(x=[], y=[]))

# create glyphs
f.circle(x='x', y='y', color='olive', line_color='yellow', source=source, size=14)
f.line(x='x', y='y', line_color='red', source=source)


# create periodic function
def update():
    new_data = dict(x=[randrange(1, 10)], y=[randrange(1, 10)])
    source.stream(new_data, rollover=15)
    print(source.data)


curdoc().add_root(f)
curdoc().add_periodic_callback(update, 1000)
