import requests
from templates.body_templates import *

@Given(u'I have created a new user')
@when(u'I create the user')
def step_impl(context):
    url = context.url + "/user"
    context.body =  createUserBody()
    response = requests.post(url, json=context.body ,headers= context.headers)
    context.response = response
    context.body["id"] = int(context.response.json()["message"])

@when(u'I modify the user')
def step_impl(context):
    url = context.url +"/user/" + context.body["username"]
    newBody = context.body
    newBody["firstName"] = "Nuevo juan"
    newBody["lastName"] = "Nuevo Alvarez"
    newBody["id"] = int(context.response.json()["message"])
    context.body = newBody
    response = requests.put(url, json=newBody ,headers= context.headers)
    context.response = response
    print(response.json())

@then(u'I should see 200 status code')
def step_impl(context):
    assert context.response.status_code == 200


@then(u'I should see the data when I get the user')
def step_impl(context):
    getResponse = requests.get(context.url +"/user/" + context.body["username"], headers= context.headers)
    assert getResponse.status_code == 200
    getJson = getResponse.json()
    assert getJson == context.body

@when(u'I delete the user')
def step_impl(context):
    url = context.url +"/user/" + context.body["username"]
    context.response = requests.delete(url, headers= context.headers)


@then(u'I should get user not found when I get it')
def step_impl(context):
    getResponse = requests.get(context.url +"/user/" + context.body["username"])
    assert getResponse.status_code == 404