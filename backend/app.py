from flask import Flask, jsonify
from model import calc_bsm_call, calc_bsm_put, calc_delta, calc_gamma, calc_intrinsic, calc_rho, calc_theta, calc_vega
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

# /api/"price,strike,rate,time,vol"
@app.route("/api/<string:data>", methods=['GET'])
def page(data):
    dataConverted = list(map(float, data.split(",")))
    cPrice = calc_bsm_call(dataConverted[0], dataConverted[1], dataConverted[2], dataConverted[3], dataConverted[4])
    pPrice = calc_bsm_put(dataConverted[0], dataConverted[1], dataConverted[2], dataConverted[3], dataConverted[4])
    delta = calc_delta(dataConverted[0], dataConverted[1], dataConverted[2], dataConverted[3], dataConverted[4])
    gamma = calc_gamma(dataConverted[0], dataConverted[1], dataConverted[2], dataConverted[3], dataConverted[4])
    vega = calc_vega(dataConverted[0], dataConverted[1], dataConverted[2], dataConverted[3], dataConverted[4])
    theta = calc_theta(dataConverted[0], dataConverted[1], dataConverted[2], dataConverted[3], dataConverted[4])
    rho = calc_rho(dataConverted[0], dataConverted[1], dataConverted[2], dataConverted[3], dataConverted[4])
    intrinsic = calc_intrinsic(dataConverted[0], dataConverted[1])

    return jsonify({"price" : {
        "call" : cPrice, "put" : pPrice
    }, "greek" : {
        "delta" : {
            "call" : delta[0],
            "put" : delta[1]
        }, "gamma" : gamma,
        "vega" : vega,
        "theta" : {
            "call" : theta[0],
            "put" : theta[1]
        }, "rho" : {
            "call" : rho[0],
            "put" : rho[1]
        }
    }, "intrinsic": {
        "call" : intrinsic[0],
        "put" : intrinsic[1]
    }})