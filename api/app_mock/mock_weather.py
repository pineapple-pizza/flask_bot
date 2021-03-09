from flask import Flask, request, render_template
import requests
import json

class Weather(object):
    def __init__(self):
        self.query = "paris"
        
    @property
    def get(self):
        weather_req = requests.get("https://api.openweathermap.org/data/2.5/weather?q="+ self.query + "&units=metric&lang=fr&APPID=45ba61fe0432754de8daa1adc7e5f590")
        if weather_req.ok:
            return weather_req
        else:
            return None