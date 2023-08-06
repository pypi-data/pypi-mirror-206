import sys
import json
import io
from contextlib import redirect_stdout
from ..search_google_direct.grab import grab_internet

def capture_grab_internet_output(*args, context=None, **kwargs):
    original_stdout = sys.stdout
    sys.stdout = io.StringIO()

    user_prompt = kwargs.get("user_prompt", "")
    if context:
        formatted_context = " ".join([f"{entry['sender']}: {entry['message']}" for entry in context])
        user_prompt = f"{formatted_context}\n{user_prompt}"
        kwargs["user_prompt"] = user_prompt

    with redirect_stdout(sys.stdout):
        grab_internet(*args, **kwargs)

    output = sys.stdout.getvalue()
    sys.stdout = original_stdout

    output_json = json.loads(output)
    content = output_json['content'].strip()

    if content.startswith("Agent:"):
        content = content.split("Agent:", 1)[1].strip()

    return content


