from tkinter import *

# list used for button text
com_list = ["Open", "Add", "File", "Exit", "Send", "Terminal"]


# button class
class TButton:
    def __init__(self, root, xp, yp, **kwargs):
        self.button = Button(root, width=10, height=1, bg="beige", fg="blue", borderwidth=3, **kwargs)
        self.button.place(x=xp, y=yp)


class TBox:
    def __init__(self, root, xp, yp, **kwargs):
        self.text = Text(root, width=39, height=7, **kwargs)
        self.text.place(x=xp, y=yp)

    def insert_text(self, value):
        self.text.delete("1.0", END)
        self.text.insert("1.0", value)


# end classes

root = Tk()
root.geometry("350x370")
root.config(bg="grey")

text_box = TBox(root, 10, 180)  # create an instance of TBox


def insert_text(value):
    global text_box
    text_box.insert_text(value)


for y in range(3):
    for x in range(2):
        TButton(root, x * 95 + 63, y * 30 + 30, text=com_list[x + y * 2],
                command=lambda value=com_list[x + y * 2]: insert_text(value))

root.mainloop()
