from flask import Flask, jsonify, request
app = Flask(__name__)
heart = [
    {
        "heart_id": "1911503",
        "date": "November 29, 2023",
        "heart_rate": "80/120"
    },
    {
        "heart_id": "1911504",
        "date": "November 28, 2023",
        "heart_rate": "70/130"
    }
]
@app.route('/Heart', methods=['GET'])
def getHeart():
    return jsonify(heart)

#@app.route('/Heart/<int:index>', methods=['GET'])
#def get2Heart():
#    heart == index
#    return jsonify(heart)

@app.route('/Heart', methods=['POST'])
def addHeart():
    hearts = request.get_json()
    heart.append(hearts)
    return {'id': len(heart)}, 200

@app.route('/Heart/<int:index>', methods=['DELETE'])
def delHeart(index):
    heart.pop(index)
    return 'The heart has been broken', 200


if __name__ == '__main__':
    app.run()