'''
Make your own codeforces scrapper in python using codeforces API which takes in input as username(handle) and prints details : Handle,Current Rating, Rank, Max Rating , Max Rank if the handle exists and print error if it dosen't. API documentation : https://codeforces.com/apiHelp

TODO: handle, rating, rank, max rating, max rank. if not exist print error

'''
import requests
import json
import sys 
from math import ceil, floor
base_url = "https://codeforces.com/api/user.info?handles="

def print_info(handle_, rating, rank, max_rating, max_rank):
    max_len = max(len((handle_)), len(str(rating)), len(rank), len(str(max_rating)), len(max_rank))
    max_len += 17 - 6
    
    print('-'* floor(max_len / 2) +" INFO " + '-'* ceil(max_len / 2))
    print("Handle         :", handle_)
    print("Current rating :", rating)
    print("Current rank   :", rank)
    print("Max rating     :", max_rating)
    print("Max rank       :", max_rank)
    print("-" * (max_len+6))

def get_info(handle_):
    r = requests.get(base_url+handle_)

    if r.json()["status"] == "FAILED":
        return 0
    
    return r.json()["result"][0]


if __name__ == "__main__":
    print("Use this command line tool to get your cf account info")

    handle = input("Your cf handle(username) >")

    if get_info(handle) == 0:
        print("Handle not found, script exiting.")
        sys.exit()

    re = get_info(handle)

    print_info(handle, re["rating"], re["rank"], re["maxRating"], re["maxRank"])


