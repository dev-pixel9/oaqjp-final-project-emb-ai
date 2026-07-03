# Emotion Detector - Final Project

## Project Overview

This project is an AI-based web application that detects emotions from text using the IBM Watson NLP library. The application analyzes input text and classifies emotions including joy, fear, anger, sadness, and disgust.

## Project Structure

```
oaqjp-final-project-emb-ai/
├── README.md
├── requirements.txt
├── server.py
├── test_emotion_detection.py
├── EmotionDetection/
│   ├── __init__.py
│   └── emotion_detection.py
├── templates/
│   └── index.html
└── static/
    └── styles.css
```

## Features

- **Emotion Detection**: Classifies text into emotions (joy, fear, anger, sadness, disgust)
- **REST API**: Flask-based web service for emotion detection
- **Error Handling**: Comprehensive error handling for invalid inputs
- **Unit Tests**: Full test coverage using pytest
- **Static Code Analysis**: Code quality checks using pylint

## Installation

1. Clone the repository:
```bash
git clone https://github.com/dev-pixel9/oaqjp-final-project-emb-ai.git
cd oaqjp-final-project-emb-ai
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Running the Web Application

```bash
python server.py
```

The application will be available at `http://localhost:5000`

### Running Unit Tests

```bash
python -m pytest test_emotion_detection.py -v
```

### Running Static Code Analysis

```bash
python -m pylint server.py emotion_detection.py --disable=all --enable=E,F
```

## Technologies Used

- **Python 3.x**
- **Flask** - Web framework
- **Watson NLP** - Emotion detection engine
- **pytest** - Unit testing framework
- **pylint** - Static code analysis

## License

This project is licensed under the Apache License 2.0 - see the LICENSE file for details.