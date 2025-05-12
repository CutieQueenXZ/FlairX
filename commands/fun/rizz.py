import requests

def get_rizz():
    response = requests.get("https://rizz-api.vercel.app/")
    if response.status_code == 200:
        return response.json().get("pickup", "Couldn't fetch any rizz right now.")
    else:
        return "Couldn't fetch any rizz right now."
