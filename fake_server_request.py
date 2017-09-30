# coding=utf-8
from os import path
from shutil import copy
import json
import requests as rq


def get_args_for_fake_participants_filling():

    participants = ["JEANMICHEL", "TAMERE"]

    roles = ["firm", "firm"]

    names = json.dumps(participants)
    game_ids = json.dumps(list(range(len(participants))))
    roles = json.dumps(roles)

    args = {
        "demand_type": "writing",
        "table": "participants",
        "gameIds": game_ids,
        "names": names,
        "roles": roles
    }

    return args


def get_args_for_erasing_tables():

    args = {
        "demand_type": "empty_tables"
    }

    return args


def main():

    if not path.exists("parameters/network.json"):
        copy("templates/network.json", "parameters")

    with open("parameters/website.json") as f:
        param = json.load(f)

    website = param["website"]
    page = "server_request.php"

    data = get_args_for_erasing_tables()  # Change this line for testing other things...

    response = rq.get("{}/{}".format(website, page), params=data)

    print("I called the page '{}' with a GET request (key and values: '{}').".format(page, data))
    print("I received the response: '{}'.".format(response.text))


if __name__ == "__main__":

    main()