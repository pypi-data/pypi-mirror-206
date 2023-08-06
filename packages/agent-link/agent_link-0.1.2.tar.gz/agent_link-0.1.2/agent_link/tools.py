import os
from core.web.web_grab.grabber import capture_grab_internet_output
from core.memory.chat.chat_memory import ChatMemory
from src.result.display_result import display_result
from termcolor import colored
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-web", action="store_true", help="Use web search before generating a response")
    parser.add_argument("-chat", action="store_true", help="Enable continuous chat mode")
    parser.add_argument("--prompt", help="User prompt for the model")
    args = parser.parse_args()

    username = os.environ.get('USER')
    conversation_file_path = f"./bin/user/conversation/{username}.json"
    chat_memory = ChatMemory(conversation_file_path)
    agent_name = "Agent"

    if args.web and args.prompt:
        chat_memory.add_message("User", args.prompt)
        recent_conversation = chat_memory.get_recent_conversation()
        result = capture_grab_internet_output(user_prompt=args.prompt, model="gpt-4", context=recent_conversation)
        display_result(agent_name, result, None)
    elif args.chat:
        print("Entering chat mode. Type 'exit' to quit.")
        while True:
            user_prompt = input(colored("User: ", 'cyan'))
            if user_prompt.lower() == 'exit':
                break

            chat_memory.add_message("User", user_prompt)
            recent_conversation = chat_memory.get_recent_conversation()
            result = capture_grab_internet_output(user_prompt=user_prompt, model="gpt-4", context=recent_conversation)
            chat_memory.add_message(agent_name, result)
            display_result(colored(agent_name, 'magenta'), result, None)

            chat_memory.save_conversation_to_json(conversation_file_path)

        print(f"Conversation saved to {conversation_file_path}")
    else:
        print("Use the '-web' flag with '--prompt' for a single response or the '-chat' flag to enable continuous chat mode.")
