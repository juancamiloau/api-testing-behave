import random
import string
from string import Template
import json

def createUserBody():
    with open('templates/create_user.json', 'r') as file:
        template_content = file.read()

    random_value = ''.join(random.choices(string.ascii_lowercase + string.digits, k=6))
    template = Template(template_content)
    body = json.loads(template.substitute(random = random_value))
    return body