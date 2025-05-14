"""Ordering system for a bubble tea (boba) shop called Bobalicious."""
from tkinter import *
from tkinter import messagebox


class Orders:
    """Support class for the ordering system."""

    def __init__(self, id, name, phone_number, items):
        """Create the objects used in the class."""
        self.id = id
        self.name = name
        self.phone_number = phone_number
        self.items = items

    def display_info(self, f, r):
        """Display the order information stored."""
        id_lab = Label(f, text="Order number:", bg="light blue")
        id_lab.grid(row=r, column=0, padx=2, pady=2, sticky=W)
        id = Label(f, text=self.id, bg="light blue")
        id.grid(row=r, column=1, padx=2, pady=2)
        r += 1
        name_lab = Label(f, text="Name:", bg="light blue")
        name_lab.grid(row=r, column=0, padx=2, pady=2, sticky=W)
        n = Label(f, text=self.name, bg="light blue")
        n.grid(row=r, column=1, padx=2, pady=2)
        r += 1
        phone_lab = Label(f, text="Phone number:", bg="light blue")
        phone_lab.grid(row=r, column=0, padx=2, pady=2, sticky=W)
        pn = Label(f, text=self.phone_number, bg="light blue")
        pn.grid(row=r, column=1, padx=2, pady=2)
        r += 1
        items_lab = Label(f, text="Items:", bg="light blue")
        items_lab.grid(row=r, column=0, padx=2, pady=2, sticky=W)
        for b in self.items:
            i = Label(f, text=f"{b[1]} x {b[2]} {b[0]}",
                      bg="light blue").grid(row=r, column=1,
                                            padx=2, pady=2)
            r += 1
        blank_space = Label(f, text="\n", bg="light blue")
        blank_space.grid(row=r, column=0, padx=2, pady=2, sticky=W)
        r += 1
        return r


class Display:
    """Main class, this sets up the frames."""

    def __init__(self, parent):
        """Create the objects used in the class.

        This function sets up many of the widgets and all
        of the frames used.
        """
        self.standard_wd = 24
        self.half_wd = 12
        self.amount_of_rows = 1
        self.home_frame = Frame(parent, bg="pink")
        self.menu_frame = Frame(parent, bg="pink")
        self.order_frame = Frame(parent, bg="pink")
        self.order_info_frame = Frame(parent, bg="pink")
        self.order_confirmation_frame = Frame(parent, bg="pink")
        self.admin_login_frame = Frame(parent, bg="light blue")
        self.admin_view_frame = Frame(parent, bg="light blue")
        self.max_reached_frame = Frame(parent, bg="pink")
        self.orders_list = []
        self.order_number = 1
        self.total_cost = 0
        self.order = []
        self.menu_items = {"Classic Pearl Milk Tea":
                           {"Name": "Classic Pearl Milk Tea",
                            "Price": {"Small": 8.5, "Large":
                                      10.5}},
                           "Brown Sugar Milk Tea":
                           {"Name": "Brown Sugar Milk Tea",
                            "Price": {"Small": 8.9, "Large":
                                      11.9}},
                           "Taro Milk Tea":
                           {"Name": "Taro Milk Tea", "Price":
                            {"Small": 9, "Large": 12}},
                           "Passionfruit Green Tea":
                           {"Name": "Passionfruit Green Tea",
                            "Price": {"Small": 9.2, "Large":
                                      12.2}},
                           "Mango Yakult Tea":
                           {"Name": "Mango Yakult Tea",
                            "Price": {"Small": 8.7, "Large":
                                      11.7}}}
        self.quantity_options = [1, 2, 3, 4]
        self.size_options = ["Small", "Large"]
        self.item_chosen = StringVar(value="Select an item")
        self.quantity_chosen = StringVar(value="Quantity")
        self.size_chosen = StringVar(value="Size")
        self.name_var = StringVar()
        self.phone_var = StringVar()
        self.password_var = StringVar()

        """Home screen widgets"""
        home_title = Label(self.home_frame, text="Bobalicious", bg="hot pink",
                           width=40, pady=4, font=(24))
        home_title.grid(row=0, column=0, columnspan=2, sticky=E+W)
        admin_but = Button(self.home_frame, text="Admin Login",
                           command=self.change_to_admin_login,
                           width=self.half_wd)
        admin_but.grid(row=0, column=0, padx=2, pady=2, sticky=W)
        menu_but = Button(self.home_frame, text="View Menu",
                          command=self.change_to_menu,
                          width=self.half_wd)
        menu_but.grid(row=1, column=0, columnspan=2, padx=2, pady=4)
        order_but = Button(self.home_frame, text="Place an order",
                           command=self.change_to_order,
                           width=self.half_wd)
        order_but.grid(row=2, column=0, columnspan=2, padx=2, pady=4)
        self.home_frame.pack()

        """Menu screen widgets"""
        menu_title = Label(self.menu_frame, text="Menu", bg="hot pink", pady=4)
        menu_title.grid(row=0, column=0, columnspan=3, sticky=E+W)
        column_1 = Label(self.menu_frame, text="Name;", width=self.standard_wd,
                         bg="pink")
        column_1.grid(row=1, column=0, padx=2, pady=2)
        column_2 = Label(self.menu_frame, text="Small;", width=self.half_wd,
                         bg="pink")
        column_2.grid(row=1, column=1, padx=2, pady=2)
        column_3 = Label(self.menu_frame, text="Large;", width=self.half_wd,
                         bg="pink")
        column_3.grid(row=1, column=2, padx=2, pady=2)
        row_num = 2
        for n in self.menu_items:
            display_name = Label(self.menu_frame, text=self.menu_items[n]
                                 ["Name"], width=self.standard_wd, bg="pink")
            display_name.grid(row=row_num, column=0, padx=2, pady=2)
            display_small = Label(self.menu_frame,
                                  text=
                                  f"${self.menu_items[n]['Price']['Small']}",
                                  width=self.half_wd, bg="pink")
            display_small.grid(row=row_num, column=1, padx=2, pady=2)
            display_large = Label(self.menu_frame,
                                  text=
                                  f"${self.menu_items[n]['Price']['Large']}",
                                  width=self.half_wd, bg="pink")
            display_large.grid(row=row_num, column=2, padx=2, pady=2)
            row_num += 1
        self.order_back_but = Button(self.menu_frame, text="Back to order",
                                     command=self.change_to_order,
                                     width=self.half_wd, state=DISABLED)
        self.order_back_but.grid(row=7, column=0, columnspan=2, padx=2, pady=4)
        back_but_menu = Button(self.menu_frame, text="Back to home",
                               command=self.change_to_home, width=self.half_wd)
        back_but_menu.grid(row=7, column=1, columnspan=2, padx=2, pady=4)

        """Order item selection widgets"""
        order_title = Label(self.order_frame, text="Order", bg="hot pink",
                            pady=4)
        order_title.grid(row=0, column=0, columnspan=3, sticky=E+W)
        instruction_lab = Label(self.order_frame,
                                text=(
                                    "Select the item, quantity and size you "
                                    "want from the drop down lists :)\n"
                                    "Please note that going back to the "
                                    "main menu will cause your current "
                                    "order to be discarded."
                                ),
                                bg="pink", pady=4)
        instruction_lab.grid(row=1, column=0, columnspan=3)
        item_names = []
        for i in self.menu_items:
            item_names.append(self.menu_items[i]["Name"])
        self.item = OptionMenu(self.order_frame, self.item_chosen, *item_names)
        self.item.grid(row=2, column=0)
        self.quantity = OptionMenu(self.order_frame, self.quantity_chosen,
                                   *self.quantity_options)
        self.quantity.grid(row=2, column=1)
        self.size = OptionMenu(self.order_frame, self.size_chosen,
                               *self.size_options)
        self.size.grid(row=2, column=2)
        self.current_total = Label(self.order_frame,
                                   text=(
                                       "Current total is $"
                                       f"{round(self.total_cost, 1)}"
                                       ),
                                   bg="pink")
        self.current_total.grid(row=3, column=0, columnspan=3)
        add_item_but = Button(self.order_frame, text="Add to order",
                              command=self.add_item, width=self.half_wd)
        add_item_but.grid(row=4, column=0, padx=2, pady=4)
        view_menu = Button(self.order_frame, text="View menu",
                           command=self.change_to_menu, width=self.half_wd)
        view_menu.grid(row=4, column=1, padx=2, pady=4)
        back_but_order = Button(self.order_frame, text="Back to home",
                                command=self.change_to_home,
                                width=self.half_wd)
        back_but_order.grid(row=4, column=2, padx=2, pady=4)
        self.cont_but = Button(self.order_frame, text="Continue",
                               command=self.change_to_order_info,
                               width=self.half_wd, state=DISABLED)
        self.cont_but.grid(row=5, column=1, padx=2, pady=4)

        """Order confirmation widgets"""
        order_confirmation_title = Label(self.order_confirmation_frame,
                                         text="Order sucessful!",
                                         bg="hot pink", pady=4,
                                         width=self.standard_wd)
        order_confirmation_title.grid(row=0, column=0, sticky=E+W)
        self.order_confirmation_info = Label(self.order_confirmation_frame,
                                             text=(
                                                 "Thanks for your order (name"
                                                 ")\nYour order number is:"
                                             ), bg="pink",
                                             width=self.standard_wd)
        self.order_confirmation_info.grid(row=1, column=0, padx=2, pady=2)
        self.display_order_number = Label(self.order_confirmation_frame,
                                          text="(Order num)", bg="pink",
                                          font=(24), width=self.standard_wd)
        self.display_order_number.grid(row=2, column=0, rowspan=3, padx=2,
                                       pady=2)

        """Admin login widgets"""
        admin_login_title = Label(self.admin_login_frame, text="Admin Login",
                                  bg="light blue", pady=4,
                                  width=self.standard_wd)
        admin_login_title.grid(row=0, column=0, columnspan=2, sticky=E+W)
        self.password_lab = Label(self.admin_login_frame, text="Password:",
                                  width=self.standard_wd, bg="light blue")
        self.password_lab.grid(row=1, column=0, padx=2, pady=2)
        self.password_ent = Entry(self.admin_login_frame,
                                  textvariable=self.password_var,
                                  width=self.standard_wd)
        self.password_ent.grid(row=1, column=1, padx=2, pady=2)
        login_but = Button(self.admin_login_frame, text="Log in",
                           command=self.change_to_admin_view,
                           width=self.half_wd)
        login_but.grid(row=2, column=1, padx=2, pady=4)

        """Max reached widgets"""
        max_reached_lab = Label(self.max_reached_frame, text=(
            "Unfortunately we cannot take anymore orders tday.\nWe apologise "
            "for any inconvenience.\n\nWe look forward to seeing you tomorrow!"
            ), bg="pink")
        max_reached_lab.grid(row=0, column=0, padx=2, pady=2)
        admin_login_but = Button(self.max_reached_frame, text="Admin login",
                                 command=self.change_to_admin_login,
                                 width=self.half_wd)
        admin_login_but.grid(row=1, column=0, padx=2, pady=4)

    def change_to_menu(self):
        """Hide the home and order frames and display the menu."""
        self.home_frame.pack_forget()
        self.order_frame.pack_forget()
        self.menu_frame.pack()

    def change_to_order(self):
        """Hide the home and menu screens and display the order frame."""
        self.home_frame.pack_forget()
        self.menu_frame.pack_forget()
        self.current_total.config(text=(
                                       "Current total is $"
                                       f"{round(self.total_cost, 1)}"
                                       ))
        self.order_back_but.config(state=NORMAL)
        self.order_frame.pack()

    def change_to_home(self):
        """Hide frames listed below."""
        self.menu_frame.pack_forget()
        self.order_frame.pack_forget()
        self.order_info_frame.pack_forget()
        self.order_confirmation_frame.pack_forget()
        self.admin_login_frame.pack_forget()

        """Destroy all of the widgets in the admin view frame,
        so when it is displayed again they don't overlap"""
        for widget in self.admin_view_frame.winfo_children():
            widget.destroy()
        self.admin_view_frame.pack_forget()

        """Resets all of the information to do with the current
        order, then display the home screen"""
        self.total_cost = 0
        self.order = []
        self.order_back_but.config(state=DISABLED)
        self.cont_but.config(state=DISABLED)
        self.home_frame.pack()
        self.item_chosen.set(value="Select an item")
        self.quantity_chosen.set(value="Quantity")
        self.size_chosen.set(value="Size")

    def add_item(self):
        """Add an item to the user's order.
         
        If they have chosen an option from all three optionmenus, then reset
        the values, if not, tell them they need to.
        """
        if (self.item_chosen.get() == "Select an item" or
            self.quantity_chosen.get() == "Quantity" or
            self.size_chosen.get() == "Size"):
            messagebox.showerror("Error", "You must choose an " \
            "option for all three sections before continuing. " \
            "Please try again.")
        else:
            messagebox.showinfo("Added", "Item added to order.")
            self.cont_but.config(state=NORMAL)
            self.order.append([self.item_chosen.get(),
                               self.quantity_chosen.get(),
                               self.size_chosen.get(),
                               self.menu_items[
                                   self.item_chosen.get()]["Price"][
                                           self.size_chosen.get()]])
            self.total_cost += round(self.menu_items[
                self.item_chosen.get()]["Price"][self.size_chosen.get()]*float(
                    self.quantity_chosen.get()), 1)
            self.current_total.config(text=f"Current total is ${round(self.total_cost, 1)}")
            self.item_chosen.set(value="Select an item")
            self.quantity_chosen.set(value="Quantity")
            self.size_chosen.set(value="Size")

    def change_to_order_info(self):
        """Hide the order frame and set up + display data collection frame."""
        num=3
        self.order_frame.pack_forget()
        order_info_title = Label(self.order_info_frame,
                                 text="Complete order",
                                 bg="hot pink", pady=4)
        order_info_title.grid(row=0, column=0, columnspan=2, sticky=E+W)
        items_lab = Label(self.order_info_frame, text="Items;",
                          width=self.standard_wd, bg="pink")
        items_lab.grid(row=2, column=0, columnspan=2, padx=2, pady=2)
        self.order_info_frame.pack()

        """Set up labels to display the items in the user's order"""
        for item in self.order:
            i = Label(self.order_info_frame, text=(
                f"{item[1]} x {item[2]} {item[0]}"),
                      width=self.standard_wd, bg="pink")
            i.grid(row=num, column=0, padx=2, pady=2)
            p = Label(self.order_info_frame, text=("$" + str(item[3]), "each"),
                      width=self.half_wd, bg="pink")
            p.grid(row=num, column=1, padx=2, pady=2)
            num+=1
        
        """Set up the entry widgets asking for the user's details,
        under the list of their items"""
        self.total_cost_lab = Label(self.order_info_frame,
                                    text=(
                                       "Current total is $"
                                       f"{round(self.total_cost, 1)}"
                                       ), bg="pink")
        self.total_cost_lab.grid(row=num, column=0, columnspan=2,
                                 padx=2, pady=2)
        num += 1
        self.instructions = Label(self.order_info_frame,
                                  text=(
                                      "Please fill in your details to complete"
                                      " your order."
                                  ), bg="pink")
        self.instructions.grid(row=num, column=0, columnspan=2, padx=2, pady=2)
        num += 1
        self.name_lab = Label(self.order_info_frame, text="Name;",
                              width=self.standard_wd, bg="pink")
        self.name_lab.grid(row=num, column=0, padx=2, pady=2)
        self.name_ent = Entry(self.order_info_frame,
                              textvariable=self.name_var,
                              width=self.standard_wd)
        self.name_ent.grid(row=num, column=1, padx=2, pady=2)
        num += 1
        self.phone_lab = Label(self.order_info_frame,
                               text="Phone number;", width=self.standard_wd,
                               bg="pink")
        self.phone_lab.grid(row=num, column=0, padx=2, pady=2)
        self.phone_ent = Entry(self.order_info_frame,
                               textvariable=self.phone_var,
                               width=self.standard_wd)
        self.phone_ent.grid(row=num, column=1, padx=2, pady=2)
        num += 1
        self.cancel_but=Button(self.order_info_frame, text="Cancel order",
                               command=self.change_to_home, width=self.half_wd)
        self.cancel_but.grid(row=num, column=0, padx=2, pady=2)
        self.finish_but=Button(self.order_info_frame, text="Finish order",
                               command=self.change_to_order_confirm,
                               width=self.half_wd)
        self.finish_but.grid(row=num, column=1, padx=2, pady=2)

        """Ensure the entry widgets are empty and focused on the top box."""
        self.name_ent.delete(0, "end")
        self.phone_ent.delete(0, "end")
        self.name_ent.focus()

    def change_to_order_confirm(self):
        """Hide the order info frame and display the order confirmation.

        Checks if the user has entered values into both entry widgets,
        then if the phone number is long enough before destroying all of
        the widgets in the order info frame, so when it is displayed again
        the new widgets don't overlay previous ones, then adds the user's
        order to a list as an object of the support class.
        """
        name = self.name_var.get().title()
        phone = self.phone_var.get()
        if phone == "" and name == "":
            messagebox.showerror("Error", "Please input your name and phone " \
            "number to continue.")
            return
        elif name == "":
            messagebox.showerror("Error", "Please input your name to " \
            "continue.")
            return
        elif phone == "":
            messagebox.showerror("Error", "Please input your phone number " \
            "to continue.")
            return
        phone = phone.replace(" ", "")
        if len(phone)<3:
            messagebox.showerror("Error", "The number you have given is too " \
            "short to be your number. Please try again.")
            return
        try:
            phone = int(phone)
        except ValueError:
            messagebox.showerror("Error", "Please use a number as your phone" \
            " number to continue.")
            return
        if phone<0:
            messagebox.showerror("Error", "The number you have given is " \
            "negative. Please use a positive value.")
            return
        for widget in self.order_info_frame.winfo_children():
            widget.destroy()
        self.order_info_frame.pack_forget()
        self.order_confirmation_info.config(text=(
            f"Thanks for your order {name}\nYour order number is:"))
        self.display_order_number.config(text=str(self.order_number))
        self.orders_list.append(Orders(self.order_number, name, phone,
                                       self.order))
        self.amount_of_rows += len(self.order) + 5
        self.order_number += 1
        self.order_confirmation_frame.pack()
        if self.amount_of_rows >= 22:
            back_but_confirmation = Button(self.order_confirmation_frame,
                                           text="Back to home",
                                           command=self.change_to_max_reached,
                                           width=self.half_wd)
        else:
            back_but_confirmation = Button(self.order_confirmation_frame,
                                           text="Back to home",
                                           command=self.change_to_home,
                                           width=self.half_wd)
        back_but_confirmation.grid(row=5, column=0, padx=2, pady=4)

    def change_to_admin_login(self):
        """Hide frames then display the admin login frame.
        
        Hides the home, order confirmation, and max (orders) reached frames
         then displays the admin login frame, focusing on the password
         entry widget.
        """
        self.home_frame.pack_forget()
        self.order_confirmation_frame.pack_forget()
        self.max_reached_frame.pack_forget()
        if self.amount_of_rows >= 22:
            self.back_but_admin_login = Button(self.admin_login_frame,
                                               text="Back",
                                               command=(
                                                   self.change_to_max_reached),
                                               width=self.half_wd)
        else:
            self.back_but_admin_login = Button(self.admin_login_frame,
                                               text="Back",
                                               command=self.change_to_home,
                                               width=self.half_wd)
        self.back_but_admin_login.grid(row=2, column=0, padx=2, pady=4)
        self.admin_login_frame.pack()
        self.password_ent.focus()

    def change_to_max_reached(self):
        self.order_confirmation_frame.pack_forget()
        self.admin_login_frame.pack_forget()
        self.admin_view_frame.pack_forget()
        self.max_reached_frame.pack()

    def change_to_admin_view(self):
        """Hide the admin login frame, then display admin view frame.
        
        Ensures the user has entered a password, then checks if it is correct,
        if it is, the admin login frame is hidden and the admin view frame is
        displayed, if not, the user is told to try again.
        """
        password = self.password_var.get()
        self.password_ent.delete(0, "end")
        self.password_ent.focus()
        if password == "":
            messagebox.showerror("Error", "Please enter password to continue.")
            return
        try:
            password = int(password)
        except ValueError:
            messagebox.showerror("Error", "Password incorrect." \
            " Please try again.")
            return
        if password != 5764:
            messagebox.showerror("Error", "Password incorrect." \
            " Please try again.")
            return
        self.admin_login_frame.pack_forget()
        admin_view_title = Label(self.admin_view_frame,
                                 text="Current orders;",
                                 bg="light blue", pady=4,
                                 width=self.standard_wd)
        admin_view_title.grid(row=0, column=0, columnspan=2, sticky=E+W)
        self.admin_view_frame.pack()

        """Checks if there are any orders, if not, the program displays
        'None', if there are, it runs the display_info function
        (defined in the support class) on every order in the list"""
        if len(self.orders_list) == 0:
            order = Label(self.admin_view_frame, text="None",
                          bg="light blue", width=self.standard_wd)
            order.grid(row=1, column=0, columnspan=2, sticky=E+W)
            back_but_admin_view = Button(self.admin_view_frame, text="Exit",
                                         command=self.change_to_home,
                                         width=self.half_wd)
            back_but_admin_view.grid(row=2, column=0, columnspan=2,
                                     padx=2, pady=4)
        else:
            row = 1
            for o in self.orders_list:
                row = o.display_info(self.admin_view_frame, row)
            if self.amount_of_rows >= 22:
                back_but_admin_view = Button(self.admin_view_frame,
                                             text="Exit",
                                             command=(
                                                 self.change_to_max_reached),
                                             width=self.half_wd)
            else:
                back_but_admin_view = Button(self.admin_view_frame,
                                             text="Exit",
                                             command=self.change_to_home,
                                             width=self.half_wd)
            back_but_admin_view.grid(row=row, column=0, columnspan=2,
                                     padx=2, pady=4)


if __name__ == "__main__":
    root = Tk()
    frames = Display(root)
    root.title("Bobalicious")
    root.mainloop()
    