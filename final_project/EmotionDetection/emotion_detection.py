import requests
import json



def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {
        "Content-Type": "application/json",
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }
    data = {
        "raw_document": {
            "text": text_to_analyze
        }
    }

    try:
        # Make the POST request with timeout
        response = requests.post(url, headers=headers, json=data, timeout=10)
        response.raise_for_status()  # Raises error for bad HTTP codes

        # Parse JSON response
        result = response.json()

        # Check expected structure
        if 'emotionPredictions' not in result or not result['emotionPredictions']:
            return {"error": "No emotion predictions found in response"}

        emotions = result['emotionPredictions'][0].get('emotion', {})

        # Safely extract emotion scores
        scores = {
            'anger': emotions.get('anger', 0),
            'disgust': emotions.get('disgust', 0),
            'fear': emotions.get('fear', 0),
            'joy': emotions.get('joy', 0),
            'sadness': emotions.get('sadness', 0)
        }

        dominant_emotion = max(scores, key=scores.get)

        return {**scores, 'dominant_emotion': dominant_emotion}

    except requests.exceptions.RequestException as e:
        return {"error": f"Request failed: {str(e)}"}
    except json.JSONDecodeError:
        return {"error": "Failed to decode JSON response from API"}
    except Exception as e:
        return {"error": f"An unexpected error occurred: {str(e)}"}
