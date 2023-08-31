
# Weather Teller

The **Weather Teller** is a Python program that allows users to retrieve real-time weather information for a specified city. This project uses the **WeatherAPI** to fetch current weather data, such as temperature, wind speed, humidity, and weather condition, and presents the information to the user in both Celsius and Fahrenheit units.

## Features

- Fetches weather data using the WeatherAPI.
- Provides temperature information in both Celsius and Fahrenheit.
- Presents wind speed in both miles per hour (mph) and kilometers per hour (kph).
- Displays humidity percentage for the specified city.
- Describes the current weather condition in a user-friendly text format.

## How to Use

1. Run the program in your Python environment.
2. The program will prompt you to enter a city for which you want to retrieve weather information.
3. After entering the city name, the program will fetch data from the WeatherAPI and provide the following details:
   - Temperature in Celsius and Fahrenheit.
   - Wind speed in mph and kph.
   - Humidity percentage.
   - Current weather condition.
4. The program will also utilize text-to-speech functionality to audibly share the weather details.
5. All the retrieved information will be displayed in the terminal as well.

## Dependencies

- Python 3.x
- `requests` library for making HTTP requests
- `json` library for handling JSON data
- `pyttsx3` library for text-to-speech conversion

## Contributions

Contributions to this project are welcome! If you find any issues or have suggestions for improvements, feel free to open an issue or create a pull request.
