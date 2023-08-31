from random import randrange
from bokeh.io import curdoc
from bokeh.models import ColumnDataSource
from bokeh.plotting import figure
import requests

# create figure
f = figure(x_range=(0, 11), y_range=(0, 11))

# create columndatasource
source = ColumnDataSource(dict(x=[], y=[]))

# create glyphs
f.circle(x='x', y='y', color='olive', line_color='yellow', source=source, size=14)

# get the latest data from binance instead of instructor's bullshit site
url = "https://api.binance.com/api/v3/trades?symbol=BTCUSDT"
headers = {
    'pragma': 'no-cache',
    'cache-control': 'no-cache',
    'dnt': '1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/51.0.2704.64 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,'
              'application/signed-exchange;v=b3;q=0.9',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
}

def get_btc_value():
    req = requests.get(url, headers=headers)
    last_price = round(float(req.json()[-1]['price']), 2)
    return last_price


def update():
    new_data = dict(x=[randrange(1, 10)], y=[randrange(1, 10)])
    source.stream(new_data, rollover=15)
    print(source.data)

# add figure to curdoc and configure callback
curdoc().add_root(f)
curdoc().add_periodic_callback(update, 1000)