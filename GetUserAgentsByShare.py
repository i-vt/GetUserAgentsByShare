import requests
import datetime
import json
import random
import os
import re
import argparse
import sys
# Get string of current time as a timestamp: "yyyymmddHHMMSS"
def timestamp() -> str:
    current = datetime.datetime.now()
    return current.strftime("%Y%m%d%H%M%S")

def fetch_popular_useragents():
    url = 'https://www.useragents.me/'
    req = requests.get(url)
    text = str(req.content)

    useragents = []
    for i in text.split(">"):
        if not ("useragents list conveniently in JSON format" in i or '[{"' in i):
            continue 
        if "Get the most common " in i:
            i = (i.replace("Get the most common ", "")
                   .replace(" useragents list conveniently in JSON format", ""))
        useragents.append(i.split("<")[0])
    now = timestamp()

    filename = ""
    for i in useragents:
        if len(i) < 15:
            filename = i
        else:
            with open(f'{filename}_{now}.json', 'w') as f:
                f.write(i)

def find_latest_json(keystring, directory='.'):
    pattern = re.compile(rf'^{re.escape(keystring)}_(\d{{14}})\.json$')
    latest_file = None
    latest_timestamp = ''

    for filename in os.listdir(directory):
        match = pattern.match(filename)
        if match:
            timestamp = match.group(1)
            if timestamp > latest_timestamp:
                latest_timestamp = timestamp
                latest_file = filename

    return latest_file

def get_latest_filename_contents(keystring):
    directory = '.'
    latest = find_latest_json(keystring, directory)
    if not latest:
        raise FileNotFoundError(f"No JSON file found with keystring '{keystring}'")
    with open(latest, "r") as file:
        latest_json = file.read()
    return latest_json

def get_user_agent(passed_json):
    user_agents = [entry["ua"] for entry in passed_json]
    weights = [entry["pct"] for entry in passed_json]
    return random.choices(user_agents, weights=weights, k=1)[0]

def main():
    parser = argparse.ArgumentParser(description="User Agent Utility")
    parser.add_argument('--update', action='store_true', help='Fetch and save latest user agents (use this when running for first time)')
    parser.add_argument('--fetch', metavar='KEY', help='Get a random user agent from the latest file for given key (mobile or desktop)')
    args = parser.parse_args()
    if not any(vars(args).values()):
        parser.print_help()
        exit(1) 
    if args.update:
        fetch_popular_useragents()

    if args.fetch:
        try:
            entries = json.loads(get_latest_filename_contents(args.fetch))
            selected_ua = get_user_agent(entries)
            print(selected_ua)
        except Exception as e:
            print(f"Error fetching user agent: {e}")

if __name__ == "__main__":
    main()
