# coding=utf-8
from os import path
from shutil import copy
import json
from urllib import request, parse


def main():

    if not path.exists("parameters/network.json"):
        copy("templates/network.json", "parameters")

    with open("parameters/website.json") as f:
        param = json.load(f)

    website = param["website"]
    page = "client_request.php"

    data_dic = dict()
    data_dic["demand_type"] = "request"
    data_dic["gameId"] = "JEANPIERRE"
    data_dic["request"] = "this is my request!"
    data = parse.urlencode(data_dic).encode()

    req = request.Request("{}/{}".format(website, page), data=data)
    resp = request.urlopen(req)

    print("I called the page '{}' with a post request (key and values: '{}').".format(page, data_dic))
    print("I received the response: '{}'.".format(resp.read()))


if __name__ == "__main__":

    main()