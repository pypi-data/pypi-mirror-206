import openai
import json

def get_file_names_from_api(specifications, model):
    prompt = f"Given the following project specifications, provide a list of Python file names in JSON format that should be generated for this project:\n\n{specifications}"
    response = openai.ChatCompletion.create(
        model=model,
        messages=[
            {"role": "user", "content": prompt}
        ],
    )

    file_names_json = response['choices'][0]['message']['content'].strip()
    file_names = json.loads(file_names_json)
    return file_names
