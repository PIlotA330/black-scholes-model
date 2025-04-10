from scipy.stats import norm
import math

S = 100  #current stock price
K = 100  #strike price
r = 0.05  #risk free rate
T = 1  #time to expiration
sigma = 0.2  #volatility

def calc_bsm_call(price, strike, rate, time, vol):
    d1 = (math.log(price/strike) + (rate+(math.pow(vol, 2)/2))*time)/(vol*math.sqrt(time))
    d2 = d1 - (vol*math.sqrt(time))

    BSMpred = (price*norm.cdf(d1)) - (strike*math.exp(-1*rate*time)*norm.cdf(d2))
    return BSMpred

def calc_bsm_put(price, strike, rate, time, vol):
    d1 = (math.log(price/strike) + (rate+(math.pow(vol, 2)/2))*time)/(vol*math.sqrt(time))
    d2 = d1 - (vol*math.sqrt(time))

    BSMpred = (strike*math.exp(-1*rate*time)*norm.cdf(-1*d2)) - (price*norm.cdf(-1*d1))
    return BSMpred

print(calc_bsm_call(S, K, r, T, sigma))
print(calc_bsm_put(S, K, r, T, sigma))