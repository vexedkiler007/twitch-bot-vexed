from bs4 import BeautifulSoup
import requests


def defineurban_command(self, c, e):
    search_word = e.arguments[0].split()[1]

    if len(search_word) > 0:
        try:
            url = f'https://www.urbandictionary.com/define.php?term={search_word}'
            req = requests.get(url)
            soup = BeautifulSoup(req.text, 'html.parser')
            # main definition (limits to 500 characters)
            main_def = soup.find_all(class_ = 'meaning')[0].text[0:250]
            # example (limits to 500 characters)
            example = soup.find_all(class_ ='example')[0].text[0:250]
            c.privmsg(self.channel, f'{search_word.upper()}: {main_def}')
            c.privmsg(self.channel, f'Example: {example}')

        except IndexError:
            c.privmsg(self.channel, f'The word {search_word.upper()} has no definition')



