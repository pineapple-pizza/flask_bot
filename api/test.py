try:
    from app import app
    import unittest
    import json
    
except Exception as e:
    print ('Some modules are missing {}'.format(e))
    
class FlaskTest(unittest.TestCase):
    query = 'paris'
    lat = '48.8566969'
    lon = '48.8566969'
    name = 'Paris, Île-de-France, France métropolitaine, 75004, France'
    
    # check if res is 200
    def test_index(self):
        tester = app.test_client(self)
        response = tester.get('/api/greeting')
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)
        
    # check if content is app/json
    def test_index_content(self):
        tester = app.test_client(self)
        response = tester.get('/api/greeting')
        self.assertEqual(response.content_type, "application/json")
        
    # check for return data
    def test_index_data(self):
        tester = app.test_client(self)
        response = tester.get('/api/greeting')
        self.assertTrue(b'greeting' in response.data)
    
if __name__ == "__main__":
    unittest.main()