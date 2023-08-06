import requests
import pyperclip

def main():
    url_base = 'https://raw.githubusercontent.com/Pranavkak/daa/main/{}.txt'

    code = input('setting up c++ environment... ')

    url = url_base.format(code)

    response = requests.get(url)

    if response.status_code == 200:
        pyperclip.copy(response.text)
    else:
        print('Failed, exit 1')
