import twitch_irc
import queue
import threading
from commands import youtube

video_queue = queue.Queue()

playing_thread = threading.Thread(target=youtube.playing_video_loop, args=(video_queue,), daemon=True)
playing_thread.start()
twitch_irc.main(video_queue=video_queue)
