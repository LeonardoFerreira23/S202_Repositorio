def connect(self, database: str, collection: str):
    try:
        connection_string = "mongodb+srv://root:root@cluster0.mongodb.net/exercicioAvaliativo?retryWrites=true&w=majority"

        self.cluster_connection = pymongo.MongoClient(
            connection_string,
            tlsAllowInvalidCertificates=True
        )
        self.db = self.cluster_connection[database]
        self.collection = self.db[collection]
        print(f"Conectado ao banco de dados '{database}' e à coleção '{collection}' com sucesso!")
    except Exception as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
