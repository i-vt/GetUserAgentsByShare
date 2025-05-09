# GetUserAgentsByShare

This utility fetches and stores the most common user-agent strings in JSON format from the web. It can also retrieve a randomly selected user-agent based on weighted usage percentages from the most recent data file.

## Help Menu

```
# python3 GetUserAgentsByShare.py
usage: GetUserAgentsByShare.py [-h] [--update] [--fetch KEY]

User Agent Utility

options:
  -h, --help   show this help message and exit
  --update     Fetch and save latest user agents (use this when running for first time)
  --fetch KEY  Get a random user agent from the latest file for given key (mobile or desktop)

```
## Examples: 
### Mobile user agent
```
# python3 GetUserAgentsByShare.py --fetch mobile
Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/27.0 Chrome/125.0.0.0 Mobile Safari/537.3
```
### Desktop user agent
```
# python3 GetUserAgentsByShare.py --update --fetch desktop
Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.3
```
### Bash usage:
```
wget iplocation.net -U "$(python3 ./GetUserAgentsByShare.py --fetch desktop)"
```
