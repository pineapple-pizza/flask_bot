from flask import Flask, request, render_template
from flask_cors import CORS
from flask.views import MethodView
import folium
from folium import branca
import requests
from IPython.display import HTML, display
import json

from nltk.tokenize import word_tokenize

app = Flask(__name__)
CORS(app)

search_URL = "https://nominatim.openstreetmap.org/search?"

@app.route("/api/greeting")
def greeting():
    return {'greeting': 'Hello from Flask!'}

class Query:
    """parsing the query before executing it"""
    def __init__(self, query):
        self.query = query

    def check_query(query):
        query = request.args['query']
        file_name = "static/fr.json"
        with open(file_name) as stop_words:
            words_data = json.load(stop_words)
        
        if "'" in query:
            query = query.replace("'", ' ')
        
        words = word_tokenize(query.lower())
        filtered_sentence = []
        
        for w in words:
            if w in words_data:
                filtered_sentence.append(w)
                
        query = [i for i in words if not i in words_data]
        return query

class Data(MethodView):
    """ Example of a class inheriting from flask.views.MethodView 

    All 5 request methods are available at /api/data
    """
    def get(self):
        """ Responds to GET requests for the data"""
    
        query = request.args['query']
        checked_query = Query.check_query(query)
        print ("checked query", checked_query)
        
        search_payload = {'q': checked_query, 'format' : "json", 'addressdetails' : 1}
        search_req = requests.get(search_URL, params = search_payload)
        search_json = search_req.json()
        print('search', search_json[0])
        
        return search_json[0]

app.add_url_rule("/api/data/", view_func=Data.as_view("data"))

class Map(MethodView):
    """ Example of a class inheriting from flask.views.MethodView 

    All 5 request methods are available at /api/map
    """
    def get(self):
        """ Responds to GET requests for the map"""
    
        lat = request.args['lat']    
        lon = request.args['lon']
        name = request.args['name']
        
        iframe = branca.element.IFrame(html=name, width=150, height=50)
        
        coordinates = [lat, lon]
        
        map = folium.Map(
            location=coordinates,
            width=300,
            height=300,
            zoom_start=13,
            tiles="openstreetmap"
        )
        
        folium.Marker(
            location=coordinates,
            popup=folium.Popup(iframe, max_width='100%'),
            tooltip="Click Here!"
        ).add_to(map)
            
        return map._repr_html_()

app.add_url_rule("/api/map/", view_func=Map.as_view("map"))

class Wiki(MethodView):
    """ Example of a class inheriting from flask.views.MethodView 

    All 5 request methods are available at /api/wiki
    """
    def get(self):
        """ Responds to GET requests for the wiki"""
    
        query = request.args['query']
        checked_query = Query.check_query(query)
        print ("checked query", checked_query)
        
        wiki_req = requests.get("https://fr.wikipedia.org/w/api.php?action=query&titles="+ checked_query[0] +"&prop=extracts&formatversion=2&exsentences=3&format=json&exlimit=1&explaintext=1")
        wiki_json = wiki_req.json()
        wiki_formatted = wiki_json["query"]["pages"][0]  
        
        return wiki_formatted["extract"]

app.add_url_rule("/api/wiki/", view_func=Wiki.as_view("wiki"))

if __name__ == "__main__":
    app.run(debug=True)