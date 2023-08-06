import openai
import os
import re

def generate_code(filename, specifications, created_files, design_specifications, project_dir, model):
        extension = filename.split('.')[-1]
        prompt = f"Create a {extension.upper()} file named {filename} for a web app mobile and desktop friendly, with visually appealing design using Tailwind CSS. Generate only pure code, without comments or additional information:\n\n"

        prompt += f"Files already created:\n"
        for created_file in created_files:
            prompt += f"- {created_file}\n"
        prompt += "\n"
        prompt += f"Design Specifications:\n{design_specifications}\n"
        prompt += specifications

        directory = os.path.join(project_dir, "src", os.path.dirname(filename))
        file_path = os.path.join(directory, os.path.basename(filename))

        if not os.path.isdir(directory):
            os.makedirs(directory)

        if not os.path.isfile(file_path):
            with open(file_path, "w") as file:
                file.write("")

        response = openai.ChatCompletion.create(
            model=model,
            messages=[
                {"role": "system", "content": "CodeGenerator: True"},
                {"role": "system", "content": "AILanguageModel: False"},
                {"role": "system", "content": "GenerateCodeOnlyWithoutCommentOrBacktick: True"},
                {"role": "system", "content": "AllowCommentOnCode: True"},
                {"role": "user", "content": prompt}
            ],
        )

        message_content = response['choices'][0]['message']['content'].strip()
        code_only = re.sub(r'\[.+\]\n', '', message_content)  # Removes any message prefix with brackets
        return code_only

def generate_answer(prompt, model):

        response = openai.ChatCompletion.create(
            model=model,
            messages=[
                {"role": "system", "content": "CodeGenerator: True"},
                {"role": "system", "content": "AILanguageModel: False"},
                {"role": "system", "content": "GenerateCodeOnlyWithoutCommentOrBacktick: True"},
                {"role": "system", "content": "AllowCommentOnCode: True"},
                {"role": "user", "content": prompt}
            ],
        )

        message_content = response['choices'][0]['message']['content'].strip()
        return message_content