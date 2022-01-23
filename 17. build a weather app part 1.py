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
root.configure(bg = 'navy')

# https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=89129&distance=25&API_KEY=310CCCAF-C876-4A4B-A8B0-3369E45E2998

try:
    api_request = requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=89129&distance=25&API_KEY=310CCCAF-C876-4A4B-A8B0-3369E45E2998")
    api = json.loads(api_request.content)
    city = api[0]['ReportingArea']
    qualtiy = api[0]['AQI']
    category = api[0]['Category']['Name']
except Exception as e:
    api = "Error..."

#myLabel = Label(root, text = api)
#myLabel = Label(root, text = api[0])
#myLabel = Label(root, text = api[0]['ReportingArea'])
#myLabel = Label(root, text = api[0]['AQI'])
#myLabel = Label(root, text = api[0]['Category'])
#myLabel = Label(root, text = api[0][Category]['Name'])
myLabel = Label(root, text = city + ' ' + 'Air Qualtiy' + ' ' + str(qualtiy)+ ' '+ category, bg = 'navy', fg = 'white', font = ("Helvetica", 20))
myLabel.pack()

root.mainloop()