from tkinter import*
from PIL import Image, ImageTk
import requests
import os
from datetime import datetime
from config import myapi

root = Tk()
root.title("WEATHER APP")
root.geometry("900x600")
root.resizable(False, False)            # Disable both horizontal and vertical resizing
root.wm_iconbitmap("weather_icon.ico")
root.config(bg = "#04FFE1")




def show_data():
    user_api = myapi
    location = city.get()

    complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q=" + location + "&appid=" + user_api

    api_link = requests.get(complete_api_link)
    api_data = api_link.json()
    
    temp_city = ((api_data['main']['temp']) - 273.15)
    weather_desc = api_data['weather'][0]['description']
    hmdt = api_data['main']['humidity']
    wind_spd = api_data['wind']['speed']
    pressure = api_data['main']['pressure']
    date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

    result1 = date_time
    result_date.config(text = result1)
    
    result2 = ("{:.2f} ° C".format(temp_city))
    result_temp.config(text = result2)

    result3 = wind_spd
    result_wind.config(text = str(result3) + "Km/h")

    result4 = hmdt
    result_humidity.config(text = str(result4) + "%")

    result5 = weather_desc.title()
    result_desc.config(text = result5)

    result6 = pressure
    result_pressure.config(text = result6)


head = Label(root, text = "WEATHER APP", font = "Verdana 30 bold underline", bg = "#04FFE1", fg = "purple")
head.pack()
    
subhead = Label(root, text = "Get your weather details on single click.", font = "Georgia 18 bold", bg = "#04FFE1", fg = "green")
subhead.pack(anchor = "w", padx = 20, pady = 5)

canva = Canvas(root, height = 100, width = 300, border = 5, bg = "grey")
canva.pack(anchor = "nw", padx = 20, pady = 20)

city = StringVar()
city_input = Entry(canva, textvariable = city, font = "arial 22 bold")
city_input.pack(anchor = W, side = LEFT, padx = 10, pady = 10)


search = Button(canva, text = "Search", font = "arial 15 bold", command = show_data, bg = "#F8ED03")
search.pack(side = LEFT, padx = 10, pady = 10)


result_date = Label(root, text = "", font = "arial 22 bold",  bg = "#04FFE1")
result_date.pack(anchor = "nw", padx = 25, pady = 2)

new_width = 275
new_height = 275

image_path = "C:\\All Data\\Professional work\\CS Project\\API Programs\\Weather app using tkinter\\img_for_apk.jpg"
img_pil = Image.open(image_path)
resized_img = img_pil.resize((new_width, new_height))
img = ImageTk.PhotoImage(resized_img)
img_labe = Label(image = img, border = 5, bg = "red", relief = SUNKEN)                     
img_labe.pack(anchor = "nw", side = LEFT, padx = 30, pady = 5)


result_temp = Label(root, text="", font = "arial 30 bold", bg = "#04FFE1",  fg = "orange")
result_temp.pack(anchor = "nw", pady = 20)


canva2 = Canvas(root, height = 100, width = 400, bg = "#069CFD")
canva2.pack(anchor = "sw")

frame1 = Frame(canva2, bg = "#069CFD")
frame1.pack(anchor = "nw", side = LEFT, padx = 10, pady = 10)
text1 = Label(frame1, text = "Wind", font = "Helvetica 15 bold underline", fg = "white", bg = "#069CFD",)
text1.pack(padx = 5, pady = 10)

result_wind = Label(frame1, text="", font = "arial 15 bold", bg = "#069CFD")
result_wind.pack()

frame2 = Frame(canva2, bg = "#069CFD")
frame2.pack(side = LEFT, padx = 10, pady = 10)
text2 = Label(frame2, text = "Humidity", font = "Helvetica 15 bold underline", fg = "white", bg = "#069CFD",)
text2.pack(padx = 5, pady = 10)

result_humidity = Label(frame2, text="", font = "arial 15 bold", bg = "#069CFD")
result_humidity.pack()

frame3 = Frame(canva2, bg = "#069CFD")
frame3.pack(side = LEFT, padx = 10, pady = 10)
text3 = Label(frame3, text = "Pressure", font = "Helvetica 15 bold underline", fg = "white", bg = "#069CFD",)
text3.pack(padx = 5, pady = 10)

result_pressure = Label(frame3, text="", font = "arial 15 bold", bg = "#069CFD")
result_pressure.pack()

frame4 = Frame(canva2, bg = "#069CFD")
frame4.pack(side = LEFT, padx = 10, pady = 10)
text4 = Label(frame4, text = "Description", font = "Helvetica 15 bold underline", fg = "white", bg = "#069CFD",)
text4.pack(padx = 5, pady = 10)

result_desc = Label(frame4, text="", font = "arial 15 bold", bg = "#069CFD")
result_desc.pack()




root.mainloop()
