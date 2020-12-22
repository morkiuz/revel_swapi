from gql import gql, Client
from gql.transport.requests import RequestsHTTPTransport
import json


class Swapi:
    "prints a list of characters from the movies, allows to get list of movies"
    " with specific character"

    def __init__(self, endpoint):
        self.endpoint = endpoint
        self.transport = RequestsHTTPTransport(url=self.endpoint)
        self.client = Client(
            transport=self.transport, fetch_schema_from_transport=True)

    def get_characters(self):
        "returns all characters from SW"

        query = gql(
            """
            query getAllChars{
                allPeople{people{name, id}}
                }
            """
        )
        result = self.client.execute(query)

        with open("characters.json", "w") as char_file:
            json.dump(result, char_file)

        # print parsed list for user to select chars from
        if "allPeople" in result:
            for rec in result["allPeople"]["people"]:
                print(rec["name"])
        else:
            print("Incorrect results from API!")
            exit()

        return result

    def get_films(self, qry_ID):
        "returns list of films character was in"

        query = gql(
            """
            query getCharFilms{
                person(id: "%s"){
                    filmConnection{
                        films{
                            title
                            }
                        }
                    }
                }
            """ % (qry_ID)
        )
        try:
            result = self.client.execute(query)
        except Exception as e:
            if "No valid ID extracted" in str(e):
                print("Invalid name provided!")
            else:
                print("Unknown error")
            return {}

        with open("films.json", "w") as char_file:
            json.dump(result, char_file)

        if "person" in result:
            for rec in result["person"]["filmConnection"]["films"]:
                print("\t" + rec["title"])
        else:
            print("Incorrect results from API!")
            return {}

        return result


if __name__ == "__main__":
    tech_chal = Swapi(
        "https://swapi-graphql.netlify.app/.netlify/functions/index/")
    characters = tech_chal.get_characters()

    qry_char = input("Type the name of a character:\n")

    qry_ID = next((
        item["id"] for item in characters["allPeople"]["people"] if
        item["name"] == qry_char
    ), "")
    tech_chal.get_films(qry_ID)
