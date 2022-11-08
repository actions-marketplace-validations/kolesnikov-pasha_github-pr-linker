from github_parser.extract_pr_data import get_author_login, get_author_url, get_pr_data
from entities.entities import EventAction

cases_author = [
    (get_pr_data("pr_linker/github_parser/tests/example_github_event.json"), "kolesnikov-pasha")
]
cases_author_url = [
    (get_pr_data("pr_linker/github_parser/tests/example_github_event.json"), "https://github.com/kolesnikov-pasha")
]

for case in cases_author:
    actual_result = get_author_login(case[0])
    assert actual_result == case[1], f"Test case input = {case[0]}, expected output = {case[1]}, actual output = {actual_result}"

for case in cases_author_url:
    actual_result = get_author_url(case[0])
    assert actual_result == case[1], f"Test case input = {case[0]}, expected output = {case[1]}, actual output = {actual_result}"