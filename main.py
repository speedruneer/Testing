import requests

def get_github_file_content(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text  # Returns the raw content as a string
    else:
        raise Exception(f"Error fetching the file: {response.status_code}")
