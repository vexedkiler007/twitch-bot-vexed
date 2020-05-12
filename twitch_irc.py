import config
import irc.bot
import requests
import time

# Requires an instance of the TwitchBot Class ( can only exist in TwitchBot class)
from commands import game, title, youtube, commands, uptime, save, links, define, defineurban, next_, play


class TwitchBot(irc.bot.SingleServerIRCBot):

    def __init__(self, username, client_id, token, channel, video_queue):
        self.client_id = client_id
        self.token = token
        self.channel = '#' + channel
        self.start_time = int(time.time())

        # Get the channel id, we will need this for v5 API calls
        url = 'https://api.twitch.tv/kraken/users?login=' + channel
        headers = {'Client-ID': client_id, 'Accept': 'application/vnd.twitchtv.v5+json'}
        r = requests.get(url, headers=headers).json()
        self.channel_id = r['users'][0]['_id']

        # Create IRC bot connection
        server = 'irc.chat.twitch.tv'
        port = 6667
        print('Connecting to ' + server + ' on port ' + str(port) + '...')
        irc.bot.SingleServerIRCBot.__init__(self, [(server, port, token)], username, username)
        # queues
        self.video_queue = video_queue

    def on_welcome(self, c, e):
        print('Joining ' + self.channel)

        # You must request specific capabilities before you can use them
        c.cap('REQ', ':twitch.tv/membership')
        c.cap('REQ', ':twitch.tv/tags')
        c.cap('REQ', ':twitch.tv/commands')
        c.join(self.channel)

    def on_pubmsg(self, c, e):

        # If a chat message starts with an exclamation point, try to run it as a command
        if e.arguments[0][:1] == '!':
            cmd = e.arguments[0].split(' ')[0][1:]
            print(f'Command: {cmd}')
            self.do_command(e, cmd)

        return
    # https://github.com/sharkbound/PythonTwitchBotFramework
    # {'youtube':  youtube.youtube_command(self, e)}
    # def foo(self, e, cmd):
    #
    def do_command(self, e, cmd):
        c = self.connection
        mod = moderator(e)

        # commands only for mods
        # opens firefox and searches youtube for a video
        if cmd == 'youtube':
                if mod:
                    youtube.youtube_command(self, e)
        elif cmd == 'defineurban':
            if mod:
                defineurban.defineurban_command(self, c, e)

        # commands available for everyone
        elif cmd == 'game':
            game.game_command(self, c)
        # Creates a request to figure out which title is up
        elif cmd == "title":
            title.title_command(self, c)
        # Gives out list of available commands
        elif cmd == 'commands':
            commands.commands_command(self, c)
        # uptime of bot
        elif cmd == 'uptime':
            uptime.uptime_command(self, c)
        # save link
        elif cmd == 'save':
            save.save_command(self, e, c)
        # gives out links that were saved in the database with the !save command
        elif cmd == 'links':
            links.links_command(self, e, c)
        # defines a words with using dictionary.com
        elif cmd =='define':
            define.define_command(self, c, e)
        # skips song in youtube queue
        elif cmd == 'next':
            next_.next_command(self, c, e, youtube.event)
        # saves name to database to play coffee game
        elif cmd == 'play':
            play.play_command(e)
        else:
            c.privmsg(self.channel, "Did not understand command: " + cmd)


    # checks to see if the user is a moderator from e data


def moderator(e):
    # checks for moderator tag in e data
    if e.tags[7]['value'] == '1':
        return True
    # checks for streamer tag in e data
    if e.tags[1]['value'] == 'broadcaster/1,premium/1':
        return True
    if e.tags[1]['value'] == 'broadcaster/1':
        return True

    return False


def main(video_queue):
    username = config.c_username
    client_id = config.c_client_id
    token = config.c_token
    channel = config.c_channel

    bot = TwitchBot(username, client_id, token, channel, video_queue)
    bot.start()

if __name__ == "__main__":
    main()

# type: pubmsg, source: vexedkiller0071!vexedkiller0071@vexedkiller0071.tmi.twitch.tv, target: #vexedkiller0071, arguments: ['testing'], tags: [{'key': 'badge-info', 'value': None}, {'key': 'badges', 'value': 'broadcaster/1,premium/1'}, {'key': 'color', 'value': '#FF0000'}, {'key': 'display-name', 'value': 'vexedkiller0071'}, {'key': 'emotes', 'value': None}, {'key': 'flags', 'value': None}, {'key': 'id', 'value': '986495d5-8df1-4889-a07a-62fb0aa8b438'}, {'key': 'mod', 'value': '0'}, {'key': 'room-id', 'value': '428208221'}, {'key': 'subscriber', 'value': '0'}, {'key': 'tmi-sent-ts', 'value': '1585594790750'}, {'key': 'turbo', 'value': '0'}, {'key': 'user-id', 'value': '428208221'}, {'key': 'user-type', 'value': None}]
