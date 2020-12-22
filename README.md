# SWAPI tech challenge by Revel Systems
The challenge had a clear discription, however, not very specific, therefore a few decisions had to be made based on assumptions. 

Works with Python > 3.8

## Clone 
```bash
$ git clone git@github.com:morkiuz/revel_swapi.git
```
## Dependencies
This app uses **gql** as the client and **pytest** for testing.

## Run the app
Navigate to the lib folder and run:
```bash
$ python3 swapi.py
```
The app will print a list of movie characters, print the *json response* from the server as a file, and allow
you to input your desired character.

After the name of a character is given, the app makes another request to the server with the character's ID. 
The response is printed to the shell and json response is saved as a file. 

## JSON response
The challenge does not provide a schema for the JSON file, so the app simply dumps JSON response from the API.
The file is printed in the current path of the app. 

## Testing
Please run the test by navigating one directory up from the lib.
```bash
$ pytest
```
