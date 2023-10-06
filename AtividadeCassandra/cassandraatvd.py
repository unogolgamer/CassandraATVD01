from cassandra.cluster import Cluster
from uuid import uuid4

class TaskManager:
    def __init__(self):
        cluster = Cluster(['localhost'])  # Substitua 'localhost' pelo endereço do seu cluster, se aplicável
        self.session = cluster.connect('bancodados')  # Use o keyspace 'task_manager'

    def add_task(self, description):
        task_id = uuid4()
        query = "INSERT INTO tasks (task_id, description) VALUES (%s, %s)"
        self.session.execute(query, (task_id, description))
        print(f'Tarefa {task_id} adicionada: {description}')

    def list_tasks(self):
        rows = self.session.execute("SELECT task_id, description FROM tasks")
        print("Lista de Tarefas:")
        for row in rows:
            print(f"ID: {row.task_id}, Descrição: {row.description}")

    def remove_task(self, task_id):
        task_id = uuid4(task_id)  # ID da tarefa a ser removida
        query = "DELETE FROM tasks WHERE task_id = %s"
        self.session.execute(query, (task_id,))
        print(f"Tarefa {task_id} removida")

if __name__ == "__main__":
    task_manager = TaskManager()

    while True:
        print("\n1. Adicionar Tarefa")
        print("2. Listar Tarefas")
        print("3. Remover Tarefa")
        print("4. Sair")

        choice = input("Escolha uma opção: ")

        if choice == '1':
            description = input("Digite a descrição da tarefa: ")
            task_manager.add_task(description)
        elif choice == '2':
            task_manager.list_tasks()
        elif choice == '3':
            task_id = input("Digite o ID da tarefa a ser removida: ")
            task_manager.remove_task(task_id)
        elif choice == '4':
            break
        else:
            print("Opção inválida. Escolha novamente.")
