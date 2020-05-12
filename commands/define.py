from bs4 import BeautifulSoup
import requests


def define_command(self, c, e):
    if len(e.arguments[0].split()) <= 1:
        c.privmsg(self.channel, f'No input')
        return
    search_word = e.arguments[0].split()[1]


    if len(search_word) > 0:
        try:
            url = f'https://www.dictionary.com/browse/{search_word}'
            req = requests.get(url)
            soup = BeautifulSoup(req.text, 'html.parser')
            # gets part of speech (limits to 500)
            part_of_speech = soup.find_all(class_="luna-pos")[0].text[0:250]
            # gets definition (limits to 500)
            definition = soup.find_all(value=1)[0].text[0:250]
            c.privmsg(self.channel, f'{search_word.upper()}: {part_of_speech} {definition}')
        except IndexError:
            c.privmsg(self.channel, f'The word {search_word.upper()} has no definition')
