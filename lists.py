from tkinter import *
root=Tk()

root.title("Multidimensal Array")
root.geometry("1000x1000")

lbl = Label(root)
array_1d = ["Tompson","Tintin","Nester"]
print(array_1d[2])

array_2d = [["Tompson","A"],["Tintin","B"],["Nester","C"]]
print(array_2d[2][0])

array_3d = [[["Tompson","A","Excellent"],["Tintin","B","Very Good"],["Nester","C","Good"]]]
print(array_3d[0][2][0])

root.mainloop()