class TeacherCRUD:
    def __init__(self, database):
        self.db = database

    def create(self, name, ano_nasc, cpf):
        with self.db.driver.session() as session:
            session.run(
                "CREATE (:Teacher {name: $name, ano_nasc: $ano_nasc, cpf: $cpf})",
                name=name, ano_nasc=ano_nasc, cpf=cpf
            )
            print(f"Teacher '{name}' criado com sucesso.")

    def read(self, name):
        with self.db.driver.session() as session:
            result = session.run(
                "MATCH (t:Teacher {name: $name}) RETURN t.name as name, t.ano_nasc as ano_nasc, t.cpf as cpf",
                name=name
            )
            record = result.single()
            if record:
                return {"name": record["name"], "ano_nasc": record["ano_nasc"], "cpf": record["cpf"]}
            else:
                print(f"Teacher '{name}' não encontrado.")
                return None

    def update(self, name, newCpf):
        with self.db.driver.session() as session:
            session.run(
                "MATCH (t:Teacher {name: $name}) SET t.cpf = $newCpf",
                name=name, newCpf=newCpf
            )
            print(f"CPF do Teacher '{name}' atualizado para '{newCpf}'.")

    def delete(self, name):
        with self.db.driver.session() as session:
            session.run("MATCH (t:Teacher {name: $name}) DELETE t", name=name)
            print(f"Teacher '{name}' deletado com sucesso.")
