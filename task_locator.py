import os
from notion_client import Client
from utils import print_properties, get_task_id, get_page_id, update_link_property


notion = Client(auth=os.environ["NOTION_TOKEN"])
response = notion.databases.query(database_id="8ad76183848046f2bb81658f92b3a431")
for result in response["results"]:
    print(f"----------{get_task_id(result, 'ID')}, {get_page_id(result)}----------")
    print_properties(result)
    print()
    update_link_property(result, "Github PR", None)
