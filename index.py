import redis
import argparse
import subprocess
import sys
import json

def main(host: str, user: str, creds: str, name: str, text: str): 
    link = "redis://" + user + ":" + creds + "@" + host
    subprocess.call("redis-cli -u " + link + " set " + name + " " + text, shell=True)

    target = subprocess.call("redis-cli -u " + link + " get " + name,  shell=True)
    return target

args = argparse.ArgumentParser(prog="pyred", description="pyred is a python redis cli tool that adds data to amy redis server")
args.add_argument("-t", "--target", help="enter the redis server host e.g (ip:port) like 127.0.0.1:6379")
args.add_argument("-u", "--user", help="user is the username of the redis server like default")
args.add_argument("-c", "--cred", help="creds is the password of the redis server like default")
args.add_argument("-n", "--name", help="name is the key to the value of the data you enter")
args.add_argument("-d", "--data", help="data is the value of the data you want to store")

parser = args.parse_args()
print(main(parser.target, parser.user, parser.cred, parser.name, parser.data))