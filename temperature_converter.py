import tkinter as tk
root = tk.Tk()
root.configure(background="Sky Blue")
root.title("Temperature Converter")
root.geometry("775x300")
#Functions
def convert():
	ture=int(cel1.get())	
	ter=(ture*9/5)+32
	fahren1.delete(0,10)
	fahren1.insert(0,ter)

def convert1():
	ot=int(fahren3.get())
	do=(ot-32)*5/9
	cel3.delete(0,10)
	cel3.insert(0,do)
	

#Label for App
temp=tk.Label(root, text="TEMPERATURE CONVERTER", font=("courier", "39"), bg='white', fg="black").grid(row=0, column=1)

#Labels With Entry Boxes 
cel=tk.Label(root, text="CELSIUS", font=("courier", "10"), bg='white', fg="black").grid(row=2, column=0)
cel1=tk.Entry(root,font=("courier", "10"), bg='white', fg="black")
cel1.grid(row=3, column=0)
ce=tk.Label(root, bg="Sky Blue").grid(row=1, column=0)
fahren=tk.Label(root, text="FAHRENHEIT", font=("courier", "10"), bg='white', fg="black").grid(row=2, column=2)
fahren1=tk.Entry(root, font=("courier", "10"), bg='white', fg="black")
fahren1.grid(row=3, column=2)
fah=tk.Label(root, bg="Sky Blue").grid(row=1, column=2)

fahren2=tk.Label(root, text="FAHRENHEIT", font=("courier", "10"), bg='white', fg="black").grid(row=6, column=0)
fahren3=tk.Entry(root, font=("courier", "10"), bg='white', fg="black")
fahren3.grid(row=7, column=0)
fahren4=tk.Label(font=("courier", "10"), bg='white', fg="black").grid(row=7, column=0)
cel2=tk.Label(root, text="CELSIUS", font=("courier", "10"), bg='white', fg="black").grid(row=6, column=2)
cel3=tk.Entry(root,font=("courier", "10"), bg='white', fg="black")
cel3.grid(row=7, column=2)
ce14=tk.Label(root, bg="Sky Blue").grid(row=5, column=3)


#Buttons 
btn=tk.Button(root, text="Convert Temperature", command=convert).grid(row=3, column=1)
btn1=tk.Button(root, text="Convert Temperature", command=convert1).grid(row=7, column=1)
root.mainloop()



