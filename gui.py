from tkinter import *


def main():
    root = Tk()
    switch_frame = Frame(root)

    screen_width = int(float(root.winfo_screenwidth()))
    screen_height = int(float(root.winfo_screenheight()))

    switch_frame.pack()

    switch_variable = StringVar(value="normal")
    normal_hours_button = Radiobutton(switch_frame, text="Normalne godziny", variable=switch_variable,
                                      indicatoron=False, value="normal", width=200, height=screen_height)
    short_hours_button = Radiobutton(switch_frame, text="Skrocone godziny", variable=switch_variable,
                                     indicatoron=False, value="short", width=200, height=screen_height)

    normal_hours_button.pack(fill=BOTH, side=LEFT, expand=True)
    short_hours_button.pack(fill=BOTH, side=RIGHT, expand=True)

    root.overrideredirect(True)
    root.overrideredirect(False)
    root.attributes('-fullscreen', True)
    root.mainloop()
