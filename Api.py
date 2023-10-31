from flask import Flask, request, jsonify
from POULTRYPAL import PoultryPal
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

chatbots = {}  # A dictionary to store chatbots for different user sessions

@app.route('/api/chat/<session_id>', methods=['POST'])
def chat(session_id):
    data = request.get_json()
    user_message = data["message"]

    if session_id not in chatbots:
        chatbots[session_id] = PoultryPal()

    chatbot = chatbots[session_id]

    if user_message.lower() == 'exit':
        response = "Goodbye!"
        del chatbots[session_id]  # Delete the chatbot for this session
    else:
        response = chatbot.generate_response(user_message)

    response_data = {"message": response}
    return jsonify(response_data)

if __name__ == '__main__':
    app.run(debug=True)