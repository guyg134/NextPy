import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

class FirstGUI:
    def __init__(self, master):
        self.master = master
        master.title("The best GUI in the world")

        # Create a label and buttons
        self.label = tk.Label(master, text="Click on the button to see good looking sigit:")
        self.label.pack()

        # Create a button that will open an image
        self.greet_button = tk.Button(master, text="Picture", command=self.open_image)
        self.greet_button.pack()

        # Create a button that will close the window
        self.close_button = tk.Button(master, text="Close", command=master.quit)
        self.close_button.pack()

        # Create a label that will display the image
        self.image_label = tk.Label(master)  # This label will display the image
        self.image_label.pack()

    def open_image(self):
        """
        This function opens a picture of sigit
        """
        image_path = "sides_quests\\exc6_side\\sigitlogo.png"
        if image_path:  # Check if a file was selected
            image = Image.open(image_path)
            photo = ImageTk.PhotoImage(image)
            self.image_label.config(image=photo)
            self.image_label.image = photo
            print("Image loaded successfully!")

def main():
    root = tk.Tk()
    my_gui = FirstGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()