import requests
import pyperclip

def main():
    url_base = 'https://raw.githubusercontent.com/Pranavkak/daa/main/{}.txt'

    code = input('Enter the code to copy: ')

    url = url_base.format(code)

    response = requests.get(url)

    if response.status_code == 200:
        pyperclip.copy(response.text)
        print('Copied to clipboard!')
    else:
        print('Failed to fetch code')
