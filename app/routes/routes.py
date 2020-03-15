from app import app
from flask import jsonify, request
from ..views import price



@app.route('/ibapi/price/hist', methods=['POST'])
def get_hist_price():
    
    return price.get_price_hist()

@app.route('/ibapi/price/book', methods=['POST'])
def get_book_price():
    return price.auth()