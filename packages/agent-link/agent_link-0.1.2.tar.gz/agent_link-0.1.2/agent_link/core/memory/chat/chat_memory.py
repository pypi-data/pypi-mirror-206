import os
import json

class ChatMemory:
    def __init__(self, conversation_file_path=None):
        if conversation_file_path and os.path.exists(conversation_file_path):
            with open(conversation_file_path, 'r') as f:
                self.conversation = json.load(f)
        else:
            self.conversation = []

    def add_message(self, sender, message):
        self.conversation.append({"sender": sender, "message": message})

    def get_recent_conversation(self, n=5):
        return self.conversation[-n:]

    def save_conversation_to_json(self, file_path):
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, 'w') as f:
            json.dump(self.conversation, f)