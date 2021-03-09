import unittest
from  unittest.mock import patch
from app_mock.mock_weather import Weather

class TestWeatherMock(unittest.TestCase):

    def test_weather_response(self):
        fake_weather = [{'city': 'paris', 'temperature': '12.01', 'icon': '03d'}]

        with patch('app_mock.mock_weather.requests.get') as mock_get:
            mock_get.return_value.status_code = 200
            mock_get.return_value.json.return_value = fake_weather

            obj = Weather()
            response = obj.get

            print(response.status_code)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), fake_weather)

if __name__ == "__main__":
    unittest.main()