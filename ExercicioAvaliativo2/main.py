from query import Database
from teacher_crud import TeacherCRUD
from dotenv import load_dotenv
import os

# Carregar variáveis de ambiente do .env
load_dotenv()

def main():
    uri = "bolt://localhost:7687"  
    user = "root"  
    password = "root"  

    database = Database(uri, user, password)
    teacher_crud = TeacherCRUD(database)

    # Questão 1: 
    print("=== Questão 1 ===")
    print("1. Buscar professor 'Renzo'")
    teacher_renzo = database.find_teacher_by_name("Renzo")
    print("Teacher Renzo:", teacher_renzo)

    print("\n2. Professores com nome começando com 'M'")
    teachers_with_m = database.find_teachers_by_initial("M")
    print("Teachers com 'M':", teachers_with_m)

    print("\n3. Nomes de todas as cidades")
    cities = database.find_all_cities()
    print("Cidades:", cities)

    print("\n4. Escolas com número entre 150 e 550")
    schools_in_range = database.find_schools_in_range(150, 550)
    print("Escolas:", schools_in_range)

    # Questão 2: 
    print("\n=== Questão 2 ===")
    print("1. Ano de nascimento do professor mais jovem e mais velho")
    age_range = database.find_age_range_of_teachers()
    print("Faixa etária:", age_range)

    print("\n2. Média de população das cidades")
    avg_population = database.average_population()
    print("Média de população:", avg_population)

    print("\n3. Nome da cidade com CEP '37540-000' com 'a' substituído por 'A'")
    modified_city_name = database.find_city_by_cep("37540-000")
    print("Cidade modificada:", modified_city_name)

    print("\n4. Caracteres a partir da terceira letra do nome dos professores")
    name_chars = database.get_teacher_name_chars()
    print("Caracteres:", name_chars)

    # Questão 3: 
    print("\n=== Questão 3 ===")
    
    # 1. Criar Teacher com nome 'Chris Lima'
    print("\nCriando Teacher 'Chris Lima'")
    teacher_crud.create(name="Chris Lima", ano_nasc=1956, cpf="189.052.396-66")

    # 2. Ler Teacher 'Chris Lima'
    print("\nLendo Teacher 'Chris Lima'")
    teacher = teacher_crud.read(name="Chris Lima")
    if teacher:
        print("Teacher encontrado:", teacher)

    # 3. Atualizar CPF de 'Chris Lima'
    print("\nAtualizando CPF do Teacher 'Chris Lima'")
    teacher_crud.update(name="Chris Lima", newCpf="162.052.777-77")

    # 4. Verificar atualização
    print("\nVerificando atualização do Teacher 'Chris Lima'")
    updated_teacher = teacher_crud.read(name="Chris Lima")
    if updated_teacher:
        print("Teacher atualizado:", updated_teacher)

    
    database.close()

if __name__ == "__main__":
    main()
