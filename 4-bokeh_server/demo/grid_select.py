# importing libraries
from bokeh.plotting import figure
from bokeh.io import curdoc
from bokeh.models.annotations import Span
from bokeh.models import ColumnDataSource
from bokeh.models.widgets import Select
from bokeh.layouts import layout, gridplot
from bokeh.sampledata.periodic_table import elements

elements = elements.dropna()

colormap = {
    "gas": "yellow",
    "liquid": "orange",
    "solid": "red"
}
elements['color'] = [colormap[i] for i in elements['standard state']]

elements['size'] = elements['van der Waals radius'] / 10

# Create ColumnDataSources
gas = ColumnDataSource(elements[elements['standard state'] == 'gas'])
liquid = ColumnDataSource(elements[elements['standard state'] == 'liquid'])
solid = ColumnDataSource(elements[elements['standard state'] == 'solid'])

# Create the figure object
f = figure()

# adding glyphs
f.circle(x='atomic radius', y='boiling point', size='size', fill_alpha=0.5,
         color="color", line_dash='dotted', legend_label='Gas', source=gas)

f.circle(x='atomic radius', y='boiling point', size='size', fill_alpha=0.35,
         color="color", line_dash='dotted', legend_label='Liquid', source=liquid)

f.circle(x='atomic radius', y='boiling point', size='size', fill_alpha=0.2,
         color="color", line_dash='dotted', legend_label='Solid', source=solid)


f.xaxis.axis_label = "Atomic Radius"
f.yaxis.axis_label = "Boiling Point"

# add gas and liquid spans / default for solid span
gas_mean = gas.data['boiling point'].mean()
gas_span = Span(location=gas_mean, dimension='width', line_color=gas.data['color'][0], line_width=2)

liquid_mean = liquid.data['boiling point'].mean()
liquid_span = Span(location=liquid_mean, dimension='width', line_color=liquid.data['color'][0], line_width=2)

solid_mean = solid.data['boiling point'].mean()
solid_span = Span(location=solid_mean, dimension='width', line_color=solid.data['color'][0], line_width=2)


# create function
def update_point(attr, old, new):
    val = select.value
    if val == "average_point":
        solid_span.location = solid.data['boiling point'].mean()
    elif val == "minimum_point":
        solid_span.location = solid.data['boiling point'].min()
    else:
        solid_span.location = solid.data['boiling point'].max()


# create select widget
options = [("average_point", "Solid Average Boiling Point"),
           ("minimum_point", "Solid Minimum Boiling Point"),
           ("maximum_point", "Solid Maximum Boiling Point")]
select = Select(title="Select Span Value", options=options)
select.on_change("value", update_point)


# add layouts for gas and liquid
f.add_layout(gas_span)
f.add_layout(liquid_span)
f.add_layout(solid_span)

# add curdoc sor solid apan
lay_out = layout([[select]])
curdoc().add_root(f)
curdoc().add_root(lay_out)
