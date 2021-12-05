#Here I am importing from the requests library and the json(Javascript Object Notation) module to use in my program below
import requests
import json

#Here I am welcoming the user to my program along with prompting the user for their choice of input
welcome_message = input("Welcome to the Weather Forcast Application Program: Press the Enter key to continue...")
response = input('Would you like to search by city or zip code?: ')
#Here, if the user would like to search by city, the city function will be executed below to provide the weather forecast of that chosen city 
def city():
	city_name = input("Please enter in the name of your city: ")
	URL = 'https://api.openweathermap.org/data/2.5/weather?q='+city_name+'&APPID=03fc6cd89efb8491fff91f8220620737'
	r = requests.get(URL)
	print(r.json())
#Here, if the user would like to search by zip code, the zip(zip code) function will be executed below to provide the weather forecast of that chosen zip code 
def zip():
	zip_code = input("Please enter in your zip code: ")
	URL = 'https://api.openweathermap.org/data/2.5/weather?zip='+zip_code+'&appid=3902e82072006da200f65857245b74bf'
	r = requests.get(URL)
	print(r.json())
#Here is the where the main function is implemented as an if/elif/else statement that executes based upon what input is provided by the user through the response variable
def main():
	if response == "city": 
	  city()
	elif response == "zip code": 
	  zip()
	else:
		print("The input you provided is invalid. Please try again...")
		
main()
#End of program















	
	

