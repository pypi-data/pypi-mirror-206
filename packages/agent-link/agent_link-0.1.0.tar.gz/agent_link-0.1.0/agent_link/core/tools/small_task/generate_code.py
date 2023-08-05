import openai

def generate_code(filename, specifications, model):
    prompt = f"Create a file named {filename} and create the whole as described in the following specifications. Generate only pure code, without comments or additional information:\n\n"

    prompt += specifications

    response = openai.ChatCompletion.create(
        model= model,
        messages=[
            {"role": "user", "content": prompt}
        ],
    )

    return response['choices'][0]['message']['content'].strip()

def generate_code_with_command(filename, specifications, model, command):
    prompt = f"Create a file named {filename} {command} as described in the following specifications. Generate only pure code, without comments or additional information:\n\n"

    prompt += specifications

    response = openai.ChatCompletion.create(
        model= model,
        messages=[
            {"role": "user", "content": prompt}
        ],
    )

    return response['choices'][0]['message']['content'].strip()