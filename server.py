"""
Flask server for the Emotion Detection application
Provides REST API endpoints for emotion analysis
"""

from flask import Flask, request, jsonify, render_template
from EmotionDetection.emotion_detection import emotion_detector


app = Flask(__name__)


@app.route('/')
def index():
    """Serve the home page"""
    return render_template('index.html')


@app.route('/emotion_detector', methods=['POST'])
def detect_emotion():
    """
    API endpoint for emotion detection
    
    Expected request body:
    {
        "textToAnalyze": "text to analyze"
    }
    
    Returns:
    {
        "anger": float,
        "disgust": float,
        "fear": float,
        "joy": float,
        "sadness": float,
        "dominant_emotion": string
    }
    """
    
    # Get request data
    request_body = request.get_json()
    
    # Handle missing or invalid request body
    if not request_body:
        return jsonify({
            'error': 'Request body is missing',
            'status_code': 400
        }), 400
    
    # Extract text to analyze
    text_to_analyze = request_body.get('textToAnalyze', '')
    
    # Check for blank input
    if not text_to_analyze or text_to_analyze.strip() == '':
        return jsonify({
            'error': 'Please enter some text to analyze',
            'status_code': 400
        }), 400
    
    # Perform emotion detection
    emotion_result = emotion_detector(text_to_analyze)
    
    # Check for errors from emotion detector
    if emotion_result.get('status_code') == 400:
        return jsonify({
            'error': 'Error in emotion detection',
            'status_code': 400
        }), 400
    
    # Return successful response
    return jsonify(emotion_result), 200


@app.route('/analyze', methods=['GET'])
def analyze():
    """
    Analyze endpoint for GET requests
    
    Query parameters:
    - text_to_analyze: The text to analyze
    
    Returns:
    - JSON response with emotion scores
    """
    
    # Get text from query parameters
    text_to_analyze = request.args.get('text_to_analyze', '')
    
    # Check for blank input
    if not text_to_analyze or text_to_analyze.strip() == '':
        return jsonify({
            'error': 'Please provide text to analyze',
            'status_code': 400
        }), 400
    
    # Perform emotion detection
    emotion_result = emotion_detector(text_to_analyze)
    
    # Check for errors
    if emotion_result.get('status_code') == 400:
        return jsonify({
            'error': 'Invalid input',
            'status_code': 400
        }), 400
    
    return jsonify(emotion_result), 200


@app.errorhandler(400)
def bad_request(error):
    """Handle 400 Bad Request errors"""
    return jsonify({'error': 'Bad request', 'status_code': 400}), 400


@app.errorhandler(404)
def not_found(error):
    """Handle 404 Not Found errors"""
    return jsonify({'error': 'Endpoint not found', 'status_code': 404}), 404


@app.errorhandler(500)
def internal_error(error):
    """Handle 500 Internal Server errors"""
    return jsonify({'error': 'Internal server error', 'status_code': 500}), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)