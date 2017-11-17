# coding=utf-8
import sys
from os import path, mkdir
from shutil import copy
import json
from ftplib import FTP


def main(f_name="client_request.php"):

    try:

        if not path.exists("parameters/network.json"):
            if not path.exists("parameters"):
                mkdir(parameters)
            copy("templates/network.json", "parameters/network.json")

        with open("parameters/network.json") as f:

            param = json.load(f)

        host = param["host"]
        user = param["user"]
        password = param["password"]

        # File to send
        f = open("php/{}".format(f_name), 'rb')

        ftp = FTP(host, user, password)

        ftp.storbinary('STOR ' + f_name, f)
        ftp.close()

        f.close()

        print("File '{}' pushed on the server.".format(f_name))

    except Exception as e:
        print("I encountered error '{}'. I couldn't push the desired file. \n"
              "Check the network parameters in 'parameters/network.json'.".format(e))


if __name__ == "__main__":

    try:
        file_to_push = sys.argv[1]
        main(file_to_push)

    except IndexError:
        raise Exception("You should indicate which file you want to push (e.g. 'python push.py script.php').")
