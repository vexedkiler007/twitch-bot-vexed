import time

def uptime_command(self, c):
    time_passed = int(time.time()) - self.start_time
    hours = time_passed // (60*60)
    minutes = (time_passed//60)%60
    c.privmsg(self.channel, f"The stream has been up for {hours} hour(s) and {minutes} minute(s)")
    del time_passed
    del minutes
    del hours
