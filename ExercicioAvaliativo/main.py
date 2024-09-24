from database import Database
from motorista_dao import MotoristaDAO
from motorista_cli import MotoristaCLI

db = Database(database="exercicioAvaliativo", collection="motoristas")

# db.reset_database()

MotoristaModel = MotoristaDAO()

motoristaCLI = MotoristaCLI()

motoristaCLI.menu()
