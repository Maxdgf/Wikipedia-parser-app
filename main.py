from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter as tk
from tkinter import filedialog
from tkinter import scrolledtext
import random
import wikipedia

class App():
    def __init__(self):
        super().__init__()

        array_of_colors = [
            "green",
            "yellow",
            "red",
            "magenta",
            "violet",
            "cyan",
            "white",
            "gold",
            "brown",
            "gray",
            "silver"
        ]

        listValues = [
            "ru",
            "eng"
        ]

        randomColor = random.choice(array_of_colors)
        randomColor2 = random.choice(array_of_colors)

        window = Tk()
        window.title("app")
        window.geometry("500x500")
        window.configure(background=randomColor)

        Label(window, text="Wikipedia parser", font=("Verdana", 15), bg=randomColor2).pack() 
         
        def closeWindow():
        	window.destroy()
        	
        Button(window, text="exit", bg="red", width=2, command=closeWindow).place(x=0, y=0)
        
        def getSummary():
        	try:
        		languageValue = list.get()
        		summaryValue = Summary.get()
        		wikipedia.set_lang(languageValue)
        		answerValue = wikipedia.				summary(summaryValue)
        		resultField.insert(tk.END, answerValue)
        	except:
        		#errorData.configure(text="errors: extraction process\nfailed!")
        		print("connection error")
        		messagebox.showinfo("Error detected", "Extraction process failed!\n Please chek summary data,\n language data\n and your internet connection.")
        	
        def clearAnswerField():
        	resultField.delete("1.0", "end")
        	
        def saveSummaryTxt():
        	content = resultField.get("1.0", "end")
        	file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("TXT files", "*.txt")])
        	if file_path:
        		with open(file_path, "w", encoding="utf-8") as file:
        			file.write(content)	
        	
        list = ttk.Combobox(window, values=listValues)
        list.set("language")
        list.pack(pady=60)
        Label(window, text="input summary:", bg=randomColor2).pack()
        Summary = Entry(window, width=40)
        Summary.pack(pady=50)
        Button(window, text="get\nsummary", bg="yellow", width=10, command=getSummary).pack()
        Button(window, text="save txt", bg="orange", width=10, command=saveSummaryTxt).pack()
        Button(window, text="clear all", bg="maroon", width=10, command=clearAnswerField).pack()
        #errorData = Label(window, text="errors: none").pack(pady=20)
        Button(window, text="copy result", bg="light green", width=10).pack()
        resultField = scrolledtext.ScrolledText(window, width=300, height=500)
        resultField.pack(pady=100)

        window.mainloop()
if __name__ == "__main__":
    root = App()	
