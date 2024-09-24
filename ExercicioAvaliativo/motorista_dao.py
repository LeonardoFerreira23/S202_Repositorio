from database import Database
from bson import ObjectId

class MotoristaDAO:
    def __init__(self):
        self.db = Database(database="exercicioAvaliativo", collection="motoristas").collection

    def create_motorista(self, motorista):
        motorista_dict = motorista.__dict__
        motorista_dict['corridas'] = [corrida.__dict__ for corrida in motorista.corridas]
        self.db.insert_one(motorista_dict)

    def read_motorista(self, motorista_id):
        return self.db.find_one({"_id": ObjectId(motorista_id)})

    def update_motorista(self, motorista_id, novos_dados):
        self.db.update_one({"_id": ObjectId(motorista_id)}, {"$set": novos_dados})

    def delete_motorista(self, motorista_id):
        self.db.delete_one({"_id": ObjectId(motorista_id)})
