import requests
import config
from urllib.parse import urlencode


def get_meme_templates():
    url = config.API_URL + 'get_memes'

    result = requests.get(url).json()['data']['memes']

    return result


def get_meme(id):
    all_memes = get_meme_templates()
    for meme in all_memes:
        if meme["id"] == id:
            return meme


def create_meme(id, texts=[]):
    url = config.API_URL + 'caption_image'
    params = f'?username={config.USERNAME}&password={config.PASSWORD}&template_id={id}&'
    params += f'text0={texts[0]}&text1={texts[1]}'
    result = requests.post(url+params).json()

    return result
