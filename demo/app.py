from flask import Flask, make_response

app = Flask(__name__)

@app.route('/role', methods=['GET'])
def role():
    # Create a response object
    response = make_response("OK", 200)
    # Add Cache-Control header to the response
    response.headers['Cache-Control'] = 'max-age=600'
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

