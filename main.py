import tkinter as tk
class QuizApp:
    def __init__(self, master):
        self.master = master
        
        #Background colour here
        
        self.master.configure(background='PaleGreen2')
        
        #first pages text here
        
        self.master.title("Welcome to Haaziq's Geography Quiz")
        self.name_label = tk.Label(self.master, text="Enter Your Name:", font=("Arial", 16), bg='PaleGreen2', fg='white', padx=20)
        
        #page size setup for the 
        
        self.name_label.grid(row=0, column=0, pady=20, sticky='w')
        self.name_entry = tk.Entry(self.master)
        self.name_entry.grid(row=0, column=1, pady=20)

        #confirm button here
        
        self.confirm_button = tk.Button(self.master, text="Confirm", command=self, bg='green', fg='white')
        self.confirm_button.grid(row=3, column=2, pady=20, padx=20)
root = tk.Tk()
app = QuizApp(root)
root.mainloop()