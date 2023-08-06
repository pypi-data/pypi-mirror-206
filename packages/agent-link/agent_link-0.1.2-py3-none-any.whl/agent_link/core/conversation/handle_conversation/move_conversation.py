import os
import datetime

def move_old_conversation(username, chat_memory):
    folder_name = f"./bin/user/conversation/old/{username}"
    os.makedirs(folder_name, exist_ok=True)

    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    json_file_name = f"{timestamp}.json"
    json_file_path = os.path.join(folder_name, json_file_name)

    chat_memory.save_conversation_to_json(json_file_path)
    chat_memory.clear_conversation()

    print(f"Old conversation moved to {json_file_path}")