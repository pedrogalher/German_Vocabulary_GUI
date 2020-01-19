# -*- coding: utf-8 -*-
"""
Created on Thu Jan  2 17:22:53 2020

@author: Home
"""
import pandas as pd
import numpy as np
import os
import random
from tkinter import *
from tkinter import filedialog


class GermanGUI:
    
    """ References:
        https://likegeeks.com/python-gui-examples-tkinter-tutorial/
        https://pythonspot.com/tk-file-dialogs/
        https://python-textbok.readthedocs.io/en/1.0/Introduction_to_GUI_Programming.html
        https://www.geeksforgeeks.org/indexing-and-selecting-data-with-pandas/
        http://effbot.org/
        https://effbot.org/tkinterbook/grid.htm
        https://www.homeandlearn.uk/python-database-form-tabs.html
        https://www.tutorialspoint.com/python/tk_frame.htm
    """

    def __init__(self, master):
        self.master = master
        master.title("Learn German NOW")
        self.label_top = Label(master, text="German Word").grid(row=0, columnspan=2)
        
        # Select File Button
        self.select_file_button = Button(master, text="Select File",
                               command=self.select_file).grid(row=1, columnspan=2)
        
        # Show Spanish word Button
        self.show_es_button = Button(master, text="Next Spanish Word", 
                                     command=self.random_word).grid(row=2, columnspan=2)
       
        # Text associated to Spanish Word
        self.es_text = Text(master, height=5, width=20).grid(row=3, columnspan=2)
        
        # Text associated to German Word
        self.de_entry = Entry(master)
        self.de_entry.delete(0, END)
        self.de_entry.grid(row=5, column=0)
        
        # Check answer Button
        self.check_button = Button(master, text="Check Answer",
                                   command=lambda: self.check_answer(None)).grid(row=5, column=1)  # If the buton is pressed, it means that no key has been pressed, then event=None
        
        self.master.bind('<Return>', self.check_answer)  # Alternatively, check is made pressing the Enter key
        # Close Button
        self.close_button = Button(master, text="Close", command=master.quit).grid(row=10, columnspan=2)
        
        # Counter Words
        self.counter = 0
        self.counter_text = Text(master, height=1, width=4)
        self.counter_text.insert(END, self.counter)
        self.counter_text.tag_configure("center", justify='center')
        self.counter_text.tag_add("center", 1.0, "end")
        self.counter_text.grid(row=6, column=1)
        self.counter_label = Label(master, text="Counter words").grid(row=6, column=0)
        
        #  Counter Success at first try
        self.success = 0
        self.flag = 1  # Will serve to decide whether the solution was given at first try or not
        self.success_text = Text(master, height=1, width=4)
        self.success_text.insert(END, self.success)
        self.success_text.tag_configure("center", justify='center')
        self.success_text.tag_add("center", 1.0, "end")
        self.success_text.grid(row=7, column=1)
        self.success_label=Label(master, text="Correct words at first try").grid(row=7, column=0)
    
        #  Success Rate
        self.success_rate = 0
        self.success_rate_text = Text(master, height=1, width=6)
        self.success_rate_text.insert(END, self.success)
        self.success_rate_text.tag_configure("center", justify='center')
        self.success_rate_text.tag_add("center", 1.0, "end")
        self.success_rate_text.grid(row=8, column=1)
        self.success_rate_label = Label(master, text="Success Ratio").grid(row=8, column=0)
        
        # Timer
        
    
    def select_file(self):
        self.filename = filedialog.askopenfilename(
                initialdir="/", title="Select file",
                filetypes=(("all files", "*.*.*"), ("jpeg files", "*.jpg")))
        self.df = self.load_data()

    def load_data(self):
        df = pd.read_excel(io=self.filename, header=None)
        print("Data loaded succesfully")
        return df

    def random_word(self):
        self.de_entry.delete(0, END)  # Clear previous entry word
        nb_words = self.df.shape[0]
        id_word = random.randint(0, nb_words)
        self.de, self.es = self.select_words(id_word)
        self.es_text.insert(END, self.es)
        self.es_text.config(state=DISABLED)
        self.es_text.tag_configure("center", justify='center')
        self.es_text.tag_add("center", 1.0, "end")
        return nb_words, id_word

    def select_words(self, i):
        """ This method will select a pair of words.
        The input is the excel row of the desired word.
        """
        es = self.df.iat[i, 0]
        de = self.df.iat[i, 1]
        return de, es

    def check_answer(self, event=None):
        answer = self.de_entry.get()
        if answer == self.de:
            print(" Well done!")
            self.es_text.config(state=NORMAL)
            self.es_text.delete(1.0, END)  # Delete the text and wait for next spanish word
            self.de_entry.delete(0,END)  # Delete the previous entry
            self.counter_text.delete(1.0, END)
            self.counter += 1
            self.counter_text.insert(END, self.counter)
            self.counter_text.config(state=NORMAL)
            self.counter_text.tag_configure("center", justify='center')
            self.counter_text.tag_add("center", 1.0, "end")
            self.success_rate_text.delete(1.0, END)
            self.success_rate = (self.success/self.counter)*100
            self.success_rate_text.insert(END, self.success_rate)
            self.success_rate_text.config(state=NORMAL)
            self.success_rate_text.tag_configure("center", justify='center')
            self.success_rate_text.tag_add("center", 1.0, "end")
            
            if self.flag == 1:
                self.success_text.delete(1.0, END)
                self.success +=1
                self.success_text.insert(END, self.success)
                self.success_text.config(state=NORMAL)
                self.success_text.tag_configure("center", justify='center')
                self.success_text.tag_add("center", 1.0, "end")
                
            else:
                self.flag = 1
            
        else:
            print("Try again!")
            self.de_entry.delete(0,END)
            self.de_entry.insert(END, self.de)
            self.flag = 0
    
    
if __name__ == "__main__":
    root = Tk()
    german_app = GermanGUI(root)
    root.mainloop()
