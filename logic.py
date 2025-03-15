from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/get_response', methods=['POST'])
def get_response():
    user_message = request.json['message'].lower()
    bot_response = "I hear you."  # Default response

    if "hello" in user_message or "hi" in user_message:
        bot_response = "Hi there! How are you feeling today?"
    elif "sad" in user_message or "upset" in user_message or "down" in user_message:
        bot_response = "I'm sorry to hear that. Would you like to talk about it?"
    elif "happy" in user_message or "good" in user_message or "great" in user_message:
        bot_response = "That's wonderful! What made you happy?"
    elif "angry" in user_message or "mad" in user_message or "frustrated" in user_message:
        bot_response = "I understand you're feeling angry. What's causing you to feel this way?"
    elif "scared" in user_message or "afraid" in user_message or "nervous" in user_message:
        bot_response = "It's okay to feel scared. Can you tell me what you're afraid of?"
    elif "excited" in user_message or "thrilled" in user_message or "enthusiastic" in user_message:
        bot_response = "That's exciting! What are you looking forward to?"
    elif "confused" in user_message or "unsure" in user_message or "puzzled" in user_message:
        bot_response = "I understand you're feeling confused. What's unclear to you?"
    elif "bored" in user_message or "uninterested" in user_message or "dull" in user_message:
        bot_response = "I'm sorry you're feeling bored. Is there anything you'd like to talk about or do?"

    return jsonify({'response': bot_response})

if __name__ == '__main__':
    app.run(debug=True)
