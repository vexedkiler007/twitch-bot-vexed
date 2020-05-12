import sqlite3
import re


def on_start():
    con = sqlite3.connect(r'C:\Users\juanr\PycharmProjects\Twitch_Bot\data\streamer_links.db')
    create_table = 'CREATE TABLE user_links (user_login varchar(255), link_text varchar(255))'
    create_index = 'CREATE UNIQUE INDEX user_login_link_text ON user_links (user_login, link_text)'
    c = con.cursor()
    c.execute(create_table)
    c.execute(create_index)
    con.commit()
    c.close()


def save_command(self, e, c):
    twitch_name = e.tags[3]['value']
    try:
        twitch_link = e.arguments[0].split()[1]
    except IndexError:
        c.privmsg(self.channel, f'You forgot arguments {twitch_name}')


    if validate_url(twitch_link):
        con = sqlite3.connect(r'C:\Users\juanr\PycharmProjects\Twitch_Bot\data\streamer_links.db')
        save_link = 'INSERT OR IGNORE INTO user_links (user_login, link_text) VALUES (:user_login, :link_text)'
        cur = con.cursor()
        cur.execute(save_link, (twitch_name, twitch_link))
        con.commit()
        cur.close()
    else:
        c.privmsg(self.channel, f'Invalid link {twitch_name}')


def validate_url(url):
        # oof re seems hard
        return re.match(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', url)




