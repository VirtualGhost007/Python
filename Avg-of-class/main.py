import tkinter as tk

window = tk.Tk()
window.title("Avg Marks of Class Calculator")
window.minsize(width=400, height=400)
# label = tk.(text="Enter a number")
# label.pack()
window.mainloop()

den = 0
num = 0
while True:
    try:
        number = float(input("Enter a number: "))
        num += number
        den += 1
    except ValueError:
        print(num / den)
        break
