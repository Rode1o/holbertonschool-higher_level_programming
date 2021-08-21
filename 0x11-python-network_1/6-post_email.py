#!/usr/bin/python3
"""Python script that fetches
https://intranet.hbtn.io/status"""

if __name__ == "__main__":
    import requests
    import sys
    response = requests.post(sys.argv[1], {"email": sys.argv[2]}).text
    print(response)
