from flask import Flask, render_template, request, jsonify
from flask_wtf.csrf import CSRFProtect, generate_csrf

app = Flask(__name__)
app.secret_key = 'your_secret_key'
csrf = CSRFProtect(app)

balance = 2000

@app.route('/')
def index():
    csrf_token= generate_csrf()
    print("CSRF Token for this session: " , csrf_token)
    return render_template('index.html', csrf_token=csrf_token)


@app.route('/balance', methods=['POST'])
def get_balance():
    csrf_token = request.form.get('csrf_token')
    if not csrf_token:
        return jsonify({"error": "CSRF token is missing."}), 403
    return jsonify({"balance": balance})

@app.errorhandler(400)
def bad_request(e):
    return jsonify({"error": "Bad Request: " + str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
