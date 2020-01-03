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
    """

    def __init__(self, master):
        self.master = master
        master.title("Learn German NOW")
        self.label_top = Label(master, text="German Word")
        self.label_top.pack()
        # Select File Button
        self.select_file_button = Button(master, text="Select File",
                               command=self.select_file)
        self.select_file_button.pack()
        # Show Spanish word Button
        self.show_es_button = Button(master, text="Next Spanish Word", 
                                     command=self.random_word)
        self.show_es_button.pack()
        # Text associated to Spanish Word
        self.es_text = Text(master, height=5, width=20)
        self.es_text.pack()
        # Text associated to German Word
        self.de_entry = Entry(master)
        self.de_entry.delete(0,END)
        self.de_entry.pack()
        # Check answer Button
        self.check_button = Button(master, text="Check Answer",
                                   command=lambda: self.check_answer(
                                           self.de_entry.get()))
        self.check_button.pack()
        # Close Button
        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.pack()
        # Counter Words
        self.counter = 0
        #  Counter Success at first try
        self.success = 0
        #  Success Rate
        self.success_rate = 0
        
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
        return nb_words, id_word

    def select_words(self, i):
        """ This method will select a pair of words.
        The input is the excel row of the desired word.
        """
        es = self.df.iat[i, 0]
        de = self.df.iat[i, 1]
        return de, es

    def check_answer(self, answer):
        if answer == self.de:
            print(" Well done!")
            self.es_text.config(state=NORMAL)
            self.es_text.delete(1.0, END)
            self.de_entry.delete(0,END)
        else:
            print("Try again!")
            self.de_entry.delete(0,END)
            self.de_entry.insert(END,self.de)
    
    
if __name__ == "__main__":
    root = Tk()
    german_app = GermanGUI(root)
    root.mainloop()
