import tkinter as tk
from tkinter import messagebox
import random
import re # Importing the regex module
from emoji_map import emoji_country_dict

class Utils:
    @staticmethod
    def get_random_emoji():
        return random.choice(list(emoji_country_dict.keys()))

class EmojiGame(tk.Tk):
    def __init__(self):
        super().__init__()
        
        # Window Configurations
        self.title("Guess the Country")
        self.geometry("600x600+200+200") 
        self.configure(bg='#FFDAB9')  # Peach color
        
        # Instance Variables
        self.current_emoji = Utils.get_random_emoji()
        
        # Widgets Initialization
        self.init_widgets()
        
    def init_widgets(self):
        self.emoji_label = tk.Label(self, text=self.current_emoji, font=("Arial", 100), bg='#FFDAB9')
        self.emoji_label.pack(pady=20)
        
        self.entry = tk.Entry(self, font=("Arial", 20), width=20)
        self.entry.pack(pady=20)
        
        self.submit_button = tk.Button(self, text="Submit", command=self.check_answer, font=("Arial", 20))
        self.submit_button.pack(pady=20)
        
        self.result_label = tk.Label(self, text="", font=("Arial", 20), bg='#FFDAB9', fg='white')
        self.result_label.pack(pady=20, fill='x')
       
    def check_answer(self):
        user_input = self.entry.get().strip().title()
        if not user_input:
            self.error_handler("You cannot leave it blank!")
            return
        if not re.fullmatch(r'[a-zA-Z-\s\']+', user_input): # allow letters, spaces, hyphens and apostrophes
            self.error_handler("Please enter only letters of the alphabet. [spaces, hyphens, and apostrophe where approriate!]")
            return
        if user_input == emoji_country_dict[self.current_emoji]:
            self.configure(bg='green')
            self.emoji_label.config(bg='green') # makes emoji label green
            self.result_label.config(text=f"{self.current_emoji} represents the country {emoji_country_dict[self.current_emoji]}. Correct!",
                                      bg='green') # added bg='green'
        else:
            self.result_label.config(text="Try again!")
            
    def error_handler(self, error_message):
        messagebox.showerror("Error", error_message)

# Start the game
if __name__ == "__main__":
    app = EmojiGame()
    app.mainloop()

