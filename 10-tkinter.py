import tkinter as tk

ventana = tk.Tk()
ventana.title("Informatorio")
ventana.geometry("800x600")
ventana.configure(bg= "#46C4F6")
                  
texto = tk.Label(ventana, text="¡Hola, Bienvenidos!")
texto.pack()
ventana.mainloop()