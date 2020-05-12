# string of commands goes here
# length for message might require two messages if string gets to long
commands = '!commands !game !title !uptime !youtube <youtube link> !save <save link> !links !define <search term> ' \
           '!defineurban <search term> !play'


# reads out commands
def commands_command(self, c):
    c.privmsg(self.channel, commands)
