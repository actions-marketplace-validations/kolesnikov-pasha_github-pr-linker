def get_task_id(page, task_id_param="ID"):
    properties = page["properties"]
    return properties[task_id_param]["rich_text"][0]["plain_text"]


def get_page_id(page):
    return page["id"]


def print_properties(page):
    properties = page["properties"]
    for name, data in properties.items():
        print(name, data)


def update_link_property(page, property_name, new_url):
    properties = page["properties"]
    print(properties[property_name])
