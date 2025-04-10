from flask import Flask
from model import calc_bsm_call, calc_bsm_put

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

# /api/"price,strike,rate,time,vol"
@app.route("/api/<string:data>")
def page(data):
    dataConverted = list(map(float, data.split(",")))
    cPrice = calc_bsm_call(dataConverted[0], dataConverted[1], dataConverted[2], dataConverted[3], dataConverted[4])
    pPrice = calc_bsm_put(dataConverted[0], dataConverted[1], dataConverted[2], dataConverted[3], dataConverted[4])
    return f'<p>Call: { cPrice } and Put: { pPrice }</p>'