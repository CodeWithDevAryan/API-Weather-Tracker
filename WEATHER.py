'''Weather Tracker'''

## IMPORTING SECTION ##
import requests,json,tkinter as tk 
from tkinter import *
from PIL import Image,ImageTk
import pytz
from datetime import *
from datetime import datetime

#DEFINE FUNCTIONS
def clear_canvas():
    canvas.delete('weather_details')


def user_data():
    global weather_description,main_temp,main_feelslike,main_min_temp,main_max_temp,main_humidity,sys_country

    clear_canvas()

    val = var1.get()
    #LINKING PYTHON TO REALTIME WEATHER TRACKING
    Api_Key = 'c7386923f55c4622e0d6480e4ea4405a'
    base_URL = 'https://api.openweathermap.org/data/2.5/weather?q='
    full_URL = base_URL + val + '&appid=' + Api_Key
    result = requests.get(full_URL)
    data = result.json()
    ## FILTERED REQUIRED DATA ##
    weather_description = data.get('weather')[0].get('description').upper()
    main_temp = data.get('main').get('temp')
    main_feelslike = data.get('main').get('feels_like')
    main_min_temp = data.get('main').get('temp_min')
    main_max_temp = data.get('main').get('temp_max')
    main_humidity = data.get('main').get('humidity')
    sys_country = data.get('sys').get('country')
    coord_lon = data.get('coord').get('lon')
    coord_lat = data.get('coord').get('lat')
    degree_sign = u'\N{DEGREE SIGN}'
    #GETTING THE NAME OF COUNTRY
    country_name = pytz.country_names[sys_country].capitalize()
    canvas.create_text(155,260,text=country_name,fill='#00ffea',font=('Helvetica',23,'bold'), tags='weather_details')
    #GETTING THE TIME OF CITY
    '''XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX  WORK IN PROGRESS  XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'''
    #BOTTOM DESCRIPTION PRINTING
    canvas.create_text(160,530,text=weather_description,fill='#ebe702',font=('arial',18,'bold'), tags='weather_details')
    #BOTTOM MIN TEMPERATURE PRINTING
    canvas.create_text(355,530,text=int(main_min_temp)-273,fill='#ebe702',font=('arial',18,'bold'), tags='weather_details')
    canvas.create_text(375,525,text=degree_sign,fill='#ebe702',font=('Helvetica',16,'bold'), tags='weather_details')
    #MAX TEMPERATURE PRINTING
    canvas.create_text(550,530,text=int(main_max_temp)-273,fill='#ebe702',font=('arial',18,'bold'), tags='weather_details')
    canvas.create_text(570,525,text=degree_sign,fill='#ebe702',font=('Helvetica',16,'bold'), tags='weather_details')
    #BOOTOM HUMIDITY PRINTING
    canvas.create_text(750,530,text=main_humidity,fill='#ebe702',font=('arial',18,'bold'), tags='weather_details')
    canvas.create_text(775,530,text='%',fill='#ebe702',font=('arial',18,'bold'), tags='weather_details')
    #SIDE TEMPERATURE
    canvas.create_text(650,230,text=int(main_temp)-273,fill='red',font=('Helvetica',60,'bold'), tags='weather_details')
    canvas.create_text(710,210,text=degree_sign,fill='red',font=('Helvetica',45,'bold'), tags='weather_details')
    #SIDE DESCRIPTION
    weather_description1 = data.get('weather')[0].get('description').title()
    canvas.create_text(700,290,text=weather_description1,fill='white',font=('arial',18,'bold'), tags='weather_details')
    #SIDE FEELS LIKE
    canvas.create_text(667,320,text='|Feels Like ',fill='white',font=('arial',18,'bold'), tags='weather_details')
    canvas.create_text(748,320,text=int(main_feelslike)-273,fill='red',font=('arial',18,'bold','underline'), tags='weather_details') 
    canvas.create_text(765,315,text=degree_sign,fill='red',font=('Helvetica',16,'bold'), tags='weather_details')

## GENRATING A WINDOW FOR THE RESULT ##
root=tk.Tk()
root.title('Weather Tracker')
scrollbar=Scrollbar(root)
scrollbar.pack(side = RIGHT,fill=Y)
root.geometry("950x630+50+30")

## CREATING CANVAS WITH SKY IMAGE ##
canvas = Canvas(root, width = 2000, height = 800)
canvas.pack()
img = PhotoImage(file=r"sky1.png")
canvas.create_image(0,0, anchor=NW, image=img)

## WORKING ON CANVAS ##
#TITLE TEXT
canvas.create_text(460,65,text='Weather Tracker',fill='white',font=('Helvetica',81,'bold'))

#SEARCH BAR IMAGE
bar_img = Image.open(r'bar.png')
bar_img = bar_img.resize((410,250))
bar_img = ImageTk.PhotoImage(bar_img)
bar_img1 = canvas.create_image(0,40,anchor=NW,image=bar_img)
canvas.tag_bind(bar_img1)

#FEED FOR SEARCH BAR
var1 = StringVar()
searchbar = Entry(root,textvariable=var1,bg='white',fg='black',justify='center',font=('helvetica',17,'bold'),highlightthickness=0,bd=0,width=21,borderwidth=0,border=0).place(x=28,y=137)

#SEARCH BUTTON
search_button = Image.open(r'final_search_icon1.png')
search_button = search_button.resize((39,37))
search_button = ImageTk.PhotoImage(search_button)
Button(root,image=search_button,highlightthickness=0,bd=0,border=0,borderwidth=0,command=user_data).place(x=302,y=133.5)
root.bind('<Return>',lambda x: user_data())

#CENTER LOGO
logo = Image.open(r'logo1.png')
logo = logo.resize((230,230))
logo = ImageTk.PhotoImage(logo)
logo_img = canvas.create_image(480,300,image=logo)
canvas.tag_bind(logo_img)

#COUNTRY TEXT
canvas.create_text(160,220,text='COUNTRY',fill='#02db59',font=('arial black',25,'bold'))

#TIME TEXT
canvas.create_text(170,328,text='CURRENT TIME',fill='#02db59',font=('arial black',24,'bold'))

#BOTTOM SHOW IMG WITH THE TEXT
bottom_box  = Image.open(r'box.png')
bottom_box = bottom_box.resize((900,195))
bottom_box = ImageTk.PhotoImage(bottom_box)
bottom_box_img = canvas.create_image(13,430,anchor=NW,image=bottom_box)
canvas.tag_bind(bottom_box_img)
canvas.create_text(140,480,text='Description',fill='black',font=('arial black',20,'bold','underline'))
canvas.create_text(370,480,text='Min Temp',fill='black',font=('arial black',20,'bold','underline'))
canvas.create_text(550,480,text='Max Temp',fill='black',font=('arial black',20,'bold','underline'))
canvas.create_text(770,480,text='Humidity',fill='black',font=('arial black',20,'bold','underline'))








## EXECUTING WINDOW ##
root.mainloop()



#----------------------------------------------------------------------------------------------
#https://home.openweathermap.org/api_keys      -    for the free api key
