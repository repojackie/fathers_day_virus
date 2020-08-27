"""
Python 3.6+
tkinter 
"""
from tkinter import Tk, Label, Button, Toplevel
import random 

msg_list = ['An error has occured. Please click \"ok\" to continue.',
            'Everything is up-to-date. Click \"ok\" to continue',
            'Your process has completed. Click \"ok\" to continue']

class Spawner:
    def __init__(self, master):
        """
        Basic init junk 
        """
        self.master = master 
        master.title("Process complete")

        msg = random.choice(msg_list)
        self.label = Label(master, text=msg);
        self.label.pack()

        self.spawn_button = Button(master, text="Ok", command=self.make_children)
        self.spawn_button.pack()

        self.master.protocol("WM_DELETE_WINDOW", self.make_children)

        # for tha killswitch owo 
        self.master.bind("<Key>", self.killswitch)
        
    def make_children(self):
        """
        Creates two child windows
        """
        self.other_window = Spawner(Toplevel(self.master))
        self.new_window = Spawner(Toplevel(self.master))

    def killswitch(self, event):
        """
        't' key to stop windows from popping up
        """
        if (event.char == 't'):
            self.fathers_day_dialog()

    def fathers_day_dialog(self):
        """
        Creates a single dialog window to actually 
        terminate the process.
        """
        f_root = Toplevel(self.master)
        f_root.label = Label(f_root, bg="red", text="Happy fathers day from your favorite script kiddie.")
        f_root.label.pack()

        f_root.button = Button(f_root, bg="green", text="Click this button to close all windows for real.", command=self.destroy_all)
        f_root.button.pack()

    def destroy_all(self):
        """
        Responsible for destroying all of the windows 
        and stopping the program.
        """
        root.destroy()

if __name__ == "__main__":
    root = Tk() 
    gui = Spawner(root) 
    root.mainloop()
