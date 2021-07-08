from tkinter import *
from tkinter import messagebox
from configparser import ConfigParser
from PIL import ImageTk, Image
import requests

url='https://api.openweathermap.org/data/2.5/weather?q={}&appid={}'

config_file="config.ini"
config=ConfigParser()
config.read(config_file)
api_key=config['api_key']['key']
print(api_key)

def getweather(city):
    result = requests.get(url.format(city,api_key))
    if result:
        json=result.json()
        city = json['name']
        country=json['sys']['country']
        temp_kelvin=json['main']['temp']
        temp_celsius=temp_kelvin-273.15
        temp_faranheit=(temp_kelvin)*9/5+32
        icon=json['weather'][0]['icon']
        weather= json['weather'][0]['main']
        final=(city,country,temp_celsius,temp_faranheit,icon,weather)
        return final
    else:
        return None

def target():

    pass


def search():
   
    city=city_text.get()
    weather=getweather(city)
    if weather:
        location_lb['text']='{}, {}'.format(weather[0],weather[1])
        print(weather[4])
        #image['bitmap']= 'Python/{}.png'.format(weather[4])
        #image[''] = ImageTk.PhotoImage("01d.png")
        #imglabel = Label(app, image=img).grid(row=1, column=1)
        img = Image.open(r'C:\Users\admin\Documents\Python\{}.png'.format(weather[4]))
        
        
        #img= img.resize(150,150)
        #img= ImageTk.PhotoImage(img)
        img.show()
        temp_lb['text'] = '{:.2f}c°,   {:.2f}f°'.format(weather[2],weather[3])
        weather_lb['text']= weather[5]
    else:
        messagebox.showerror('Error','Cannot find city {}'.format(city))


app=Tk()
app.title("Weather App")
app.geometry('780x360')

city_text = StringVar()
city_entry=Entry(app,textvariable=city_text)
city_entry.pack()

search_btn = Button(app, text="Search Weather",width=12,command=search) 
search_btn.pack()

location_lb=Label(app,text='Location',font=('bold',50))
location_lb.pack()

#icon=Label(app, image='')
#icon.pack()
#img= Image.open('C:/Users/admin/Documents/Python/50d.png')
#Label(app,image=img,bg="white").grid(row=1,sticky="s")
#w = Label(app, image='img')
#w.pack()
#Label(app,image=img,bg="white").grid(row=1,sticky="s")
#wp=Label(app,font=('Calibiri bold',15),bg="white") 
#wp.grid(row=2,sticky='W',padx=40)

temp_lb=Label(app, text="Temperture",font=('bold',20))
temp_lb.pack()

weather_lb=Label(app,text="Weather",font=('bold',20))
weather_lb.pack()

                                                            
app.mainloop() 
