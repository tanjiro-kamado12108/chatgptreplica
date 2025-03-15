from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/get_response', methods=['POST'])
def get_response():
    user_message = request.json['message'].lower()
    bot_response = "I hear you."  # Default response

    if "hello" in user_message or "hi" in user_message:
        bot_response = "Hi there! How are you feeling today? <br><a href='https://www.mindful.org/how-to-practice-mindfulness/' target='_blank'>Learn about mindfulness</a>"
    elif "sad" in user_message or "upset" in user_message or "down" in user_message:
        bot_response = "I'm sorry to hear that. Would you like to talk about it? <br><a href='https://www.childline.org.uk/' target='_blank'>Get help from Childline</a>"
    elif "happy" in user_message or "good" in user_message or "great" in user_message:
        bot_response = "That's wonderful! What made you happy? <br><a href='https://www.actionforhappiness.org/10-keys-to-happier-living' target='_blank'>Learn about happier living</a>"
    elif "angry" in user_message or "mad" in user_message or "frustrated" in user_message:
        bot_response = "I understand you're feeling angry. What's causing you to feel this way? <br><a href='https://www.apa.org/topics/anger/control' target='_blank'>Learn to control anger</a>"
    elif "scared" in user_message or "afraid" in user_message or "nervous" in user_message:
        bot_response = "It's okay to feel scared. Can you tell me what you're afraid of? <br><a href='https://kidshealth.org/en/kids/anxiety.html' target='_blank'>Learn about anxiety</a>"
    elif "excited" in user_message or "thrilled" in user_message or "enthusiastic" in user_message:
        bot_response = "That's exciting! What are you looking forward to? <br><a href='https://www.wikihow.com/Manage-Excitement' target='_blank'>Learn to manage excitement</a>"
    elif "confused" in user_message or "unsure" in user_message or "puzzled" in user_message:
        bot_response = "I understand you're feeling confused. What's unclear to you? <br><a href='https://www.psychologytoday.com/us/blog/in-practice/201502/how-deal-feeling-confused' target='_blank'>Learn to deal with confusion</a>"
    elif "bored" in user_message or "uninterested" in user_message or "dull" in user_message:
        bot_response = "I'm sorry you're feeling bored. Is there anything you'd like to talk about or do? <br><a href='https://www.wikihow.com/Overcome-Boredom' target='_blank'>Learn to overcome boredom</a>"

    return jsonify({'response': bot_response})

if __name__ == '__main__':
    app.run(debug=True)
