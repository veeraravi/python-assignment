from flask import Flask, request, jsonify

app = Flask(__name__)
FIELDS = {
    "title": str,
    "rating": int,
    "year": int,
    "genre": str,
}
movies = {}
current_id = 1


@app.route("/", methods=["GET"])
def list_movies():
    ordering = request.args.get("ordering")
    page = int(request.args.get("page", 1))
    page_size = 10

    movie_list = list(movies.values())

    if ordering and ordering in FIELDS:
        movie_list.sort(key=lambda x: x.get(ordering))

    start = (page - 1) * page_size
    end = start + page_size
    return jsonify(movie_list[start:end]), 200


@app.route("/", methods=["POST"])
def create_movie():
    global current_id
    data = request.get_json()
    
    if not data or any(field not in data or not isinstance(data[field], FIELDS[field]) for field in FIELDS):
        return jsonify({"error": "Bad request"}), 400

    new_movie = {**data, "id": current_id}
    movies[current_id] = new_movie
    current_id += 1
    return jsonify(new_movie), 201


@app.route("/<int:movie_id>/", methods=["GET"])
def movie_details(movie_id):
    if movie_id not in movies:
        return jsonify({"error": "Not found"}), 404
    return jsonify(movies[movie_id]), 200


@app.route("/<int:movie_id>/", methods=["PUT"])
def modify_movie(movie_id):
    if movie_id not in movies:
        return jsonify({"error": "Not found"}), 404

    data = request.get_json()
    
    if not data or any(field not in FIELDS for field in data):
        return jsonify({"error": "Bad request"}), 400
    
    if 'rating' in data and (data['rating'] < 1 or data['rating'] > 5):
        return jsonify({"error": "Bad request"}), 400

    for field in data:
        if field in FIELDS:
            movies[movie_id][field] = data[field]

    return jsonify(movies[movie_id]), 200


@app.route("/<int:movie_id>/", methods=["DELETE"])
def delete_movie(movie_id):
    if movie_id not in movies:
        return jsonify({"error": "Not found"}), 404
    del movies[movie_id]
    return '', 204


if __name__ == "__main__":
    app.run(debug=True)
