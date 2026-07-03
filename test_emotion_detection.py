"""
Unit tests for the Emotion Detection application
"""

import pytest
from EmotionDetection.emotion_detection import emotion_detector


class TestEmotionDetection:
    """Test cases for emotion_detector function"""
    
    def test_emotion_detector_joy(self):
        """Test emotion detection for positive/joy text"""
        result = emotion_detector("I love this so much!")
        assert result['dominant_emotion'] == 'joy'
        assert result['joy'] is not None
    
    def test_emotion_detector_anger(self):
        """Test emotion detection for anger"""
        result = emotion_detector("I am so angry!")
        assert result['dominant_emotion'] == 'anger'
        assert result['anger'] is not None
    
    def test_emotion_detector_disgust(self):
        """Test emotion detection for disgust"""
        result = emotion_detector("This is disgusting!")
        assert result['dominant_emotion'] == 'disgust'
        assert result['disgust'] is not None
    
    def test_emotion_detector_sadness(self):
        """Test emotion detection for sadness"""
        result = emotion_detector("I am so sad.")
        assert result['dominant_emotion'] == 'sadness'
        assert result['sadness'] is not None
    
    def test_emotion_detector_fear(self):
        """Test emotion detection for fear"""
        result = emotion_detector("I am afraid!")
        assert result['dominant_emotion'] == 'fear'
        assert result['fear'] is not None
    
    def test_emotion_detector_blank_input(self):
        """Test emotion detection with blank input"""
        result = emotion_detector("")
        assert result['status_code'] == 400
        assert result['dominant_emotion'] is None
    
    def test_emotion_detector_none_input(self):
        """Test emotion detection with None input"""
        result = emotion_detector(None)
        assert result['status_code'] == 400
        assert result['dominant_emotion'] is None
    
    def test_emotion_detector_whitespace_input(self):
        """Test emotion detection with whitespace-only input"""
        result = emotion_detector("   ")
        assert result['status_code'] == 400
        assert result['dominant_emotion'] is None
    
    def test_emotion_detector_response_format(self):
        """Test that emotion detector returns correct response format"""
        result = emotion_detector("I feel happy")
        assert 'anger' in result
        assert 'disgust' in result
        assert 'fear' in result
        assert 'joy' in result
        assert 'sadness' in result
        assert 'dominant_emotion' in result
    
    def test_emotion_detector_all_scores_present(self):
        """Test that all emotion scores are present for valid input"""
        result = emotion_detector("I feel great!")
        assert result['anger'] is not None
        assert result['disgust'] is not None
        assert result['fear'] is not None
        assert result['joy'] is not None
        assert result['sadness'] is not None


if __name__ == '__main__':
    pytest.main([__file__, '-v'])