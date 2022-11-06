import os
from notion_client import Client
from notion_utils import find_page_by_id, update_link_property, print_properties, CommentsClient, post_pr_comment
import extract_pr_data
import re
import sys


notion_token = sys.argv[1]
database_id = sys.argv[2]
task_id_prefix = sys.argv[3]
event_context = sys.argv[4] if len(sys.argv) > 4 else None

notion = Client(auth=notion_token)
notion_comment = CommentsClient(token=notion_token)
pr_data = extract_pr_data.get_pr_data(event_context)
branch = extract_pr_data.get_source_branch(pr_data)
task_id_pattern = fr"{task_id_prefix}-\d+"
task_id = None
for part in branch.split("/"):
    if re.match(task_id_pattern, part):
        task_id = part
        break
page = find_page_by_id(notion, database_id, task_id, "ID")
print_properties(page)
pr_url = extract_pr_data.get_pr_url(pr_data)
update_link_property(notion, page, "Github PR", pr_url)
post_pr_comment(
    notion_comment, 
    page, 
    extract_pr_data.get_action(pr_data),
    extract_pr_data.get_pr_name(pr_data), 
    pr_url, 
    extract_pr_data.get_author_login(pr_data), 
    extract_pr_data.get_author_url(pr_data)
)