from bokeh.io import curdoc
from bokeh.models import ColumnDataSource, DatetimeTickFormatter
from bokeh.models.widgets import Select
from bokeh.plotting import figure
import requests
import datetime as dt
from math import radians
from bokeh.layouts import layout
from pytz import timezone


# binance API endpoints and headers
url = "https://api.binance.com/api/v3/klines"
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


# get the latest data from binance instead of instructor's bullshit site
def get_crypto_value(symbol="LINKUSDT"):
    params = {"symbol": symbol,
              "interval": "1m",
              "limit": 1}
    req = requests.get(url, headers=headers, params=params)
    content = req.json()[0]
    data = {
        "open_time": float(content[0]) / 1000,
        "open_price": float(content[1]),
        "high_price": float(content[2]),
        "low_price": float(content[3]),
        "close_price": float(content[4]),
        "volume": content[5],
        "num_of_trades": content[8],
    }
    return data["close_price"]


# create figure
f = figure(x_axis_type='datetime', width=2000)

# create ColumnDataSource
source = ColumnDataSource(dict(x=[], y=[]))

# create glyphs
f.circle(x='x', y='y', color='olive', line_color='yellow', source=source, size=14)
f.line(x='x', y='y', line_color='red', source=source)


def update():
    new_data = dict(x=[dt.datetime.now()], y=[get_crypto_value(select.value)])
    # new_data = dict(x=[dt.datetime.now(timezone("turkey"))], y=[get_crypto_value(symbol)])
    source.stream(new_data, rollover=650)


def update_intermediate(attr, old, new):
    source.data = dict(x=[], y=[])
    update()


# Format x axis as datetime
f.xaxis.formatter = DatetimeTickFormatter(seconds=["%y-%m-%d-%H:%M:%S %Z"],
                                          minsec=["%y-%m-%d-%H:%M:%S"],
                                          minutes=["%y-%m-%d-%H:%M:%S"],
                                          hourmin=["%y-%m-%d-%H:%M:%S"],
                                          hours=["%y-%m-%d-%H:%M:%S"],
                                          days=["%y-%m-%d-%H:%M:%S"],
                                          months=["%y-%m-%d-%H:%M:%S"],
                                          years=["%y-%m-%d-%H:%M:%S"])

f.xaxis.major_label_orientation = radians(90)


# create select widget
options = [("LINKUSDT", "Get LINKUSDT Graph"),
           ("BTCUSDT", "Get BTCUSDT Graph"),
           ("SOLUSDT", "Get SOLUSDT Graph")]
select = Select(title="Trading Pair", value="LINKUSDT", options=options)
select.on_change("value", update_intermediate)

# add figure to curdoc and configure callback
lay_out = layout([[f], [select]])
curdoc().add_root(lay_out)
curdoc().add_periodic_callback(update, 1000)
