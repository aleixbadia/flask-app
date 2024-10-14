from flask import Flask, jsonify, request
import os
import logging

app = Flask(__name__)

# Set up logging
logging.basicConfig(level=logging.INFO)

# Health check endpoint
@app.route('/health', methods=['GET'])
def health():
    return jsonify(status="healthy"), 200

@app.route('/data', methods=['GET'])
def get_data():
    # Simulating data fetching
    try:
        param = request.args.get('param', default='default_value', type=str)
        # Log the request
        app.logger.info(f"Received request with param: {param}")

        # Simulated data response
        response_data = {"data": f"Data fetched with param: {param}"}
        return jsonify(response_data), 200

    except Exception as e:
        app.logger.error(f"Error occurred: {e}")
        return jsonify(error=str(e)), 500

if __name__ == '__main__':
    # Use the port from environment variables or default to 5000
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

