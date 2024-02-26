import json
import requests
import base64

def read_json_files(file):
    with open(file, "r") as f:
        json_list = json.load(f)
    return json_list

json_list = read_json_files("out_pull_req.json")

print("#Pull Requests: " + str(len(json_list)))
print()

print("Keys in the dictionary:")
print(json_list[0].keys())
print()
print()

""" print("Values in the dictionary")
print("Value of pull_request:\n" + str(json_list[0]["pull_request"]))
print()
print("Value of repository:\n" + str(json_list[0]["repository"]))
print() """

def extract_repo_info(data):
    repo = data["repository"]["name"]
    owner = data["repository"]["owner"]["login"]
    pull_number = data["number"]
    return owner, repo, pull_number

def get_changed_files(owner, repo, pull_number):
    url = f"https://api.github.com/repos/{owner}/{repo}/pulls/{pull_number}/files"
    response = requests.get(url)
    files = response.json()
    return [file["filename"] for file in files]

owner, repo, pull_number = extract_repo_info(json_list[0])
changed_files = get_changed_files(owner, repo, pull_number)
print(f"Owner: {owner}, Repo: {repo}, Pull Number: {pull_number}")
print()

print("Changed Files:")
print(changed_files)
print()

def get_file_content(owner, repo, path):
    url = f"https://api.github.com/repos/{owner}/{repo}/contents/{path}"
    response = requests.get(url)
    file = response.json()
    content = base64.b64decode(file["content"]).decode("utf-8")
    return content

print("Content of the changed files:")
for path in changed_files:
    print(f"Content of {path}:")
    content = get_file_content(owner, repo, path)
    print(content)
print()