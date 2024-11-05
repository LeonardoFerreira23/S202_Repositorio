from neo4j import GraphDatabase

class Database:
    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self.driver.close()

    # Questão 1
    def find_teacher_by_name(self, name):
        with self.driver.session() as session:
            result = session.run("MATCH (t:Teacher {name: $name}) RETURN t.ano_nasc, t.cpf", name=name)
            return result.single()

    def find_teachers_by_initial(self, initial):
        with self.driver.session() as session:
            result = session.run("MATCH (t:Teacher) WHERE t.name STARTS WITH $initial RETURN t.name, t.cpf", initial=initial)
            return result.values()

    def find_all_cities(self):
        with self.driver.session() as session:
            result = session.run("MATCH (c:City) RETURN c.name")
            return [record["c.name"] for record in result]

    def find_schools_in_range(self, min_number, max_number):
        with self.driver.session() as session:
            result = session.run(
                "MATCH (s:School) WHERE s.number >= $min_number AND s.number <= $max_number "
                "RETURN s.name, s.address, s.number",
                min_number=min_number, max_number=max_number
            )
            return result.values()

    # Questão 2
    def find_age_range_of_teachers(self):
        with self.driver.session() as session:
            result = session.run("MATCH (t:Teacher) RETURN min(t.ano_nasc) as oldest, max(t.ano_nasc) as youngest")
            return result.single()

    def average_population(self):
        with self.driver.session() as session:
            result = session.run("MATCH (c:City) RETURN avg(c.population) as avg_population")
            return result.single()["avg_population"]

    def find_city_by_cep(self, cep):
        with self.driver.session() as session:
            result = session.run(
                "MATCH (c:City {cep: $cep}) RETURN replace(c.name, 'a', 'A') as modified_name", cep=cep
            )
            return result.single()["modified_name"]

    def get_teacher_name_chars(self):
        with self.driver.session() as session:
            result = session.run("MATCH (t:Teacher) RETURN substring(t.name, 2, 1)")
            return [record["substring(t.name, 2, 1)"] for record in result]



