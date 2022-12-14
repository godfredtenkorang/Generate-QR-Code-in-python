import qrcode
from tkinter import *
from tkinter import messagebox

gt = Tk()
gt.title("QR Code Generator")
gt.geometry("700x700")
gt.config(bg="SteelBlue3")


def generateCode():
    qr = qrcode.QRCode(version=size.get(), box_size=10, border=5)
    qr.add_data(text.get())
    qr.make(fit=True)
    img = qr.make_image()
    fileDirect = loc.get() + '/' + name.get()
    img.save(f"{fileDirect}.png")
    messagebox.showinfo("DataFlair QR Code Generator", "QR Code is saved successfully!")


headingFrame = Frame(gt, bg="azure", bd=5)
headingFrame.place(relx=0.15, rely=0.05, relwidth=0.7, relheight=0.1)
headingLabel = Label(headingFrame, text="Generate GR Code with DataFlair", bg="black", font=("Times", 20, "bold"))
headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

Frame1 = Frame(gt, bg="SteelBlue3")
Frame1.place(relx=0.1, rely=0.15, relwidth=0.7, relheight=0.3)

label1 = Label(Frame1, text="Enter the text/URL: ", bg="SteelBlue3", fg="azure", font=("Courier", 13, "bold"))
label1.place(relx=0.05, rely=0.2, relheight=0.08)

text = Entry(Frame1, font=("Century", 12))
text.place(relx=0.05, rely=0.4, relwidth=1, relheight=0.2)

Frame2 = Frame(gt, bg="SteelBlue3")
Frame2.place(relx=0.1, rely=0.35, relwidth=0.7, relheight=0.3)

label2 = Label(Frame2, text="Enter the location to save the QR Code: ", bg="SteelBlue3", fg="azure", font=("Courier", 13
                                                                                                           , "bold"))
label2.place(relx=0.05, rely=0.2, relheight=0.08)

loc = Entry(Frame2, font=("Century", 12))
loc.place(relx=0.05, rely=0.4, relwidth=1, relheight=0.2)

Frame3 = Frame(gt, bg="SteelBlue3")
Frame3.place(relx=0.1, rely=0.55, relwidth=0.7, relheight=0.3)

label3 = Label(Frame3, text="Enter the name of the QR Code: ", bg="SteelBlue3", fg="azure",
               font=("Courier", 13, "bold"))
label3.place(relx=0.05, rely=0.2, relheight=0.08)

name = Entry(Frame3, font=("Century", 12))
name.place(relx=0.05, rely=0.4, relwidth=1, relheight=0.2)

Frame4 = Frame(gt, bg="SteelBlue3")
Frame4.place(relx=0.1, rely=0.75, relwidth=0.7, relheight=0.2)

label4 = Label(Frame4, text="Enter the size from 1 to 40 with 1 being 21x21: ", bg="SteelBlue3", fg="azure", font=
("Courier", 13, "bold"))
label4.place(relx=0.05, rely=0.2, relheight=0.08)

size = Entry(Frame4, font=("Century", 12))
size.place(relx=0.05, rely=0.4, relwidth=0.5, relheight=0.2)

button = Button(gt, text="Generate Code", font=("Courier", 15, "normal"), command=generateCode)
button.place(relx=0.35, rely=0.9, relwidth=0.25, relheight=0.05)

gt.mainloop()
