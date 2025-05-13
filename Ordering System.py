from tkinter import *
from tkinter import messagebox

class Orders:
    def __init__(self, id, name, phone_number, items):
        self.id = id
        self.name = name
        self.phone_number = phone_number
        self.items = items


class Display:
    def __init__(self, parent):
        self.standard_wd = 24
        self.half_wd = 12
        self.home_frame = Frame(parent, bg="pink")
        self.menu_frame = Frame(parent, bg="pink")
        self.order_frame = Frame(parent, bg="pink")
        self.order_info_frame = Frame(parent, bg="pink")
        self.order_confirmation_frame = Frame(parent, bg="pink")

        self.orders_list = []
        self.order_number = 1
        self.total_cost = 0
        self.order = []
        self.menu_items = {"Classic Pearl Milk Tea":{"name":"Classic Pearl Milk Tea", "price":{"Small":8.5, "Large":10.5}}, 
                           "Brown Sugar Milk Tea":{"name":"Brown Sugar Milk Tea", "price":{"Small":8.9, "Large":11.9}}, 
                           "Taro Milk Tea":{"name":"Taro Milk Tea", "price":{"Small":9, "Large":12}}, 
                           "Passionfruit Green Tea":{"name":"Passionfruit Green Tea", "price":{"Small":9.2, "Large":12.2}}, 
                           "Mango Yakult Tea":{"name":"Mango Yakult Tea", "price":{"Small":8.7, "Large":11.7}}}
        self.quantity_options = [1, 2, 3, 4]
        self.size_options = ["Small", "Large"]

        self.item_chosen = StringVar(value="Select an item")
        self.quantity_chosen = StringVar(value="Quantity")
        self.size_chosen = StringVar(value="Size")

        self.name_var = StringVar()
        self.phone_var = StringVar()


        home_title = Label(self.home_frame, text="Bobalicious", bg="hot pink", width=40, pady=4, font=(24))
        home_title.grid(row=0, column=0, columnspan=3, sticky=E+W)
        menu_but = Button(self.home_frame, text="View Menu", command=self.change_to_menu, width=self.half_wd)
        menu_but.grid(row=1, column=1, padx=2, pady=4)
        order_but = Button(self.home_frame, text="Place an order", command=self.change_to_order, width=self.half_wd)
        order_but.grid(row=2, column=1, padx=2, pady=4)
        self.home_frame.pack()

        menu_title = Label(self.menu_frame, text="Menu", bg="hot pink", pady=4)
        menu_title.grid(row=0, column=0, columnspan=3, sticky=E+W)
        column_1 = Label(self.menu_frame, text="Name;", width=self.standard_wd, bg="pink")
        column_1.grid(row=1, column=0, padx=2, pady=2)
        column_2 = Label(self.menu_frame, text="Small;", width=self.half_wd, bg="pink")
        column_2.grid(row=1, column=1, padx=2, pady=2)
        column_3 = Label(self.menu_frame, text="Large;", width=self.half_wd, bg="pink")
        column_3.grid(row=1, column=2, padx=2, pady=2)
        item_1 = Label(self.menu_frame, text="Classic Pearl Milk Tea", width=self.standard_wd, bg="pink")
        item_1.grid(row=2, column=0, padx=2, pady=2)
        item_1_small = Label(self.menu_frame, text="$8.50", width=self.half_wd, bg="pink")
        item_1_small.grid(row=2, column=1, padx=2, pady=2)
        item_1_large = Label(self.menu_frame, text="$10.50", width=self.half_wd, bg="pink")
        item_1_large.grid(row=2, column=2, padx=2, pady=2)
        item_2 = Label(self.menu_frame, text="Brown Sugar Milk Tea", width=self.standard_wd, bg="pink")
        item_2.grid(row=3, column=0, padx=2, pady=2)
        item_2_small = Label(self.menu_frame, text="$8.90", width=self.half_wd, bg="pink")
        item_2_small.grid(row=3, column=1, padx=2, pady=2)
        item_2_large = Label(self.menu_frame, text="$11.90", width=self.half_wd, bg="pink")
        item_2_large.grid(row=3, column=2, padx=2, pady=2)
        item_3 = Label(self.menu_frame, text="Taro Milk Tea", width=self.standard_wd, bg="pink")
        item_3.grid(row=4, column=0, padx=2, pady=2)
        item_3_small = Label(self.menu_frame, text="$9.00", width=self.half_wd, bg="pink")
        item_3_small.grid(row=4, column=1, padx=2, pady=2)
        item_3_large = Label(self.menu_frame, text="$12.00", width=self.half_wd, bg="pink")
        item_3_large.grid(row=4, column=2, padx=2, pady=2)
        item_4 = Label(self.menu_frame, text="Passionfruit Green Tea", width=self.standard_wd, bg="pink")
        item_4.grid(row=5, column=0, padx=2, pady=2)
        item_4_small = Label(self.menu_frame, text="$9.20", width=self.half_wd, bg="pink")
        item_4_small.grid(row=5, column=1, padx=2, pady=2)
        item_4_large = Label(self.menu_frame, text="$12.20", width=self.half_wd, bg="pink")
        item_4_large.grid(row=5, column=2, padx=2, pady=2)
        item_5 = Label(self.menu_frame, text="Mango Yakult Tea", width=self.standard_wd, bg="pink")
        item_5.grid(row=6, column=0, padx=2, pady=2)
        item_5_small = Label(self.menu_frame, text="$8.70", width=self.half_wd, bg="pink")
        item_5_small.grid(row=6, column=1, padx=2, pady=2)
        item_5_large = Label(self.menu_frame, text="$11.70", width=self.half_wd, bg="pink")
        item_5_large.grid(row=6, column=2, padx=2, pady=2)
        self.order_back_but = Button(self.menu_frame, text="Back to order", command=self.change_to_order, width=self.half_wd, state=DISABLED)
        self.order_back_but.grid(row=7, column=0, columnspan=2, padx=2, pady=4)
        back_but_menu = Button(self.menu_frame, text="Back to home", command=self.change_to_home, width=self.half_wd)
        back_but_menu.grid(row=7, column=1, columnspan=2, padx=2, pady=4)

        order_title = Label(self.order_frame, text="Order", bg="hot pink", pady=4)
        order_title.grid(row=0, column=0, columnspan=3, sticky=E+W)
        instruction_lab = Label(self.order_frame, text="Select the item, quantity and size you want from the drop down lists :)\nPlease note that going back to the main menu will cause your current order to be discarded.", bg="pink", pady=4)
        instruction_lab.grid(row=1, column=0, columnspan=3)
        item_names = []
        for i in self.menu_items:
            item_names.append(self.menu_items[i]["name"])
        self.item = OptionMenu(self.order_frame, self.item_chosen, *item_names)
        self.item.grid(row=2, column=0)
        self.quantity = OptionMenu(self.order_frame, self.quantity_chosen, *self.quantity_options)
        self.quantity.grid(row=2, column=1)
        self.size = OptionMenu(self.order_frame, self.size_chosen, *self.size_options)
        self.size.grid(row=2, column=2)
        self.current_total = Label(self.order_frame, text=f"Current total is ${round(self.total_cost, 1)}", bg="pink")
        self.current_total.grid(row=3, column=0, columnspan=3)
        add_item_but = Button(self.order_frame, text="Add to order", command=self.add_item, width=self.half_wd)
        add_item_but.grid(row=4, column=0, padx=2, pady=4)
        view_menu = Button(self.order_frame, text="View menu", command=self.change_to_menu, width=self.half_wd)
        view_menu.grid(row=4, column=1, padx=2, pady=4)
        back_but_order = Button(self.order_frame, text="Back to home", command=self.change_to_home, width=self.half_wd)
        back_but_order.grid(row=4, column=2, padx=2, pady=4)
        self.cont_but = Button(self.order_frame, text="Continue", command=self.change_to_order_info, width=self.half_wd, state=DISABLED)
        self.cont_but.grid(row=5, column=1, padx=2, pady=4)

        order_confirmation_title = Label(self.order_confirmation_frame, text="Order sucessful!", bg="hot pink", pady=4, width=self.standard_wd)
        order_confirmation_title.grid(row=0, column=0, sticky=E+W)
        self.order_confirmation_info = Label(self.order_confirmation_frame, text="Thanks for your order (name)\nYour order number is:", bg="pink", width=self.standard_wd)
        self.order_confirmation_info.grid(row=1, column=0, padx=2, pady=2)
        self.display_order_number = Label(self.order_confirmation_frame, text="(Order num)", bg="pink", font=(24), width=self.standard_wd)
        self.display_order_number.grid(row=2, column=0, rowspan=3, padx=2, pady=2)
        back_but_confirmation = Button(self.order_confirmation_frame, text="Back to home", command=self.change_to_home, width=self.half_wd)
        back_but_confirmation.grid(row=5, column=0, padx=2, pady=4)

    def change_to_menu(self):
        self.home_frame.pack_forget()
        self.order_frame.pack_forget()
        self.menu_frame.pack()

    def change_to_order(self):
        self.home_frame.pack_forget()
        self.menu_frame.pack_forget()
        self.current_total.config(text=f"Current total is ${round(self.total_cost, 1)}")
        self.order_back_but.config(state=NORMAL)
        self.order_frame.pack()

    def change_to_home(self):
        self.menu_frame.pack_forget()
        self.order_frame.pack_forget()
        self.order_info_frame.pack_forget()
        self.order_confirmation_frame.pack_forget()
        self.total_cost = 0
        self.order = []
        self.order_back_but.config(state=DISABLED)
        self.cont_but.config(state=DISABLED)
        self.home_frame.pack()
        self.item_chosen.set(value="Select an item")
        self.quantity_chosen.set(value="Quantity")
        self.size_chosen.set(value="Size")

    def change_to_order_info(self):
        num=3
        self.order_frame.pack_forget()
        order_info_title = Label(self.order_info_frame, text="Complete order", bg="hot pink", pady=4)
        order_info_title.grid(row=0, column=0, columnspan=2, sticky=E+W)
        items_lab = Label(self.order_info_frame, text="Items;", width=self.standard_wd, bg="pink")
        items_lab.grid(row=2, column=0, columnspan=2, padx=2, pady=2)
        self.order_info_frame.pack()
        for item in self.order:
            i = Label(self.order_info_frame, text=f"{item[1]} x {item[2]} {item[0]}", width=self.standard_wd, bg="pink").grid(row=num, column=0, padx=2, pady=2)
            p = Label(self.order_info_frame, text=("$" + str(item[3]), "each"), width=self.half_wd, bg="pink").grid(row=num, column=1, padx=2, pady=2)
            num+=1
        self.total_cost_lab = Label(self.order_info_frame, text=f"Your total is ${round(self.total_cost, 1)}", bg="pink")
        self.total_cost_lab.grid(row=num, column=0, columnspan=2, padx=2, pady=2)
        num+=1
        self.instructions = Label(self.order_info_frame, text="Please fill in your details to complete your order.", bg="pink")
        self.instructions.grid(row=num, column=0, columnspan=2, padx=2, pady=2)
        num+=1
        self.name_lab = Label(self.order_info_frame, text="Name;", width=self.standard_wd, bg="pink")
        self.name_lab.grid(row=num, column=0, padx=2, pady=2)
        self.name_ent = Entry(self.order_info_frame, textvariable=self.name_var, width=self.standard_wd)
        self.name_ent.grid(row=num, column=1, padx=2, pady=2)
        num+=1
        self.phone_lab = Label(self.order_info_frame, text="Phone number;", width=self.standard_wd, bg="pink")
        self.phone_lab.grid(row=num, column=0, padx=2, pady=2)
        self.phone_ent = Entry(self.order_info_frame, textvariable=self.phone_var, width=self.standard_wd)
        self.phone_ent.grid(row=num, column=1, padx=2, pady=2)
        self.name_ent.focus()
        num+=1
        self.finish_but=Button(self.order_info_frame, text="Cancel order", command=self.change_to_home, width=self.half_wd)
        self.finish_but.grid(row=num, column=0, padx=2, pady=2)
        self.finish_but=Button(self.order_info_frame, text="Finish order", command=self.change_to_order_confirm, width=self.half_wd)
        self.finish_but.grid(row=num, column=1, padx=2, pady=2)

    def add_item(self):
        if self.item_chosen.get() == "Select an item" or self.quantity_chosen.get() == "Quantity" or self.size_chosen.get() == "Size":
            messagebox.showerror("Error", "You must choose an option for all three sections before continuing. Please try again.")
        else:
            messagebox.showinfo("Added", "Item added to order.")
            self.cont_but.config(state=NORMAL)
            self.order.append([self.item_chosen.get(), self.quantity_chosen.get(), self.size_chosen.get(), self.menu_items[self.item_chosen.get()]["price"][self.size_chosen.get()]])
            self.total_cost += round(self.menu_items[self.item_chosen.get()]["price"][self.size_chosen.get()]*float(self.quantity_chosen.get()), 1)
            self.current_total.config(text=f"Current total is ${round(self.total_cost, 1)}")
            self.item_chosen.set(value="Select an item")
            self.quantity_chosen.set(value="Quantity")
            self.size_chosen.set(value="Size")
    
    def change_to_order_confirm(self):
        name = self.name_var.get().title()
        phone = self.phone_var.get()
        if phone == "" and name == "":
            messagebox.showerror("Error", "Please input your name and phone number to continue.")
            return
        elif name == "":
            messagebox.showerror("Error", "Please input your name to continue.")
            return
        elif phone == "":
            messagebox.showerror("Error", "Please input your phone number to continue.")
            return
        elif len(phone)<3:
            messagebox.showerror("Error", "The number you have given is too short to be your number. Please try again.")
            return
        phone = phone.replace(" ", "")
        try:
            phone = int(phone)
        except ValueError:
            messagebox.showerror("Error", "Please use a number as your phone number to continue.")
            return
        self.name_ent.delete(0, "end")
        self.phone_ent.delete(0, "end")
        self.name_ent.focus()
        for widget in self.order_info_frame.winfo_children():
            widget.destroy()
        self.order_info_frame.pack_forget()
        self.order_confirmation_info.config(text=f"Thanks for your order {name}\nYour order number is:")
        self.display_order_number.config(text=str(self.order_number))
        self.orders_list.append(Orders(self.order_number, name, phone, self.order))
        self.order_number += 1
        self.order_confirmation_frame.pack()



if __name__ == "__main__":
    root = Tk()
    frames = Display(root)
    root.title("Bobalicious")
    root.mainloop()