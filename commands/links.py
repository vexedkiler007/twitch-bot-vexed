import sqlite3


def links_command(self, e, c):
    twitch_name = e.tags[3]['value']
    get_links = 'SELECT link_text FROM user_links WHERE user_login = :user_login'
    con = sqlite3.connect(r'C:\Users\juanr\PycharmProjects\Twitch_Bot\data\streamer_links.db')
    cur = con.cursor()
    cur.execute(get_links, (twitch_name,))
    string_url = ''
    for url in cur.fetchall():
        string_url += f"{url[0]} "
    con.commit()
    cur.close()
    c.privmsg(self.channel, string_url)

