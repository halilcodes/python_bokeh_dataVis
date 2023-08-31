"""
This script duplicates widgets.py with required amount of text inputs,
buttons and corresponding outputs.
"""


# import libraries
from bokeh.io import curdoc
from bokeh.models.widgets import TextInput, Button, Paragraph
from bokeh.layouts import layout

widgets = dict()
count = 5
layout_list = []


for i in range(1, count+1):
    widgets[f'row{i}'] = {
        f"text_input{i}": TextInput(value=f'input {i}'),
        f"button{i}": Button(label=f'button {i}'),
        f"output{i}": Paragraph()
    }

    def update(j=i):
        widgets[f'row{j}'][f"output{j}"].text = "hello, " + widgets[f'row{j}'][f"text_input{j}"].value


    widgets[f'row{i}'][f"button{i}"].on_click(update)


for _, value_dict in widgets.items():
    to_append = [value for _, value in value_dict.items()]
    layout_list.append(to_append)


lay_out = layout(layout_list)

curdoc().add_root(lay_out)

# in terminal: bokeh serve widgets.py