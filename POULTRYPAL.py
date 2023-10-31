import openai

openai.api_key = "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"

class Poultry_pal:
    def __init__(self):
        self.user_query = ""
        self.conversation = []
    
    def generate_initial_questions(self):
        initial_questions = [
            "Have you tried solving the question yourself?", 
            "Could you provide some more context about the problem?",
        ]  
        return initial_questions    

    def process_user_query(self, user_query):
        self.user_query = user_query
        self.conversation.append(f"User: {user_query}")

    def ask_initial_questions(self):
        initial_questions = self.generate_initial_questions()
        prompt = self.user_query + "\n" + "\n".join(initial_questions)

        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=50  
        )
        app_response = response.choices[0].text.strip()
        self.conversation.append(f"App: {app_response}")
        return app_response

    def user_interaction(self, user_response):
        self.conversation.append(f"User: {user_response}")

    def generate_response(self):
        conversation_history = "\n".join(self.conversation)

        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=conversation_history,
            max_tokens=100  
        )
        app_response = response.choices[0].text.strip()
        self.conversation.append(f"App: {app_response}")
        return app_response

    def start_conversation(self):
        print("Poultry_pal: Hello! How can Poultry_pal assist you today? Type 'exit' to end the conversation.")

        while True:
            user_input = input("You: ")

            if user_input.lower() == 'exit':
                print("Poultry_pal: Goodbye!")
                break

            if not self.user_query:
                self.process_user_query(user_input)
                self.ask_initial_questions()
                print("Poultry_pal: Your response will help me understand how to assist you better.")
            else:
                self.user_interaction(user_input)
                response = self.generate_response()
                print("Poultry_pal:", response)

if __name__ == "__main__":
    app = Poultry_pal()
    app.start_conversation()
