#!/usr/bin/python3
"""Python script that fetches https://intranet.hbtn.io/status"""
if __name__ == "__main__":
    url = 'https://api.github.com/user'
    response = requests.get(url, auth=(sys.argv[1], sys.argv[2]))
    try:
        print(response.json().get("id"))
    except ValueError:
        print("Not a valid JSON")~
