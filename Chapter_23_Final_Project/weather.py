from dotenv import load_dotenv
from pprint import pprint
import requests
import os

load_dotenv()

def get_current_weather(city="jaipur"):
    request_url = f'https://api.openweathermap.org/data/2.5/weather?appid={os.getenv("API_KEY")}&q={city}&units=metric'

    print(request_url)

    return requests.get(request_url).json()

if __name__ == "__main__":
    print('\n*** Get Current Weather condition ***\n')
    city = input("\nPlease enter a city name: ")
    
    # check for empty string or string with only spaces
    if not bool(city.strip()):
        city = "jaipur"

    weather_data = get_current_weather(city)
    print("\n")
    pprint(weather_data)
          

