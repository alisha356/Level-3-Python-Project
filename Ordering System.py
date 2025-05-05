from tkinter import *

class Orders:
    def __init__(self, name, phone_number, items):
        self.name = name
        self.phone_number = phone_number
        self.items = items


class Display:
    def __init__(self, parent):
        standard_wd = 24
        half_wd = 12
        self.home_frame = Frame(parent, bg="pink")
        self.menu_frame = Frame(parent, bg="pink")
        self.order_frame = Frame(parent, bg="pink")
        self.order_confirmation_frame = Frame(parent, bg="pink")

        home_title = Label(self.home_frame, text="Bobalicious", bg="hot pink", width=40, pady=4, font=(24))
        home_title.grid(row=0, column=0, columnspan=3, sticky=E+W)
        menu_but = Button(self.home_frame, text="View Menu", command=self.change_to_menu, width=half_wd)
        menu_but.grid(row=1, column=1, padx=2, pady=4)
        order_but = Button(self.home_frame, text="Place an order", command=self.change_to_order, width=half_wd)
        order_but.grid(row=2, column=1, padx=2, pady=4)
        self.home_frame.pack()


        menu_title = Label(self.menu_frame, text="Menu", bg="hot pink", pady=4)
        menu_title.grid(row=0, column=0, columnspan=3, sticky=E+W)
        column_1 = Label(self.menu_frame, text="Name", width=standard_wd, bg="pink")
        column_1.grid(row=1, column=0, padx=2, pady=2)
        column_2 = Label(self.menu_frame, text="Small", width=half_wd, bg="pink")
        column_2.grid(row=1, column=1, padx=2, pady=2)
        column_3 = Label(self.menu_frame, text="Large", width=half_wd, bg="pink")
        column_3.grid(row=1, column=2, padx=2, pady=2)

        item_1 = Label(self.menu_frame, text="Classic Pearl Milk Tea", width=standard_wd, bg="pink")
        item_1.grid(row=2, column=0, padx=2, pady=2)
        item_1_small = Label(self.menu_frame, text="$8.00", width=half_wd, bg="pink")
        item_1_small.grid(row=2, column=1, padx=2, pady=2)
        item_1_large = Label(self.menu_frame, text="$10.50", width=half_wd, bg="pink")
        item_1_large.grid(row=2, column=2, padx=2, pady=2)

        item_2 = Label(self.menu_frame, text="Brown Sugar Milk Tea", width=standard_wd, bg="pink")
        item_2.grid(row=3, column=0, padx=2, pady=2)
        item_2_small = Label(self.menu_frame, text="$8.90", width=half_wd, bg="pink")
        item_2_small.grid(row=3, column=1, padx=2, pady=2)
        item_2_large = Label(self.menu_frame, text="$11.90", width=half_wd, bg="pink")
        item_2_large.grid(row=3, column=2, padx=2, pady=2)

        item_3 = Label(self.menu_frame, text="Taro Milk Tea", width=standard_wd, bg="pink")
        item_3.grid(row=4, column=0, padx=2, pady=2)
        item_3_small = Label(self.menu_frame, text="$9.00", width=half_wd, bg="pink")
        item_3_small.grid(row=4, column=1, padx=2, pady=2)
        item_3_large = Label(self.menu_frame, text="$12.00", width=half_wd, bg="pink")
        item_3_large.grid(row=4, column=2, padx=2, pady=2)

        item_4 = Label(self.menu_frame, text="Passionfruit Green Tea", width=standard_wd, bg="pink")
        item_4.grid(row=5, column=0, padx=2, pady=2)
        item_4_small = Label(self.menu_frame, text="$9.20", width=half_wd, bg="pink")
        item_4_small.grid(row=5, column=1, padx=2, pady=2)
        item_4_large = Label(self.menu_frame, text="$12.20", width=half_wd, bg="pink")
        item_4_large.grid(row=5, column=2, padx=2, pady=2)

        item_5 = Label(self.menu_frame, text="Mango Yakult Tea", width=standard_wd, bg="pink")
        item_5.grid(row=6, column=0, padx=2, pady=2)
        item_5_small = Label(self.menu_frame, text="$8.70", width=half_wd, bg="pink")
        item_5_small.grid(row=6, column=1, padx=2, pady=2)
        item_5_large = Label(self.menu_frame, text="$11.70", width=half_wd, bg="pink")
        item_5_large.grid(row=6, column=2, padx=2, pady=2)

        back_but = Button(self.menu_frame, text="Back to home", command=self.change_to_home, width=half_wd)
        back_but.grid(row=7, column=0, columnspan=3, padx=2, pady=4)

    def change_to_menu(self):
        self.home_frame.pack_forget()
        self.menu_frame.pack()

    def change_to_order(self):
        self.home_frame.pack_forget()
        self.order_frame.pack()

    def change_to_home(self):
        self.menu_frame.pack_forget()
        self.home_frame.pack()




if __name__ == "__main__":
    root = Tk()
    frames = Display(root)
    root.title("Bobalicious")
    root.mainloop()