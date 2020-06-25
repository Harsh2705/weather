
import requests, json 

# Enter your API key here 
api_key = '43527510ca1acd4a2f7d65e284b44f43'

# base_url variable to store url 
base_url = "http://api.openweathermap.org/data/2.5/weather?"

# Give city name 
city_name = input("Enter city name : ") 


complete_url = base_url + "appid=" + api_key + "&q=" + city_name 


response = requests.get(complete_url) 


x = response.json() 


if x["cod"] != "404": 

	
	y = x["main"] 

	
	current_temperature = y["temp"] 

	
	current_pressure = y["pressure"] 

	
	current_humidiy = y["humidity"] 

	 
	z = x["weather"] 

	
	weather_description = z[0]["description"] 

	# print following values 
	print(" Temperature (in kelvin unit) = " +
					str(current_temperature) +
		"\n atmospheric pressure (in hPa unit) = " +
					str(current_pressure) +
		"\n humidity (in percentage) = " +
					str(current_humidiy) +
		"\n description = " +
					str(weather_description)) 

else: 
	print(" City Not Found ") 
