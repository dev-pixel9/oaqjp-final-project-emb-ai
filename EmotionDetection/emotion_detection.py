"""
Emotion Detection module using Watson NLP Library
"""

import json
from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_watson.watson_service import watson_logging
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_cloud_sdk_core.get_authenticator import get_authenticator_from_environment


def emotion_detector(text_to_analyze):
    """
    Detects emotions in the provided text using Watson NLP.
    
    Args:
        text_to_analyze (str): The text to analyze for emotions
        
    Returns:
        dict: A dictionary containing emotion scores and the dominant emotion,
              or an error response with status_code 400 if input is invalid
    """
    
    # Validate input
    if not text_to_analyze or text_to_analyze.strip() == "":
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None,
            'status_code': 400
        }
    
    # Set up Watson NLU authenticator
    authenticator = get_authenticator_from_environment('WATSON_NLU')
    nlu = NaturalLanguageUnderstandingV1(
        version='2021-08-01',
        authenticator=authenticator,
        service_url='https://api.us-south.natural-language-understanding.watson.cloud.ibm.com'
    )
    
    # Perform emotion analysis
    try:
        response = nlu.analyze(
            text=text_to_analyze,
            features={
                'emotion': {}
            }
        ).get_result()
        
        # Extract emotion scores
        emotion_scores = response['emotion']['document']['emotion']
        
        # Find dominant emotion
        dominant_emotion = max(emotion_scores, key=emotion_scores.get)
        
        # Format and return response
        return {
            'anger': emotion_scores.get('anger'),
            'disgust': emotion_scores.get('disgust'),
            'fear': emotion_scores.get('fear'),
            'joy': emotion_scores.get('joy'),
            'sadness': emotion_scores.get('sadness'),
            'dominant_emotion': dominant_emotion
        }
    
    except Exception as exception:
        # Return error response for any API failures
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None,
            'status_code': 400
        }