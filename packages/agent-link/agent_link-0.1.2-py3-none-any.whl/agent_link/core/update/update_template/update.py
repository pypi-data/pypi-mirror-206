import os
import datetime

LAST_UPDATE_FILE = "last_update.txt"
TEMPLATE_DIR = "template"
TEMPLATE_ZIP_FILE = "template.zip"

def should_update_template():
    if not os.path.exists(LAST_UPDATE_FILE):
        return True

    with open(LAST_UPDATE_FILE, "r") as f:
        last_update_str = f.read().strip()
        last_update = datetime.datetime.strptime(last_update_str, "%Y-%m-%d")

    now = datetime.datetime.now()
    days_since_last_update = (now - last_update).days

    return days_since_last_update >= 7
