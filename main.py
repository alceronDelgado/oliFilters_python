import tkinter as tk
from tkinter import messagebox

def calcular():
    
    aceite = 80000;
    filtroAceite = 20000;
    manoObra = 30000;
    filtroAire = 12000;
    mensaje = ""
    total = 0
    kilometraje = 0
    
    try:
        #Get data
        kilometraje = int(kilometrajeInput.get())
        
        if (kilometraje > 0):
            if (kilometraje < 5000):
                mensaje = "su carro no necesita cambio de aceite"
                
            if ((kilometraje >= 5000) and (kilometraje <= 9999)):
                mensaje = "aceite y mano de obra"
                total = aceite + manoObra
                
            if ( (kilometraje >= 10000) and (kilometraje <= 14999)):
                mensaje = "aceite, filtro de aceite y mano de obra";
                total = aceite + filtroAceite + manoObra
                
            if ((kilometraje >= 15000)):
                mensaje = "cubre todos los servicios";
                total = aceite +    filtroAceite +     manoObra +  filtroAire;
                
    
    except ValueError:
        messagebox.showinfo("info","Kilometraje ingresado incorrecto")
        
    #Devuelvo el valor a la vista del aplicativo
    label2.config(text=mensaje)
    label3.config(text=total)

view = tk.Tk()

view.geometry('1057x779')
view.config(background="#FFF")
view.title("Oli Filters")

# Agregar imagen

bg_img = tk.PhotoImage(file="src/img/bodyImage.png")

fondo = tk.Label(view,image=bg_img)
fondo.pack()

#Segunda view para colocar dentro de los input
frame = tk.Frame(view,bg="gray")
frame.place(relx=0.27,rely=0.3,relheight=.3,relwidth=.5)

# Input de texto
text = tk.Label(frame, text="Cotice su cita",font="Helevetica",pady=10,padx=0,background="gray")
text.pack()

# Input de texto 2
text2 = tk.Label(frame,text="Digite cantidad de kilometraje que tiene su vehiculo", font="Helevetica")
text2.place(x = 0, y = 50,relwidth=1)

# Inputo de entrada de datos
kilometrajeInput = tk.Entry(frame,width=30)
#El método place funciona igual que el método pack
kilometrajeInput.place(x=0,y=75)

#Botton
button = tk.Button(frame,text="Calcular",background="black",fg="white",height=1,border=3, command=calcular)
button.place(x=145,y=100)


#Mostrar resultado = Dejamos el text en blanco para poder retornar el valor y mostrarlo en la app
label2 = tk.Label(frame,width=30,text=" ")
label2.place(x=80,y=150)

#Mostrar total 
label3 = tk.Label(frame,width=30,text= " ")
label3.place(x=80,y=170)

# Evitar que el usuario cambie la dimensión de la apliación
#agregar el label a la ventana
view.resizable("false","false")
view.mainloop()