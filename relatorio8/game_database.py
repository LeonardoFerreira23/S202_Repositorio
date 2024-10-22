from neo4j import GraphDatabase

class GameDataBase:
    def __init__(self, database):
        self.db = database

    def create_player(self, player_name):
        query = "CREATE (:Player {name: $name})"
        parameters = {"name": player_name}
        self.db.execute_query(query, parameters)

    def update_player(self, old_name, new_name):
        query = "MATCH (p:Player {name: $old_name}) SET p.name = $new_name"
        parameters = {"old_name": old_name, "new_name": new_name}
        self.db.execute_query(query, parameters)

    def delete_player(self, player_name):
        query = "MATCH (p:Player {name: $name}) DETACH DELETE p"
        parameters = {"name": player_name}
        self.db.execute_query(query, parameters)

    def get_players(self):
        query = "MATCH (p:Player) RETURN p.name AS name"
        results = self.db.execute_query(query)
        return [result["name"] for result in results]

    def create_match(self, match_id, player1_name, player2_name, result):
        query = """
            MATCH (p1:Player {name: $player1_name}), (p2:Player {name: $player2_name})
            CREATE (m:Match {id: $match_id, result: $result})<-[:PARTICIPATED_IN]-(p1),
                   (m)<-[:PARTICIPATED_IN]-(p2)
        """
        parameters = {"match_id": match_id, "player1_name": player1_name, "player2_name": player2_name, "result": result}
        self.db.execute_query(query, parameters)

    def delete_match(self, match_id):
        query = "MATCH (m:Match {id: $match_id}) DETACH DELETE m"
        parameters = {"match_id": match_id}
        self.db.execute_query(query, parameters)

    def get_match(self, match_id):
        query = """
            MATCH (m:Match {id: $match_id})<-[:PARTICIPATED_IN]-(p:Player)
            RETURN m.id AS match_id, m.result AS result, collect(p.name) AS players
        """
        parameters = {"match_id": match_id}
        results = self.db.execute_query(query, parameters)
        return results[0] if results else None

    def get_player_match_history(self, player_name):
        query = """
            MATCH (p:Player {name: $player_name})-[:PARTICIPATED_IN]->(m:Match)
            RETURN m.id AS match_id, m.result AS result
        """
        parameters = {"player_name": player_name}
        results = self.db.execute_query(query, parameters)
        return [(result["match_id"], result["result"]) for result in results]