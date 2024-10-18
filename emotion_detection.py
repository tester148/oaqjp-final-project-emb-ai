import requests

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = {
        "raw_document": {
            "text": text_to_analyze}}
    try:
        response = requests.post(url, headers=headers, json=input_json)
        response.raise_for_status() 
        response_json = response.json()
        print("Response JSON:", response_json) # i am outpuying
        emotions = response_json.get('emotion', {})  
        return emotions

    except requests.exceptions.RequestException as e:
        return f"Request failed: {e}"


