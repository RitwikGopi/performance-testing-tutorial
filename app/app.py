from flask import Flask, jsonify, request
import search

app = Flask(__name__)


@app.route("/search", methods=["POST"])
def searh():
    s = request.data.decode("utf-8")
    return search.first_non_repeating_char_bruteforce(s)
    # Comment the above line and uncomment below to use efficient algorithm
    # return search.first_non_repeating_char_hashmap(s)


