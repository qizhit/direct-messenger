"""
a5.py
"""

# Qizhi Tian
# qizhit@uci.edu
# 45765950

# 168.235.86.101

import tkinter as tk
from a5_gui import MainApp

if __name__ == "__main__":
    if __name__ == "__main__":
        # All Tkinter programs start with a root window.
        # We will name ours 'main'.
        main = tk.Tk()

        # 'title' assigns a text value to the Title Bar area of a window.
        main.title("ICS 32 Distributed Social Messenger")

        # This is just an arbitrary starting point. You can change the value
        # around to see how the starting size of the window changes.
        main.geometry("720x480")

        # adding this option removes some legacy behavior with menus that
        # some modern OSes don't support. If you're curious,
        # feel free to comment out and see how the menu changes.
        main.option_add('*tearOff', False)

        # Initialize the MainApp class, which is the starting point for the
        # widgets used in the program. All of the classes that we use,
        # subclass Tk.Frame, since our root frame is main, we initialize
        # the class with it.
        app = MainApp(main)

        # When update is called, we finalize the states of all widgets that
        # have been configured within the root frame. Here, update ensures that
        # we get an accurate width and height
        # reading based on the types of widgets we have used.
        # minsize prevents the root window from resizing too small.
        # Feel free to comment it out and see how the resizing
        # behavior of the window changes.
        main.update()
        main.minsize(main.winfo_width(), main.winfo_height())
        id_ = main.after(2000, app.check_new)
        print(id_)
        # And finally, start up the event loop for the program (you can find
        # more on this in lectures of week 9 and 10).
        main.mainloop()
