from bokeh.plotting import figure
from bokeh.embed import components
from bokeh.resources import CDN

x = [1, 2, 3, 4, 5]
y = [i for i in range(6, 11)]

f = figure()
f.line(x, y)

js, div = components(f)
cdn_js = CDN.js_files[0]
# cdn_css = CDN.css_files[0]    # depreciated
