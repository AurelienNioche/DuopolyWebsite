# coding=utf-8
from os import path
from shutil import copy
import json
import requests as rq  # For server requests
from urllib import request, parse  # For client requests


def server_request(**kwargs):

    if not path.exists("parameters/network.json"):
        copy("templates/network.json", "parameters")

    with open("parameters/website.json") as f:
        param = json.load(f)

    website = param["website"]
    page = "server_request.php"

    response = rq.get("{}/{}".format(website, page), params=kwargs)

    print("I called the page '{}' with a GET request (key and values: '{}').".format(page, kwargs))
    print("I received the response: '{}'.".format(response.text))


def client_request(**kwargs):

    if not path.exists("parameters/website.json"):
        copy("templates/website.json", "parameters")

    with open("parameters/website.json") as f:
        param = json.load(f)

    website = param["website"]
    page = "client_request_with_id.php"
    url = "{}/{}".format(website, page)
    print("I will use the url: '{}'.".format(url))

    data = parse.urlencode(kwargs).encode()

    req = request.Request(url, data=data)
    resp = request.urlopen(req)

    print("I called the page '{}' with a post request (key and values: '{}').".format(page, kwargs))
    print("I received the response: '{}'.".format(resp.read()))


def sign_in_request(**kwargs):

    if not path.exists("parameters/website.json"):
        copy("templates/website.json", "parameters")

    with open("parameters/website.json") as f:
        param = json.load(f)

    website = param["website"]
    page = "register.php"
    url = "{}/{}".format(website, page)
    print("I will use the url: '{}'.".format(url))

    data = parse.urlencode(kwargs).encode()

    req = request.Request(url, data=data)
    resp = request.urlopen(req)

    print("I called the page '{}' with a post request (key and values: '{}').".format(page, kwargs))
    print("I received the response: '{}'.".format(resp.read()))


def empty_tables():

    server_request(demand_type="empty_tables")


def fill_participants_table():

    participants = ["JEANMICHEL", "TAMERE"]

    roles = ["firm", "firm"]

    names = json.dumps(participants)
    game_ids = json.dumps(list(range(len(participants))))
    roles = json.dumps(roles)

    server_request(
        demand_type="writing",
        table="participants",
        gameIds=game_ids,
        names=names,
        roles=roles)


def address_a_demand_to_server():

    client_request(
        demand_type="request",
        gameId=0,
        request="This is a fake request."
    )


def main():

    # empty_tables()
    # client_request(
    #     demand_type="participate",
    #     gameId="none",
    #     request="none",
    #     userName="tamere"
    # )
    sign_in_request(
        demand_type="register",
        Email="nioche.aurelien@gmail.com",
        Age="31",
        MtId="tamere",
        Nationality="French"

    )


if __name__ == "__main__":

    main()
