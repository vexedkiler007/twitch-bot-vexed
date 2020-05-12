import sqlite3

def play_command(e):
    twitch_id = e.tags[12]['value']
    username = e.tags[3]['value']
    sql = 'INSERT OR REPLACE INTO usernames(twitch_id, username) VALUES (?,?)'
    con = sqlite3.connect(r'C:\Users\juanr\PycharmProjects\untitled1\play.db')
    cur = con.cursor()
    cur.execute(sql, (twitch_id, username))
    con.commit()

# !play => save to play.db
# !play => ignore
# !play and change in name => change the name in the database
# !play => ignore

