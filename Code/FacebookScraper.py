import json
import facebook

#def main():
token = "EAACc20BnkiUBALSvpSsmXUcDKzX9NU7aBcaLNqBwXApv8fJp58YpkZB2IT32vZCQPIgPStaIbdPDpZB5aui1jZBk4exyaWxu30QAhKqzuNtNI0KNmmtp9PPi4suBqxAoSXTBbOyRj5oew1hbzJenGfALBpiOMNhGclbZB8ooZB3om69yqzwNz6jT0unJ5lL40x7fEg8agYKcekRlIkG8xHonDQUZBHjLtSkuY77wrxMLC0gdYiNZCRnOHHKXkUEVUt8ZD"
graph = facebook.GraphAPI(token)
profile = graph.get_object('colinectg', fields ='albums')

print(json.dumps(profile, indent = 4))