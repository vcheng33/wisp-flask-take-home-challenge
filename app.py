from flask import Flask, jsonify
from special_math import special_math

app = Flask(__name__)


@app.get('/specialmath/<int:num>')
def calc_and_return_special_math(num):
    """ Calculates a special number based on the int provided """

    try:
        result = special_math(num)
        return jsonify(result=result)
    except ValueError as error:
        return str(error), 400