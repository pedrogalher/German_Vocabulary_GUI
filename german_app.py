# -*- coding: utf-8 -*-
"""
Created on Thu Jan  2 17:22:53 2020

@author: Home
"""
import pandas as pd
import numpy as np
import os
from tkinter import *
from tkinter import filedialog


class GermanGUI:
    
    """ References:
        https://likegeeks.com/python-gui-examples-tkinter-tutorial/
        https://pythonspot.com/tk-file-dialogs/
        https://python-textbok.readthedocs.io/en/1.0/Introduction_to_GUI_Programming.html
    """
        
    def __init__(self, master):
        self.master = master
        master.title("Learn German NOW")
        self.label_top = Label(master, text="German Word")
        self.label_top.pack()
        self.select_file_button = Button(master, text="Select File",
                               command=self.select_file)
        self.select_file_button.pack()
        self.load_data_button = Button(master, text="Load Data",
                                       command=self.load_data)
        self.load_data_button.pack()
        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.pack()

    def select_file(self):
        self.filename = filedialog.askopenfilename(
                initialdir="/", title="Select file",
                filetypes=(("all files", "*.*.*"), ("jpeg files", "*.jpg")))

    def load_data(self):
        self.df = pd.read_excel(io=self.filename, header=None)
        print("Data loaded succesfully")
        return self.df

    def random_word(self):
        nb_words = self.df.shape[0]
        return nb_words

    def select_words(self, i):
        """ This method will select a pair of words.
        The input is the excel row of the desired word.
        """
    

     
root = Tk()
german_app = GermanGUI(root)
#nb_words = german_app.random_word()
root.mainloop()
