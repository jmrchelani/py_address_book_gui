import tkinter as tk
import tkinter.font as tkFont

# A model class for address (Contact)
class Address:
    # first name, surname, address, phone number, mobile number, and email address
    def __init__(self, first_name, surname, address, phone_number, mobile_number, email_address, image):
        self.first_name = first_name
        self.surname = surname
        self.address = address
        self.phone_number = phone_number
        self.mobile_number = mobile_number
        self.email_address = email_address

    def __str__(self):
        return '{} {}'.format(self.first_name, self.surname)

# A class which represents the whole address book containing all the contacts
class AddressBook:

    # Constructor
    def __init__(self):
        self.addresses = []

    # function to add a new contact to the address book
    def add(self, address):
        self.addresses.append(address)

    
    def delete(self, index): # delete a contact from the address book
        self.addresses.pop(index)

    
    def change(self, index, address): # change a contact in the address book
        self.addresses[index] = address

    def lookup(self, index): # lookup a contact in the address book
        return self.addresses[index]

    def index_of(self, address): # return the index of a contact in the address book
        return self.addresses.index(address)

    # function to sort the address list alphabetically by first name   
    def sort_by_first_name(self):
        self.addresses.sort(key=lambda x: x.first_name)

    def print_list(self): # print the address list
        for i in range(len(self.addresses)):
            print(self.addresses[i].first_name, self.addresses[i].surname)


class ListWindow:
    def __init__(self, root, item_list):
        #setting title
        root.title("Address Book")
        #setting window size
        width=590
        height=470
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        self.root = root

        

        GListBox_737=tk.Listbox(root)
        scrollbar = tk.Scrollbar(GListBox_737)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        GListBox_737.config(yscrollcommand=scrollbar.set)

        self.list_box=GListBox_737
        self.old_items = item_list.addresses

        GListBox_737.insert(tk.END, *item_list.addresses)

        def callback(event):
            selection = event.widget.curselection()
            if selection:
                ContactWindow.show_window(self.old_items[selection[0]], self) # When a contact is clicked then opens contact window
                
           

        GListBox_737.bind("<<ListboxSelect>>", callback)
       
        GListBox_737["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=14)
        GListBox_737["font"] = ft
        GListBox_737["fg"] = "#333333"
        GListBox_737["justify"] = "center"
        GListBox_737.place(x=250,y=100,width=279,height=271)

        GLabel_163=tk.Label(root)
        ft = tkFont.Font(family='Times',size=34)
        GLabel_163["font"] = ft
        GLabel_163["fg"] = "#333333"
        GLabel_163["justify"] = "center"
        GLabel_163["text"] = "Address Book"
        GLabel_163.place(x=170,y=30,width=254,height=36)

        GButton_96=tk.Button(root, highlightbackground="#5fb878")
        GButton_96["bg"] = "#5fb878"
        ft = tkFont.Font(family='Times',size=10)
        GButton_96["font"] = ft
        GButton_96["fg"] = "#000000"
        GButton_96["justify"] = "center"
        GButton_96["text"] = "Add New Address"
        GButton_96.place(x=320,y=390,width=147,height=36)
        GButton_96["command"] = self.GButton_96_command

        GButton_37=tk.Button(root, highlightbackground="#ffc592")
        GButton_37["bg"] = "#ffc592"
        ft = tkFont.Font(family='Times',size=10)
        GButton_37["font"] = ft
        GButton_37["fg"] = "#000000"
        GButton_37["justify"] = "center"
        GButton_37["text"] = "First Name"
        GButton_37.place(x=60,y=180,width=147,height=36)
        GButton_37["command"] = self.GButton_37_command

        GLabel_565=tk.Label(root)
        ft = tkFont.Font(family='Times',size=22)
        GLabel_565["font"] = ft
        GLabel_565["fg"] = "#333333"
        GLabel_565["justify"] = "center"
        GLabel_565["text"] = "Sort By:"
        GLabel_565.place(x=80,y=120,width=102,height=32)

        GButton_574=tk.Button(root, highlightbackground="#ffc592")
        GButton_574["bg"] = "#ffc592"
        ft = tkFont.Font(family='Times',size=10)
        GButton_574["font"] = ft
        GButton_574["fg"] = "#000000"
        GButton_574["justify"] = "center"
        GButton_574["text"] = "Surname"
        GButton_574.place(x=60,y=230,width=147,height=36)
        GButton_574["command"] = self.GButton_574_command

        reset_entries=tk.Button(root, highlightbackground="#ff5722")
        reset_entries["bg"] = "#ff5722"
        ft = tkFont.Font(family='Times',size=10)
        reset_entries["font"] = ft
        reset_entries["fg"] = "#000000"
        reset_entries["justify"] = "center"
        reset_entries["text"] = "Reset Entries"
        reset_entries.place(x=60,y=320,width=147,height=36)
        reset_entries["command"] = self.reset_all

    def GButton_96_command(self): # When Add New Contact is clicked
        AddNewAddress.show_window(old_window=self)

    def reset_all(self):
        self.old_items = []
        self.list_box.delete(0,tk.END)
        self.list_box.insert(tk.END, *self.old_items)
        self.list_box.update()


    def GButton_37_command(self): # When sort by first name is clicked
        self.old_items.sort(key=lambda x: x.first_name)
        self.list_box.delete(0,tk.END)
        self.list_box.insert(tk.END, *self.old_items)
        self.list_box.update()


    def GButton_574_command(self): # When sort by surname is clicked
        self.old_items.sort(key=lambda x: x.surname)
        self.list_box.delete(0,tk.END)
        self.list_box.insert(tk.END, *self.old_items)
        self.list_box.update()

    def show_window(items):
        root = tk.Tk()
        app = ListWindow(root, items)
        root.mainloop()


class ContactWindow:
    def __init__(self, root, item, old_window):
        #setting title
        root.title("Contact Details")
        #setting window size
        width=590
        height=470
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        self.old_window = old_window
        self.item = item
        self.root = root

        firstName = tk.StringVar(root, value=item.first_name)
        surName = tk.StringVar(root, value=item.surname)
        address = tk.StringVar(root,value=item.address)
        phone = tk.StringVar(root,value=item.phone_number)
        mobile = tk.StringVar(root,value=item.mobile_number)
        email = tk.StringVar(root,value=item.email_address)

        GLabel_163=tk.Label(root)
        ft = tkFont.Font(family='Times',size=34)
        GLabel_163["font"] = ft
        GLabel_163["fg"] = "#333333"
        GLabel_163["justify"] = "center"
        GLabel_163["text"] = '{}'.format(item.first_name)
        GLabel_163.place(x=170,y=30,width=254,height=36)

        GButton_96=tk.Button(root, highlightbackground="#5fb878")
        GButton_96["bg"] = "#5fb878"
        ft = tkFont.Font(family='Times',size=10)
        GButton_96["font"] = ft
        GButton_96["fg"] = "#000000"
        GButton_96["justify"] = "center"
        GButton_96["text"] = "Update Contact"
        GButton_96.place(x=140,y=380,width=147,height=36)
        GButton_96["command"] = self.update_item

        GLabel_565=tk.Label(root)
        ft = tkFont.Font(family='Times',size=14)
        GLabel_565["font"] = ft
        GLabel_565["fg"] = "#333333"
        GLabel_565["justify"] = "center"
        GLabel_565["text"] = "First Name:"
        GLabel_565.place(x=80,y=100,width=102,height=32)

        GButton_906=tk.Button(root, highlightbackground="#ff5722")
        GButton_906["bg"] = "#ff5722"
        ft = tkFont.Font(family='Times',size=10)
        GButton_906["font"] = ft
        GButton_906["fg"] = "#000000"
        GButton_906["justify"] = "center"
        GButton_906["text"] = "Delete Contact"
        GButton_906.place(x=310,y=380,width=147,height=36)
        GButton_906["command"] = self.delete_item

        GLabel_557=tk.Label(root)
        ft = tkFont.Font(family='Times',size=14)
        GLabel_557["font"] = ft
        GLabel_557["fg"] = "#333333"
        GLabel_557["justify"] = "center"
        GLabel_557["text"] = "Surname:"
        GLabel_557.place(x=90,y=140,width=70,height=25)

        GLabel_412=tk.Label(root)
        ft = tkFont.Font(family='Times',size=14)
        GLabel_412["font"] = ft
        GLabel_412["fg"] = "#333333"
        GLabel_412["justify"] = "center"
        GLabel_412["text"] = "Address:"
        GLabel_412.place(x=90,y=180,width=70,height=25)

    


        GLabel_916=tk.Label(root)
        ft = tkFont.Font(family='Times',size=14)
        GLabel_916["font"] = ft
        GLabel_916["fg"] = "#333333"
        GLabel_916["justify"] = "center"
        GLabel_916["text"] = "Phone:"
        GLabel_916.place(x=90,y=220,width=70,height=25)

        GLabel_701=tk.Label(root)
        ft = tkFont.Font(family='Times',size=14)
        GLabel_701["font"] = ft
        GLabel_701["fg"] = "#333333"
        GLabel_701["justify"] = "center"
        GLabel_701["text"] = "Mobile:"
        GLabel_701.place(x=90,y=260,width=70,height=25)

        GLabel_60=tk.Label(root)
        ft = tkFont.Font(family='Times',size=14)
        GLabel_60["font"] = ft
        GLabel_60["fg"] = "#333333"
        GLabel_60["justify"] = "center"
        GLabel_60["text"] = "Email:"
        GLabel_60.place(x=90,y=300,width=70,height=25)

        

        GLineEdit_273=tk.Entry(root, textvariable=firstName)
        GLineEdit_273["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_273["font"] = ft
        GLineEdit_273["fg"] = "#333333"
        GLineEdit_273["justify"] = "center"
        GLineEdit_273["text"] = '{}'.format(item.first_name)
        GLineEdit_273.place(x=220,y=100,width=270,height=32)

        self.first_name_entry = GLineEdit_273
        

        GLineEdit_272=tk.Entry(root, textvariable=surName)
        GLineEdit_272["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_272["font"] = ft
        GLineEdit_272["fg"] = "#333333"
        GLineEdit_272["justify"] = "center"
        GLineEdit_272["text"] = '{}'.format(item.surname)
        GLineEdit_272.place(x=220,y=140,width=270,height=32)

        self.surname_entry = GLineEdit_272

        GLineEdit_28=tk.Entry(root, textvariable=address)
        GLineEdit_28["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_28["font"] = ft
        GLineEdit_28["fg"] = "#333333"
        GLineEdit_28["justify"] = "center"
        GLineEdit_28["text"] = '{}'.format(item.address)
        GLineEdit_28.place(x=220,y=180,width=270,height=32)

        self.address_entry = GLineEdit_28

        GLineEdit_968=tk.Entry(root, textvariable=phone)
        GLineEdit_968["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_968["font"] = ft
        GLineEdit_968["fg"] = "#333333"
        GLineEdit_968["justify"] = "center"
        GLineEdit_968["text"] = '{}'.format(item.phone_number)
        GLineEdit_968.place(x=220,y=220,width=270,height=32)

        self.phone_entry = GLineEdit_968

        GLineEdit_192=tk.Entry(root, textvariable=mobile)
        GLineEdit_192["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_192["font"] = ft
        GLineEdit_192["fg"] = "#333333"
        GLineEdit_192["justify"] = "center"
        GLineEdit_192["text"] = '{}'.format(item.mobile_number)
        GLineEdit_192.place(x=220,y=260,width=270,height=32)

        self.mobile_entry = GLineEdit_192

        GLineEdit_152=tk.Entry(root, textvariable=email)
        GLineEdit_152["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_152["font"] = ft
        GLineEdit_152["fg"] = "#333333"
        GLineEdit_152["justify"] = "center"
        GLineEdit_152["text"] = '{}'.format(item.email_address)
        GLineEdit_152.place(x=220,y=300,width=270,height=32)
        
        self.email_entry = GLineEdit_152

    def delete_item(self): # method which deletes the current contact
        self.old_window.old_items.remove(self.item)
        self.old_window.list_box.delete(0,tk.END)
        self.old_window.list_box.insert(tk.END, *self.old_window.old_items)
        self.old_window.list_box.update()
        self.root.destroy()


    def update_item(self): # method which updates the current contact
        self.item.first_name = self.first_name_entry.get()
        self.item.surname = self.surname_entry.get()
        self.item.address = self.address_entry.get()
        self.item.phone_number = self.phone_entry.get()
        self.item.mobile_number = self.mobile_entry.get()
        self.item.email_address = self.email_entry.get()
        # self.old_window.old_items.remove(self.item)
        self.old_window.list_box.delete(0,tk.END)
        self.old_window.list_box.insert(tk.END, *self.old_window.old_items)
        self.old_window.list_box.update()
        self.root.destroy()
        
      
    def show_window(item, old_window):
        root = tk.Tk()
        app = ContactWindow(root, item, old_window)
        old_window.root.wait_window(app.root)
        root.mainloop()


class AddNewAddress:
    def __init__(self, root, old_window):
        #setting title
        root.title("Add New Address")
        #setting window size
        width=590
        height=470
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        # saving for later use
        self.old_window = old_window
        self.root = root

        # Used later for retreiving the input from the user
        self.firstName = tk.StringVar(root)
        self.surName = tk.StringVar(root)
        self.address = tk.StringVar(root)
        self.phone = tk.StringVar(root)
        self.mobile = tk.StringVar(root)
        self.email = tk.StringVar(root)

        # Label text
        GLabel_163=tk.Label(root) # Constructing the label
        ft = tkFont.Font(family='Times',size=34) # Construct the font
        GLabel_163["font"] = ft # Setting the font
        GLabel_163["fg"] = "#333333" # Setting the color
        GLabel_163["justify"] = "center" # Setting the justification
        GLabel_163["text"] = "Add New Address" # Setting the text
        GLabel_163.place(x=150,y=30,width=303,height=36) # Setting the position and size

        #Button 
        GButton_96=tk.Button(root, highlightbackground="#5fb878")
        GButton_96["bg"] = "#5fb878"
        ft = tkFont.Font(family='Times',size=10)
        GButton_96["font"] = ft
        GButton_96["fg"] = "#000000"
        GButton_96["justify"] = "center"
        GButton_96["text"] = "Add"
        GButton_96.place(x=140,y=380,width=147,height=36)
        GButton_96["command"] = self.GButton_96_command

        GLabel_565=tk.Label(root)
        ft = tkFont.Font(family='Times',size=14)
        GLabel_565["font"] = ft
        GLabel_565["fg"] = "#333333"
        GLabel_565["justify"] = "left"
        GLabel_565["text"] = "First Name:"
        GLabel_565.place(x=90,y=100,width=102,height=32)

        GButton_906=tk.Button(root, highlightbackground="#ff5722")
        GButton_906["bg"] = "#ff5722"
        ft = tkFont.Font(family='Times',size=10)
        GButton_906["font"] = ft
        GButton_906["fg"] = "#000000"
        GButton_906["justify"] = "center"
        GButton_906["text"] = "Cancel"
        GButton_906.place(x=310,y=380,width=147,height=36)
        GButton_906["command"] = self.GButton_906_command

        GLabel_557=tk.Label(root)
        ft = tkFont.Font(family='Times',size=14)
        GLabel_557["font"] = ft
        GLabel_557["fg"] = "#333333"
        GLabel_557["justify"] = "left"
        GLabel_557["text"] = "Surname:"
        GLabel_557.place(x=90,y=140,width=70,height=25)

        GLabel_412=tk.Label(root)
        ft = tkFont.Font(family='Times',size=14)
        GLabel_412["font"] = ft
        GLabel_412["fg"] = "#333333"
        GLabel_412["justify"] = "left"
        GLabel_412["text"] = "Address:"
        GLabel_412.place(x=90,y=180,width=70,height=25)

        GLabel_916=tk.Label(root)
        ft = tkFont.Font(family='Times',size=14)
        GLabel_916["font"] = ft
        GLabel_916["fg"] = "#333333"
        GLabel_916["justify"] = "left"
        GLabel_916["text"] = "Phone:"
        GLabel_916.place(x=90,y=220,width=70,height=25)

        GLabel_701=tk.Label(root)
        ft = tkFont.Font(family='Times',size=14)
        GLabel_701["font"] = ft
        GLabel_701["fg"] = "#333333"
        GLabel_701["justify"] = "left"
        GLabel_701["text"] = "Mobile:"
        GLabel_701.place(x=90,y=260,width=70,height=25)

        GLabel_60=tk.Label(root)
        ft = tkFont.Font(family='Times',size=14)
        GLabel_60["font"] = ft
        GLabel_60["fg"] = "#333333"
        GLabel_60["justify"] = "left"
        GLabel_60["text"] = "Email:"
        GLabel_60.place(x=90,y=300,width=70,height=25)

        GLineEdit_273=tk.Entry(root, textvariable=self.firstName)
        self.first_name_entry = GLineEdit_273
        GLineEdit_273["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_273["font"] = ft
        GLineEdit_273["fg"] = "#333333"
        GLineEdit_273["justify"] = "center"
        GLineEdit_273["text"] = "First_name_here"
        GLineEdit_273.place(x=220,y=100,width=270,height=32)

        GLineEdit_272=tk.Entry(root, textvariable=self.surName)
        self.surname_entry = GLineEdit_272
        GLineEdit_272["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_272["font"] = ft
        GLineEdit_272["fg"] = "#333333"
        GLineEdit_272["justify"] = "center"
        GLineEdit_272["text"] = "Surname_here"
        GLineEdit_272.place(x=220,y=140,width=270,height=32)

        GLineEdit_28=tk.Entry(root, textvariable=self.address)
        self.address_entry = GLineEdit_28
        GLineEdit_28["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_28["font"] = ft
        GLineEdit_28["fg"] = "#333333"
        GLineEdit_28["justify"] = "center"
        GLineEdit_28["text"] = "Address_here"
        GLineEdit_28.place(x=220,y=180,width=270,height=32)

        GLineEdit_968=tk.Entry(root, textvariable=self.phone)
        self.phone_entry = GLineEdit_968
        GLineEdit_968["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_968["font"] = ft
        GLineEdit_968["fg"] = "#333333"
        GLineEdit_968["justify"] = "center"
        GLineEdit_968["text"] = "Phone_here"
        GLineEdit_968.place(x=220,y=220,width=270,height=32)

        GLineEdit_192=tk.Entry(root, textvariable=self.mobile)
        self.mobile_entry = GLineEdit_192
        GLineEdit_192["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_192["font"] = ft
        GLineEdit_192["fg"] = "#333333"
        GLineEdit_192["justify"] = "center"
        GLineEdit_192["text"] = "Mobile_here"
        GLineEdit_192.place(x=220,y=260,width=270,height=32)

        GLineEdit_152=tk.Entry(root, textvariable=self.email)
        self.email_entry = GLineEdit_152
        GLineEdit_152["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_152["font"] = ft
        GLineEdit_152["fg"] = "#333333"
        GLineEdit_152["justify"] = "center"
        GLineEdit_152["text"] = "Email_here"
        GLineEdit_152.place(x=220,y=300,width=270,height=32)

    def GButton_96_command(self): # Method when Add Button is clicked
        # appending new item into the old list
        self.old_window.old_items.append(Address(self.first_name_entry.get(), self.surname_entry.get(), self.address_entry.get(), self.phone_entry.get(), self.mobile_entry.get(), self.email_entry.get(), ""))
        # Updating the old list by removing all and re-adding
        self.old_window.list_box.delete(0,tk.END)
        self.old_window.list_box.insert(tk.END, *self.old_window.old_items)
        self.old_window.list_box.update()
        #remove this window
        self.root.destroy()


    def GButton_906_command(self):
        self.root.destroy()

    def show_window(old_window):
        root = tk.Tk()
        app = AddNewAddress(root, old_window)
        old_window.root.wait_window(app.root)
        root.mainloop()


# main file

address_book = AddressBook() # create an address book

# add dummy contacts to the address book
address_book.add(Address("John", "Smith", "123 Main Street", "11111", "22222", "email@dot.com", ""))
address_book.add(Address("Jane", "Doe", "456 Second Street", "33333", "44444", "email@dot.com", ""))
address_book.add(Address("John", "Smith", "123 Main Street", "11111", "22222", "email@dot.com", ""))
address_book.add(Address("Jane", "Doe", "456 Second Street", "33333", "44444", "email@dot.com", ""))
address_book.add(Address("John", "Smith", "123 Main Street", "11111", "22222", "email@dot.com", ""))
address_book.add(Address("Jane", "Doe", "456 Second Street", "33333", "44444", "email@dot.com", ""))
address_book.add(Address("John", "Smith", "123 Main Street", "11111", "22222", "email@dot.com", ""))
address_book.add(Address("Jane", "Doe", "456 Second Street", "33333", "44444", "email@dot.com", ""))
address_book.add(Address("John", "Smith", "123 Main Street", "11111", "22222", "email@dot.com", ""))
address_book.add(Address("Jane", "Doe", "456 Second Street", "33333", "44444", "email@dot.com", ""))

# show the main GUI with the items (addresses) in the address book
ListWindow.show_window(items=address_book)
