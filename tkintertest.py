import tkinter as tk
from tkinter import ttk
import networkx as nx
from networkx.algorithms import community, cuts

G = nx.karate_club_graph()

comp = community.girvan_newman(G)
result = tuple(sorted(c) for c in next(comp))

pagerank = nx.pagerank(G)

pagerankOptionsList = list([i for i in pagerank.values()])
print(pagerankOptionsList)

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Tabbed App")
        self.geometry("300x200")

        # Create tab control
        tab_control = ttk.Notebook(self)

        # Create tabs
        tab1 = ttk.Frame(tab_control)
        tab2 = ttk.Frame(tab_control)

        # Add tabs to control 
        tab_control.add(tab1, text='Page Rank')
        tab_control.add(tab2, text='Conductance')

        
        # Create button and dropdown for tab 1
        self.button1 = tk.Button(tab1, text='Show Dropdown', command=self.show_dropdown1)
        self.button1.pack(pady=10)
        i =1
        k = 0
        lent = len(pagerankOptionsList)
        for j in range(len(pagerankOptionsList)):
            self.dropdown1 = tk.OptionMenu(tab1, tk.StringVar(), pagerankOptionsList[k],pagerankOptionsList[k+i],pagerankOptionsList[k+i])
            if i == lent:
                break
            else:
                i = i+1

        self.dropdown1.pack()
        self.dropdown1.pack_forget()

        # Create button and dropdown for tab 2
        self.button2 = tk.Button(tab2, text='Show Dropdown', command=self.show_dropdown2)
        self.button2.pack(pady=10)
        self.dropdown2 = tk.OptionMenu(tab2, tk.StringVar(), 'Option 1', 'Option 2', 'Option 3', 'Option 4', 'Option 5')
        self.dropdown2.pack()
        self.dropdown2.pack_forget()

        # Pack tab control
        tab_control.pack(expand=1, fill="both")

    def show_dropdown1(self):
        self.dropdown1.pack()

    def show_dropdown2(self):
        self.dropdown2.pack()


app = App()
app.mainloop()
