import shutil

def create_output_html_for_user(user_id):
        output_html_filename = f"{user_id}_output.html"
        shutil.copy("output.html", output_html_filename)
        return output_html_filename
  