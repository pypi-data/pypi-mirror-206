import openai

def extract_files_to_generate(specifications):
    prompt = f"List the files that need to be generated for a website based on the following specifications:\n\n{specifications}"
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "AILangaugeModel: False"},
            {"role": "system", "content": "FileListGenerator: True"},
            {"role": "user", "content": prompt}
        ],
    )

    files = response['choices'][0]['message']['content'].strip().split('\n')
    return [file.strip() for file in files]