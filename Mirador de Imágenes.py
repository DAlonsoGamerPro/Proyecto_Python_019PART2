from tkinter import *
from PIL import ImageTk, Image
from tkinter import ttk
from tkinter import filedialog
    
root = Tk()
root.title("Mirador de Imágenes")
root.geometry("500x500")
root.config(bg="turquoise1")

label_planet_image = Label(root,bg="red",highlightthickness=5,borderwidth=2,relief=SOLID)

img_path = ""

def open_file():
    global img_path
    img_path = filedialog.askopenfilename(title="Abrir Archivo",filetypes = [("Archivos de imágenes","*.jpg *.gif *jpeg *.png")])
    print(img_path)
    im = Image.open(img_path)
    img = ImageTk.PhotoImage(im)
    label_planet_image["image"] = img
    img.close()
    
def Operation_rotate():
    global img_path
    im = Image.open(img_path)
    img = ImageTk.PhotoImage(im.rotate(90))
    label_planet_image["image"] = img
    img.close()

btn = Button(root,text="Abrir Imagen",command=open_file)
btn2 = Button(root,text="Rotar Imagen",command=Operation_rotate)
label_credits = Label(root,bg="turquoise1",text="Hecho por Diego Alonso, con la ayuda de BYJU´S Learning y la maestra Ivonne Margarita Pinto Herrera")

label_planet_image.place(relx=0.5,rely=0.5,anchor=CENTER)
btn.place(relx=0.5,rely=0.18,anchor=CENTER)
btn2.place(relx=0.5,rely=0.8,anchor=CENTER)
label_credits.place(relx=0.5,rely=0.98,anchor=CENTER)

root.mainloop()