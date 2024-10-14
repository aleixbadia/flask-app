from flask import Flask, jsonify, Response
from prometheus_client import Counter, generate_latest

app = Flask(__name__)

# Existing functionality
@app.route('/message', methods=['GET'])
def get_message():
    data = {"message": "Hello, Cloud Native!"}
    return jsonify(data)

# Prometheus metric: Counter for HTTP requests
request_count = Counter('http_requests_total', 'Total HTTP Requests')

@app.route('/')
def index():
    request_count.inc()  # Increment the counter for each request
    return "Hello, World!"

# Prometheus metrics endpoint
@app.route('/metrics')
def metrics():
    return Response(generate_latest(), mimetype='text/plain')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
