# import libraries
from bokeh.io import curdoc
from bokeh.models import ColumnDataSource
from bokeh.plotting import figure
from random import randrange
from bokeh.embed import components
from bokeh.resources import CDN


# create figure
f = figure(x_range=(0, 11), y_range=(0, 11), name="bokeh_server_figure")

# create ColumnDataSource
source = ColumnDataSource(data=dict(x=[], y=[]))

# create glyphs
f.circle(x='x', y='y', size=8, fill_color='olive', line_color='yellow', source=source)


# create periodic function
def update():
    new_data = dict(x=[randrange(1, 10)], y=[randrange(1, 10)])
    source.stream(new_data, rollover=15)
    # print(source.data)



# add figure to curdoc and configure callback
curdoc().add_root(f)
curdoc().add_periodic_callback(update, 1000)
js, div = components(f)
cdn_js = CDN.js_files[0]
