from tkinter import *

class Orders:
    def __init__(self, name, phone_number, items):
        self.name = name
        self.phone_number = phone_number
        self.items = items


class Display:
    def __init__(self, parent):
        WD = 20
        self.menu_frame = Frame(parent, bg="pink")
        self.order_frame = Frame(parent, bg="light blue")
        self.order_confirmation_frame = Frame(parent, bg="light yellow")
