import json
file = open('farmers-protest-tweets-2021-03-5.json')
data = json.load(file)

def funcion(info):
    maximos = []
    for persona in data:
        print(persona)
        #print(persona["retweetCount"])

funcion("info")