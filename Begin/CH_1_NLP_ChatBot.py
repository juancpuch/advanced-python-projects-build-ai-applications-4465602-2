

# Define intents and their corresponding responses based on keywords

    # Convert the message to lowercase for consistent keyword matching
  
    # Check if the message contains any keywords associated with defined intents
    
    
    # Analyze the sentiment of the message using TextBlob

    
    # Return a response based on the sentiment score
   
    # Greet the user and prompt for input
   
    # Continuously prompt the user for input until they choose to exit
   
    # Thank the user for chatting when they exit
from textblob import TextBlob

class ChatBot:
    def __init__(self):
        self.intents = {
            "hours": {
                "keywords": ["hour", "open", "close"],
                "response": "We are open form 9 AM to 5 PM, Monday to Friday."
            },
            "return": {
                "keywords": ["refund", "money back", "return"],
                "response": "I'd be happy to help you process your return. Let me transfer you to a live agent."
            }
        }

    def get_respone(self, message):
        message = message.lower()
        for intent_data in self.intents.values():
            if any(word in message for word in intent_data["keywords"]):
                return intent_data["response"]
        sentiment = TextBlob(message).sentiment.polarity
        return ("That's great to hear!" if sentiment > 0 else
                "I'm so sorry to hear that. How can I help?" if sentiment < 0 else
                "I see. Can you tell me more about that?")
    def chat(self):
        print("ChatBot: Hi, how can I help you today?")
        while (user_message := input("You: ").strip().lower()) not in ['exit', 'quit', 'bye']:
            print(f"\nChatBot: {self.get_respone(user_message)}")
        print("ChatBot: Thank you for chatting. Have a great day!")

if __name__ == "__main__":
    ChatBot().chat()  # Start the chat when the script is executed
