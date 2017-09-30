# coding=utf-8
from os import path
from shutil import copy
import json
from urllib import request, parse


def main():

    if not path.exists("parameters/website.json"):
        copy("templates/website.json", "parameters")

    with open("parameters/website.json") as f:
        param = json.load(f)

    website = param["website"]
    page = "client_request.php"
    url = "{}/{}".format(website, page)
    print("I will use the url: '{}'.".format(url))

    data_dic = dict()
    data_dic["demand_type"] = "request"
    data_dic["gameId"] = 0
    data_dic["request"] = "This is a fake request."
    data = parse.urlencode(data_dic).encode()

    req = request.Request(url, data=data)
    resp = request.urlopen(req)

    print("I called the page '{}' with a post request (key and values: '{}').".format(page, data_dic))
    print("I received the response: '{}'.".format(resp.read()))


if __name__ == "__main__":

    main()
