from flask import Flask
from model import calc_bsm_call, calc_bsm_put

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/<float:price>/<float:strike>/<float:rate>/<float:time>/<float:vol>")
def page(price, strike, rate, time, vol):
    cPrice = calc_bsm_call(price, strike, rate, time, vol)
    pPrice = calc_bsm_put(price, strike, rate, time, vol)
    return f'<p>Call: { cPrice } and Put: { pPrice }</p>'