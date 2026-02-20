import configparser
from typing import Dict
from .player import Player
import requests

class QueryManager:
    headers: Dict[str, str]

    def __init__(self, config_file: str = "CONFIG") :
        config = configparser.ConfigParser()
        config.read(config_file)

        self.headers = {}
        self.headers['Authorization'] = config['DEFAULT']['Authorization']

    def run_query(self, query, variables):
        request = requests.post('https://api.start.gg/gql/alpha',
                                json={"query":query,
                                      "variables": variables},
                                headers=self.headers)
        if request.status_code == 200:
            return request.json()
        else :
            raise Exception("Query failed to run. Return code: {}\n{}".format(request.status_code, query))
    
    def get_event_id(self, path: str) -> str:
        query = """
            query getEventId($slug: String) {
                event(slug: $slug) {
                    id
                    name
                }
            }
            """
        
        variables = {"slug": path}
        return self.run_query(query, variables)['data']['event']['id']
    

    def get_event_players(self, event_id: str) -> Dict[str, Player]:
        current_page = 1
        query = """
        query EventEntrants($eventId: ID!, $page: Int!, $perPage: Int!) {
            event(id: $eventId) {
                id
                name
                entrants(query: {
                    page: $page
                    perPage: $perPage
                }) {
                    pageInfo {
                        total
                        totalPages
                    }
                    nodes {
                        id
                        participants {
                            id
                            gamerTag
                            prefix
                            checkedIn
                          	requiredConnections {
                              externalId
                              externalUsername
                              type
                            }
                            user {
                                genderPronoun
                            }
                        }
                    }
                }
            }
        },"""
        
        variables = {
            "eventId": event_id,
            "page": current_page,
            "perPage": 10
        }

        response = self.run_query(query, variables)
        players: Dict = {}

        for node in response['data']['event']['entrants']['nodes'] :
            pl = Player.from_entrant_query(node)
            players[pl.id] = pl

        while response['data']['event']['entrants']['pageInfo']['totalPages'] > current_page:
            current_page += 1
            variables["page"] = current_page
            response = self.run_query(query, variables)

            for node in response['data']['event']['entrants']['nodes'] :
                pl = Player.from_entrant_query(node)
                players[pl.id] = pl

        return players