import json


def load_companies():

    with open("companies.json", "r") as file:
        return json.load(file)