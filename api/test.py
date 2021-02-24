try:
    from app import app
    import unittest
    
except Exception as e:
    print ('Some modules are missing {}'.format(e))
    
class FlaskTest(unittest.TestCase):
    
    """check if res is 200 """
    def test_index(self):
        tester = app.test_client(self)
        response = tester.get('/api/greeting')
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)
        
    """check if content is app/json in """
    def test_index_content(self):
        tester = app.test_client(self)
        response = tester.get('/api/greeting')
        self.assertEqual(response.content_type, "application/json")
        
    """check for return data"""
    def test_index_data(self):
        tester = app.test_client(self)
        response = tester.get('/api/greeting')
        self.assertTrue(b'greeting' in response.data)
        
    """check for route api/data"""
    def test_data_res(self):
        query = 'paris'
        with app.test_client() as c:
            response = c.get('/api/data?query=' + query)
            self.assertEqual(response.status_code, 200)

    """check for route api/map"""
    def test_map_res(self):
        lat = '48.8566969'
        lon = '48.8566969'
        name = 'Paris, Île-de-France, France métropolitaine, 75004, France'

        with app.test_client() as c:
            response = c.get('/api/map?lat=' + lat + '&lon=' + lon + '&name=' + name)
            self.assertEqual(response.status_code, 200)
            
    """check for route api/wiki"""
    def test_wiki_res(self):
        query = 'paris'
        with app.test_client() as c:
            response = c.get('/api/wiki?query=' + query)
            self.assertEqual(response.status_code, 200)
            
    """check for route api/weather"""
    def test_weather_res(self):
        query = 'paris'
        with app.test_client() as c:
            response = c.get('/api/weather?query=' + query)
            self.assertEqual(response.status_code, 200)
            
if __name__ == "__main__":
    unittest.main()