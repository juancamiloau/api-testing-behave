from utilities.configurations import *

def before_scenario(context, scenario):
    context.url = getConfig()['API']['endpoint']
    context.headers = {"Content-Type":"application/json"
                       ,"accept":"application/json"}