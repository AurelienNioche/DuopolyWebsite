# coding=utf-8
from os import path
import json
from shutil import copy
from urllib import parse, request

import push


def send_request(**kwargs):

    assert "demandType" in kwargs and "userName" in kwargs and "message" in kwargs, \
        "A request to the server should contains a 'demandType', a 'userName' and a 'message'."

    if not path.exists("parameters/website.json"):
        copy("templates/website.json", "parameters")

    with open("parameters/website.json") as f:
        param = json.load(f)

    website = param["website"]
    page = "messenger.php"
    url = "{}/{}".format(website, page)
    print("I will use the url: '{}'.".format(url))

    data = parse.urlencode(kwargs).encode()

    req = request.Request(url, data=data)
    enc_resp = request.urlopen(req)

    response = enc_resp.read().decode()

    print("I called the page '{}' with a post request (args: '{}').".format(page, data))
    print("I received the response: '{}'.".format(response))

    return response


def example_server_send_message():

    print("I send a request for sending a message as the server.")

    send_request(
        demandType="serverSpeaks",
        userName="Michael",
        message="Hello Michael!"
    )


def example_user_send_message():

    print("I send a request for sending a message as a user.")

    send_request(
        demandType="clientSpeaks",
        userName="Michael",
        message="Hello, my name is Michael!"
    )


def example_server_receives_message():

    print("I send a request for receiving the messages intended to server.")

    response = send_request(
        demandType="serverHears",
        userName="none",
        message="none"
    )

    if "reply" in response:
        args = [i for i in response.split("/") if i]
        n_messages = int(args[1])
        print("I received {} new message(s).".format(n_messages))
        if n_messages:
            for arg in args[2:]:

                sep_args = arg.split("<>")

                user_name, message = sep_args[0], sep_args[1]

                print("I send confirmation for message '{}'.".format(arg))
                send_request(
                    demandType="serverReceiptConfirmation",
                    userName=user_name,
                    message=message
                )


def example_user_receives_message():

    print("I send a request for receiving the messages intended to user.")

    user_name = "Michael"

    response = send_request(
        demandType="clientHears",
        userName=user_name,
        message="none"
    )

    if "reply" in response:
        args = [i for i in response.split("/") if i]
        n_messages = int(args[1])
        print("I received {} new message(s).".format(n_messages))
        if n_messages:
            for arg in args[2:]:
                print("I send confirmation for message '{}'.".format(arg))
                send_request(
                    demandType="clientReceiptConfirmation",
                    userName=user_name,
                    message=arg
                )


def empty_tables():

    print("I send a request for erasing tables.")

    send_request(
        demandType="emptyTables",
        userName="none",
        message="none"
    )


def main():

    push.main("messenger.php")
    print()
    empty_tables()
    print()
    example_user_send_message()
    print()
    example_server_receives_message()
    print()
    example_server_send_message()
    print()
    example_user_receives_message()


if __name__ == "__main__":

    main()
