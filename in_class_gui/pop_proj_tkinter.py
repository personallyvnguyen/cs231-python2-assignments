# pop_proj_tkinter.py
#
# A231 Python 2 Spring 2021
# Credit: 
# - Cabrera, James
# - Nguyen, Van
# - Sim, Kevin
# IN-CLASS 2021-04-15 GUI
#
# Resources used:
# https://www.geeksforgeeks.org/tkinter-application-to-switch-between-different-page-frames/


import sys
import tkinter as tk
from tkinter import ttk
  
 

LARGEFONT = ("Verdana", 20)
FILE_NAME = 'localpops.txt'



class Population_Projection(tk.Tk):
    'GUI to project city population'

    def __init__(self, *args, **kwargs) -> None:
        'Initializes the instance variables'
        tk.Tk.__init__(self, *args, **kwargs)

        container = tk.Frame(self) 
        container.pack(side = "top", fill = "both", expand = True)
  
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)

        self.frames = {} 
  
        for F in (StartPage, Page1, Page2):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row = 0, column = 0, sticky ="nsew")
  
        self.show_frame(StartPage)


    def starting_param(self, city):
        self.frames[Page1].selected_city(city)
        frame = self.frames[Page1]
        frame.tkraise()


    def take_input(self, starting, years):
        self.frames[Page2].input_param(starting, years)
        frame = self.frames[Page2]
        frame.tkraise()


    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()



class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        try:
            self._cities = []

            with open(FILE_NAME, 'r') as f:
                lines = f.readlines()

                for line in lines:
                    data = [value.strip() for value in line.split(',')]
                    self._cities.append((
                        data[0],
                        int(data[1]),
                        int(data[2]),
                        int(data[3]),
                    ))
        except:
            print(
                'Unable to open file \'localpops.txt\'.\n'
                'Please check the file again and run the program again'
            )
            sys.exit()

        label = ttk.Label(self, text ="Cities Available in the Data Set", font = LARGEFONT)
        label.grid(row = 0, column = 4, padx = 10, pady = 10)

        buttons = {}

        for i, city in enumerate(self._cities, 1):
            buttons[i] = ttk.Button(self, text = f'{i} - {city[0]}',
                command = lambda city = city[0]: controller.starting_param(city))
            buttons[i].grid(row = i, column = 1, padx = 10, pady = 10)



class Page1(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.city_name = tk.StringVar()
        self.heading = ttk.Label(self, textvariable = self.city_name, font = LARGEFONT)
        self.heading.grid(row = 0, column = 4, padx = 10, pady = 10)

        button1 = ttk.Button(self, text ="Back",
            command = lambda : controller.show_frame(StartPage))
        button1.grid(row = 6, column = 1, padx = 10, pady = 10)

        button2 = ttk.Button(self, text ="Enter",
            command = lambda : self.take_input())
        button2.grid(row = 6, column = 3, padx = 10, pady = 10)


    def selected_city(self, city):
        self.city_name.set(city)

        self.prompt = ttk.Label(self, text = 'Please input the starting population')
        self.prompt.grid(row = 1, column = 1, padx = 10, pady = 10)

        inValue = tk.StringVar()
        self.starting = tk.Entry(self, textvariable=inValue)
        self.starting.grid(row = 2, column = 1, padx = 10, pady = 10)

        self.prompt2 = ttk.Label(self, text = 'Please input the number of years')
        self.prompt2.grid(row = 3, column = 1, padx = 10, pady = 10)

        inValue2 = tk.StringVar()
        self.years = tk.Entry(self, textvariable=inValue2)
        self.years.grid(row = 4, column = 1, padx = 10, pady = 10)

    def take_input(self):
        starting = int(self.starting.get())
        years = int(self.years.get())

        self.controller.take_input(starting, years)



class Page2(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

    def input_param(self, starting, years):
        print(starting, years)
        self.prompt = ttk.Label(self, text = 'POPULATION CALC')
        self.prompt.grid(row = 1, column = 1, padx = 10, pady = 10)



if __name__ == '__main__':
    app = Population_Projection()
    app.mainloop()