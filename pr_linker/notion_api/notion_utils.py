from notion_client import Client
import requests
from entities import entities
import json


class CommentsClient():
    def __init__(self, token):
        self.base_url = "https://api.notion.com/v1/comments"
        self.headers = {
            "accept": "application/json",
            "Notion-Version": "2022-06-28",
            "content-type": "application/json",
            "authorization": f"Bearer {token}"
        }

    def post_comment_on_page(self, page_id, rich_text):
        print(requests.post(self.base_url, headers=self.headers, json={
            "parent": {"page_id": page_id},
            "rich_text": rich_text
        }).content)


def get_database(client, database_id):
    return client.databases.query(database_id=database_id)


def __get_task_id__(page, task_id_param="ID"):
    properties = page["properties"]
    return properties[task_id_param]["rich_text"][0]["plain_text"]


def __get_page_id__(page):
    return page["id"]


def __iterate_through_database_pages__(database):
    for page in database["results"]:
        yield page


def find_page_by_id(database, task_id, task_id_param="ID"):
    for page in __iterate_through_database_pages__(database):
        if __get_task_id__(page, task_id_param) == task_id:
            return page


def print_properties(page):
    properties = page["properties"]
    for name, data in properties.items():
        print(name, data)


def update_link_property(client: Client, page, property_name, new_url):
    client.pages.update(
        page_id=__get_page_id__(page), 
        properties={property_name: {"url": new_url}}
    )


def __build_annotions__(annotations: dict):
    return {
        'bold': annotations.get("bold", False), 
        'italic': annotations.get("italic", False), 
        'strikethrough': annotations.get("strikethrough", False), 
        'underline': annotations.get("underline", False), 
        'code': annotations.get("code", False), 
        'color': annotations.get("color", 'default')
    }


def __create_rich_text__(text: entities.Text):
    return {
        'type': 'text', 
        'text': {'content': text.text, 'link': None if text.href is None else {"url": text.href}}, 
        'annotations': __build_annotions__({"bold": text.is_bold}), 
        'plain_text': text.text, 
        'href': text.href
    }


def __build_pr_comment__(message):
    return list(map(__create_rich_text__, message))


def post_pr_comment(client: CommentsClient, page, message):
    client.post_comment_on_page(
        __get_page_id__(page), 
        __build_pr_comment__(message)
    )