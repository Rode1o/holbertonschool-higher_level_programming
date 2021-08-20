#!/usr/bin/python3
"""Python script that fetches https://intranet.hbtn.io/status"""
if __name__ == "__main__":
    import urllib.request as request
    from sys import argv
    url = request.Request(argv[1])
    with request.urlopen(url) as page:
        print(page.headers.get('X-Request-Id'))
