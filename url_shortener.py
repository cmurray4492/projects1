"""URL Shourtener Project
Need to handle errors and different statuses - API Docs"""
# API key 07027f337678b2058339ea925cdab51de06be

from typing import Final
import requests
API_KEY: Final[str] = '07027f337678b2058339ea925cdab51de06be'
BASE_URL: Final[str] = 'https://cutt.ly/api/api.php'


def shorten_link(full_link: str):
    """founction to shorten link through API"""
    payload: dict = {'key': API_KEY, 'short': full_link}
    request = requests.get(BASE_URL, params=payload)
    data: dict = request.json()

    if url_data := data.get('url'):
        if url_data['status'] == 7:
            short_link: str = url_data['shortLink']
            print('Link: ', short_link)
        else:
            print('Error status: ', url_data['status'])


def main():
    """Main porgram function and entry point"""
    input_link: str = input('Enter a link to shorten: ')
    shorten_link(input_link)


if __name__ == '__main__':
    main()
