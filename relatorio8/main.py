from database import Database
from game_database import GameDataBase

if __name__ == "__main__":
    db = Database("bolt://localhost:7687", "neo4j", "password")
    game_db = GameDatabase(db)
    
   
    game_db.create_player("Alice")
    game_db.create_player("Bob")

    
    game_db.create_match("match1", "Alice", "Bob", "Alice venceu")

    
    print(game_db.get_players())

    
    print(game_db.get_match("match1"))

    
    print(game_db.get_player_match_history("Alice"))

    
    db.close()