import json
import time
import vlc
import gui

f = open('data/data.json')
data = json.load(f)
f.close()

short_enabled = False
index = 0


def play_on_time(data):
    time_string = time.strftime("%H:%M", time.localtime())
    if time_string in data:
        global index
        index = data.index(time_string) + 1
        play_n_clocks(3)


def play_n_clocks(n):
    for _ in range(n):
        p = vlc.MediaPlayer("data/clock.mp3")
        p.play()
        time.sleep(1)
        duration = p.get_length() / 1000
        time.sleep(duration - 1)


while True:
    gui.main()
    # TODO: LCD DISPLAY IMPLEMENTATION
    if short_enabled:
        play_on_time(data["short_hours"])
        print(index)
        print(data["short_hours"][index])
        time.sleep(60)
    else:
        play_on_time(data["normal_hours"])
        print(index)
        print(data["normal_hours"][index])
        time.sleep(60)
