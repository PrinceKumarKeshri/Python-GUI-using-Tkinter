# -*- coding: utf-8 -*-
"""
Created on Fri Dec  3 18:53:20 2021

@author: 0526p
"""

from tkinter import *
from PIL import ImageTk, Image
import requests
import json

root = Tk()
root.title('Working on API with Tkinter')

# https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=89129&distance=25&API_KEY=310CCCAF-C876-4A4B-A8B0-3369E45E2998

try:
    #api_request = requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=89129&distance=25&API_KEY=310CCCAF-C876-4A4B-A8B0-3369E45E2998")
    #api_request = requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=83814&distance=25&API_KEY=310CCCAF-C876-4A4B-A8B0-3369E45E2998")
    #api_request = requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=83530&distance=25&API_KEY=310CCCAF-C876-4A4B-A8B0-3369E45E2998")
    api_request = requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=70801&distance=25&API_KEY=310CCCAF-C876-4A4B-A8B0-3369E45E2998")
    api = json.loads(api_request.content)
    city = api[0]['ReportingArea']
    qualtiy = api[0]['AQI']
    category = api[0]['Category']['Name']
    
    if category == 'Good':
        weather_color = '#0C0'
    elif category == "Moderate":
        weather_color = '#FFFF00'
    elif category == "Unhealthy for Sensitive Groups":
        weather_color = '#ff9900'
    elif category == "Unhealthy":
        weather_color = '#FF0000'
    elif category == "Very Unhealthy":
        weather_color = '#990066' 
    elif category == "Hazarious":
        weather_color = '#660000'

    root.configure(bg = weather_color)
    
    myLabel = Label(root, text = city + ' ' + 'Air Qualtiy' + ' ' + str(qualtiy)+ ' '+ category, bg = weather_color, font = ("Helvetica", 20))
    myLabel.pack()

except Exception as e:
    api = "Error..."


root.mainloop()
