import sys
import requests

def main():
    if sys.argv[1]:
        target = sys.argv[1]
    else:
        return False
    resp = requests.get("https://hacked-emails.com/api?q={}".format(target), verify=True, timeout=10)
    print(resp.json())
if __name__ == '__main__':
    main()