import requests

def title_command(self, c ):
    url = 'https://api.twitch.tv/kraken/channels/' + self.channel_id
    headers = {'Client-ID': self.client_id, 'Accept': 'application/vnd.twitchtv.v5+json'}
    r = requests.get(url, headers=headers).json()
    c.privmsg(self.channel, f"{r['display_name'].rstrip()}'s channel title is {r['status'].rstrip()}")
