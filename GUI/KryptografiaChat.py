import customtkinter
import secrets

class ChatApplication:
    def __init__(self, appearance_mode, color_theme):
        self.username = secrets.token_hex(30)
        self.appearance = appearance_mode
        self.theme = color_theme
        customtkinter.set_appearance_mode(self.appearance)
        customtkinter.set_default_color_theme(self.theme)
        customtkinter.set_window_scaling(2.0)
        self.root = customtkinter.CTk()
        self.root.geometry("500x350")
        self.root.title("Kryptografia-Chat")

        self.usern = 1

        self.frame = customtkinter.CTkFrame(master=self.root)
        self.frame.pack(pady=20, padx=60, fill="both", expand=True)

        self.label = customtkinter.CTkLabel(master=self.frame, text="Secured Using Standardized Cryptographic Algorithms")
        self.label.pack(pady=20, padx=10)
        self.label.place(relx=0.5, rely=0.95, anchor='c')

        self.nlabel = customtkinter.CTkLabel(master=self.frame, text="Number of users in group:   " + str(self.usern))
        self.nlabel.pack(pady=20, padx=10)
        self.nlabel.place(relx=0.15, rely=0.05, anchor='c')

        self.userlabel = customtkinter.CTkLabel(master=self.frame, text="Signature: " + self.username)
        self.userlabel.pack(pady=20, padx=10)
        self.userlabel.place(relx=0.5, rely=0.85, anchor='c')

        self.entry1 = customtkinter.CTkEntry(master=self.frame, width=600, height=40, placeholder_text="Type Message...")
        self.entry1.pack(pady=80, padx=10)
        self.entry1.place(relx=0.5, rely=0.9, anchor='c')


        self.chatframe = customtkinter.CTkFrame(master=self.frame, width=800, height=400)
        self.chatframe.pack(pady=150, padx=100, fill="both", expand=True)
        self.chatframe.place(relx=0.5, rely=0.5, anchor='c')

        self.button = customtkinter.CTkButton(master=self.frame, width=100, height=40, text="Send MSG", command=self.MSG_sent)
        self.button.pack(pady=80, padx=400)
        self.button.place(relx=0.9, rely=0.9, anchor='c')

        self.button2 = customtkinter.CTkButton(master=self.frame, width=100, height=40, text="Connect", command=self.connectWIN)
        self.button2.pack(pady=80, padx=400)
        self.button2.place(relx=0.9, rely=0.1, anchor='c')

        self.buttonCopy = customtkinter.CTkButton(master=self.frame, width=120, height=40, text="Copy Signature")
        self.buttonCopy.pack(pady=80, padx=400)
        self.buttonCopy.place(relx=0.135, rely=0.1, anchor='c')


    def MSG_sent(self):
        self.entry1.delete(0, 10000)
    
    def chng_username(self):
        self.entryuser5.delete(0, 10000)
    
    def connectWIN(self):
        root2 = customtkinter.CTkToplevel()
        root2.geometry("400x180")
        root2.title("Connect to Users")
        root2.wm_attributes("-topmost", True)
        frame5 = customtkinter.CTkFrame(master=root2)
        frame5.pack(pady=20, padx=60, fill="both", expand=True)
        
        button5 = customtkinter.CTkButton(master=frame5, width=100, height=40, text="Connect")
        button5.pack(pady=80, padx=400)
        button5.place(relx=0.9, rely=0.1, anchor='c')

        entrysign = customtkinter.CTkEntry(master=frame5, width=600, height=40, placeholder_text="Enter or Paste Digital Signature...")
        entrysign.pack(pady=80, padx=10)
        entrysign.place(relx=0.5, rely=0.5, anchor='c')

        self.entryuser5 = customtkinter.CTkEntry(master=frame5, width=180, height=40, placeholder_text="Enter your display username")
        self.entryuser5.pack(pady=80, padx=100)
        self.entryuser5.place(relx=0.2, rely=0.1, anchor='c')

        button6 = customtkinter.CTkButton(master=frame5, width=80, height=40, text="Set", command=self.chng_username)
        button6.pack(pady=80, padx=400)
        button6.place(relx=0.4, rely=0.1, anchor='c')



    def main(self):

        
        self.root.mainloop()



App = ChatApplication("dark", "dark-blue")

App.main()


