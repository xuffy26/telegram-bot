from flask import Flask, request
import requests

app = Flask(__name__)

BOT_TOKEN = '8105997635:AAEaHWnIvc-eiRMF33momXTDQ8dSt2N7g6M'
TELEGRAM_API = f"https://api.telegram.org/bot{BOT_TOKEN}"

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json

    if 'message' in data:
        chat_id = data['message']['chat']['id']
        username = data['message']['from'].get('username', 'NoUsername')
        first_name = data['message']['from'].get('first_name', '')
        last_name = data['message']['from'].get('last_name', '')
        text = data['message'].get('text', '')

        if text.startswith("/start"):
            referral_code = text[7:].strip() if len(text) > 6 else None

            # 👉 Store chat_id, username, referral_code, etc. to DB (or print for now)
            print(f"New user: {chat_id}, @{username}, referral: {referral_code}")

            # ✅ Send welcome message
            message = f"Hi {first_name}! 🎉 You're now subscribed to our Telegram updates!"
            requests.post(f"{TELEGRAM_API}/sendMessage", json={
                "chat_id": chat_id,
                "text": message
            })

    return "ok"

if __name__ == '__main__':
    app.run(port=5000)
