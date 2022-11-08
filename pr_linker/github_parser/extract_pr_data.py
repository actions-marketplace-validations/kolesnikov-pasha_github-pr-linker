import json
from entities import entities

def get_pr_data(path):
    with open(path, "r") as f:
        data = "".join(f.readlines())
        return json.loads(data)


def get_action(pr_data):
    action = pr_data["action"]
    if action == "closed" and pr_data["pull_request"]["merged"]:
        action = "merged"
    return entities.EventAction(action)


def get_author_url(pr_data):
    return pr_data["sender"]["html_url"]


def get_author_login(pr_data):
    return pr_data["sender"]["login"]


def get_pr_url(pr_data):
    return pr_data["pull_request"]["html_url"]


def get_pr_name(pr_data):
    return pr_data["pull_request"]["title"]


def get_source_branch(pr_data):
    return pr_data["pull_request"]["head"]["ref"]