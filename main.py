import json
import time
import vlc

f = open('data/data.json')
data = json.load(f)
f.close()

short_enabled = False

def play_on_time(data):
  if time.strftime("%H:%M", time.localtime()) in data:
    play_n_clocks(3)
    time.sleep(60)

def play_n_clocks(n):
  for _ in range(n):
    p = vlc.MediaPlayer("data/clock.mp3")
    p.play()
    time.sleep(1)
    duration = p.get_length() / 1000
    time.sleep(duration - 1)

while True:
  if short_enabled:
    play_on_time(data["short_hours"])
  else:
    play_on_time(data["normal_hours"])


