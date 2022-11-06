from notion_client import Client
import requests


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



def __get_task_id__(page, task_id_param="ID"):
    properties = page["properties"]
    return properties[task_id_param]["rich_text"][0]["plain_text"]


def __get_page_id__(page):
    return page["id"]


def find_page_by_id(client, database_id, task_id, task_id_param="ID"):
    database_response = client.databases.query(database_id=database_id)
    for page in database_response["results"]:
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


def create_rich_text(text, annotations={}):
    return {
        'type': 'text', 
        'text': {'content': text, 'link': None}, 
        'annotations': __build_annotions__(annotations), 
        'plain_text': text, 
        'href': None
    }


def create_rich_text_bold(text):
    return create_rich_text(text, {"bold": True})


def create_rich_text_url(text, url, annotations={}):
    return {
        'type': 'text', 
        'text': {'content': text, 'link': {"url": url}}, 
        'annotations': __build_annotions__(annotations), 
        'plain_text': text, 
        'href': url
    }


def post_pr_comment(client: CommentsClient, page, action: str, pr_name, pr_url, author_id, author_url):
    client.post_comment_on_page(__get_page_id__(page), [
        create_rich_text_bold(f"{action.capitalize()} PR "), 
        create_rich_text_url(f"\"{pr_name}\"", pr_url, {"underline": True}), 
        create_rich_text_bold(" by "),
        create_rich_text_url(f"@{author_id}", author_url)
    ])