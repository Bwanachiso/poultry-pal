from flask import Flask, request, jsonify
from POULTRYPAL import Poultry_pal  

app = Flask(__name__)

# Initialize the chatbot
chatbot = Poultry_pal()

@app.route('/api/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_message = data["message"]
    
    if user_message.lower() == 'exit':
        response = "Goodbye!"
    else:
        response = chatbot.generate_response(user_message)

    response_data = {"message": response}
    return jsonify(response_data)

if __name__ == '__main__':
    app.run(debug=True)
