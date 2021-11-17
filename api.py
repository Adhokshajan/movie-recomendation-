from flask import Flask, jsonify, request
import csv 

all_movies = []
liked_movies = []
unliked_movies = []
didnot_watch=[]
with open("movies.csv", encoding='utf8') as f:
    reader = csv.reader(f)
    data = list(reader)
    all_movies = data[1:]


app = Flask(__name__)

@app.route("/")
def index():
    return jsonify({
        "data": all_movies[0],
        "message": "success"
    })

@app.route("/liked-movies", methods=["POST"])
def liked_movies():
    movie = all_movies[0]
    all_movies = all_movies[1:]
    liked_movies.append(movie)
    return jsonify({
        "status": "success"
    })

@app.route("/unliked-movies", methods=["POST"])
def unliked_movies():
    movie = all_movies[0]
    all_movies= all_movies[1:]
    unliked_movies.append(movie)
    return jsonify({
        "status": "success"
    })






@app.route("/didnotwatch-movies", methods=["POST"])
def didnot_watch():
    movie = all_movies[0]
    all_movies= all_movies[1:]
    didnot_watch.append(movie)
    return jsonify({
        "status": "success"
    })












if __name__ == "__main__":
    app.run(debug = True)
