import os
from notion_client import Client
from notion_utils import find_page_by_id, update_link_property, print_properties, CommentsClient, post_open_pr_comment


notion = Client(auth=os.environ["NOTION_TOKEN"])
notion_comment = CommentsClient(token=os.environ["NOTION_TOKEN"])
page = find_page_by_id(notion, "8ad76183848046f2bb81658f92b3a431", "TASKS-1", "ID")
print_properties(page)
update_link_property(notion, page, "Github PR", "https://github.com/kolesnikov-pasha/github-pr-linker/pull/1")
post_open_pr_comment(
    notion_comment, 
    page, 
    "Updated PR comments functionality", 
    "https://github.com/kolesnikov-pasha/github-pr-linker/pull/1", 
    "kolesnikov-pasha", 
    "https://github.com/kolesnikov-pasha"
)