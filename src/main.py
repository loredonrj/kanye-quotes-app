import tkinter as tk
from tkinter import Label, Button
import requests
from PIL import Image, ImageTk
import io
import base64

class KanyeQuotesApp:

    #initializing a graphical user interface (GUI) application using a TKinter window object from the Tkinter library
    def __init__(self, gui): # gui is the name we chose for the parameter expected to be found by the Tk() Class during the instanciation of the Tkinter window object tk.Tk() for the Tkinter window instance (object ie . It is the main application window.
        
        self.gui = gui ## the gui instance (that will be created when the ```gui = tk.Tk()`` command will be invoked in the main function) stores the TKinter window object into it'self' (It's how the object refers to 'it'self) so it can be used it throughout the KanyeQuotesApp Class. 
        self.gui.title("Kanye Quotes") ## sets the window title
        self.gui.geometry("800x600") ## sets the window size in px
        
        self.gui.configure(bg="#FFE4C4") # Sets main window's background color to Peach
        
        self.quote_label = Label( # Creates a label displays a text to the user
            gui,
            text="Clique sur Kanye pour recevoir sa sagesse!",
            wraplength=600, ## wraps (or pack) the text within a width of 600 pixels, making it more readable
            font=("Helvetica", 24, "bold"),
            bg="#FFE4C4",
            fg="#4A4A4A"
        )
        
        self.quote_label.pack(pady=50) # the pack method positions the Label in the GUI by adding 50px of padding(space) above and below it
        
        # Load the image
        self.kanye_image = Image.open("img/kanye.png")
        self.kanye_image = self.kanye_image.resize((100, 100))
        self.kanye_photo = ImageTk.PhotoImage(self.kanye_image)

        self.button = Button( # Creates a button class (or widget) with a Kanye emoji as its label. Users click it to get a quote(you can replace the emoji with an actual image)
            gui,
            image=self.kanye_photo, 
            ## Button styling
            font=("Arial", 40), ### a large font size
            bg="#FFE4C4",
            borderwidth=0, ## no border.
            activebackground="#FFE4C4",
            ## Button behaviour
            command=self.get_quote # when the button is clicked, the get_quote method will be called, it fetches and displays the quote 
        )
 
        self.button.pack(pady=20) # the pack method positions the Button in the GUI by adding 20px of padding(space) above and below it

    def get_quote(self):   
        try:
            # Get quote from API
            response = requests.get("https://api.kanye.rest")
            quote = response.json()["quote"]
            
            # Update label with new quote, replacing the "Click Kanye for wisdom!" label with the quote
            self.quote_label.config(text=f'"{quote}"')
        except Exception as e:
            self.quote_label.config(text="Failed to get quote. Try again!")

if __name__ == "__main__":
    gui = tk.Tk() # Creates the main window object (the gui). What happens here is defined in the def __init__(self, gui) initialization of the Main Window (the gui)
    app = KanyeQuotesApp(gui) # The gui object is passed to the KanyeQuotesApp class as an argument. The KanyeQuotesApp class is then instantiated as an object called app. 
    gui.mainloop()