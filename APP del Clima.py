from tkinter import *
import requests


# 2ee785b50ab528b432fb97abf38d25ea
# api.openweathermap.org/data/2.5/weather?q={city name}&appid={your api key}

#Funcion para mostrar respuestas

def mostrar(clima):
    try:
        nombre_ciudad = clima["name"]
        desc = clima["weather"][0]["description"]
        temp = clima["main"]["temp"]
        ciudad["text"] = nombre_ciudad
        temperatura["text"] = str(int(temp)) + "°C"
        descripcion["text"] = desc
    except:
        ciudad["text"] = "ERROR!Intenta Nuevamente"
        temperatura["text"] = ""
        descripcion["text"] = ""
# Funcion para el llamado de la API

def clima_JSON(ciudad):
    try:
        API_Key = "2ee785b50ab528b432fb97abf38d25ea"
        URL = "https://api.openweathermap.org/data/2.5/weather"
        parametros = {"APPID": API_Key, "q": ciudad, "units": "metric", "lang": "es"}
        respuesta = requests.get(URL, params = parametros)
        clima = respuesta.json()
        mostrar(clima)

    except:
        print("Error")

# Intefaz del programa
# Ventana
ventana = Tk()
ventana.geometry("400x500")
ventana.config(bg="black")
ventana.title('****- App del clima -****')


# Entrada de texto
text_ciudad = Entry(ventana, font=("Arial", 20, "normal"), justify="center")
text_ciudad.pack(padx=30, pady=30)

# Boton
obtener_clima = Button(ventana, text="Obtener Clima", font=("Arial", 18, "normal"),command=lambda: clima_JSON(text_ciudad.get()))
obtener_clima.pack()

# Etiqueta para mostrar el Clima
ciudad = Label(font=("Arial", 20, "normal"))
ciudad.pack(padx=20, pady=20)

temperatura = Label(font=("Arial", 50, "normal"))
temperatura.pack(padx=10, pady=10)

descripcion = Label(font=("Arial", 20, "normal"))
descripcion.pack(padx=10, pady=10)

ventana.mainloop()
