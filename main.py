from turtle import width
import prs
import tkinter as tk

class Main(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)        
        # dedclare widgets
        self.result = tk.Label(self, text='Flames By Jon Clyde Dagaang')
        self.nameEntry1 = tk.Entry(self, width=26)
        self.nameEntry2 = tk.Entry(self, width=26)
        self.submitBtn = tk.Button(self, text='Submit', command=self.submit)

        # Grid the declared widgets
        self.result.pack()
        self.nameEntry1.pack()
        self.nameEntry2.pack()
        self.submitBtn.pack(ipadx=56)

    def submit(self):
        if self.nameEntry1.get() == '' or self.nameEntry2.get() == '':
            self.result['text'] = 'FILL THE ENTRIES!!!'
        else:
            output = prs.parse(self.nameEntry1.get(), self.nameEntry2.get())
            self.nameEntry1.delete(0, tk.END)
            self.nameEntry2.delete(0, tk.END)
            self.result['text'] = output


app = Main()
app.title('Flames')
app.geometry('250x100')
app.resizable(False, False)
app.mainloop()
