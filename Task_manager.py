"""
Менеджер задач

Задача: Создай класс Task, который позволяет управлять задачами (делами). У задачи должны быть атрибуты: описание задачи,
срок выполнения и статус (выполнено/не выполнено). Реализуй функцию для добавления задач, отметки выполненных задач и 
вывода списка текущих (не выполненных) задач. Добавь возможность удаления задач, редактирования
Программируй на питоне

Конечно! Давайте создадим класс `Task`, который будет управлять задачами, а также реализуем функции для добавления, удаления, 
редактирования и вывода текущих задач. Вот пример реализации на Python:
"""

class Task:
    def __init__(self, description, due_date):
        self.description = description
        self.due_date = due_date
        self.completed = False

    def mark_completed(self):
        self.completed = True

    def __repr__(self):
        status = "Выполнено" if self.completed else "Не выполнено"
        return f"Задача: {self.description}, Срок: {self.due_date}, Статус: {status}"


class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, description, due_date):
        new_task = Task(description, due_date)
        self.tasks.append(new_task)
        print(f"Добавлена задача: {new_task}")

    def mark_task_completed(self, task_index):
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index].mark_completed()
            print(f"Задача отмечена как выполненная: {self.tasks[task_index]}")
        else:
            print("Некорректный индекс задачи.")

    def delete_task(self, task_index):
        if 0 <= task_index < len(self.tasks):
            removed_task = self.tasks.pop(task_index)
            print(f"Удалена задача: {removed_task}")
        else:
            print("Некорректный индекс задачи.")

    def edit_task(self, task_index, new_description, new_due_date):
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index].description = new_description
            self.tasks[task_index].due_date = new_due_date
            print(f"Задача обновлена: {self.tasks[task_index]}")
        else:
            print("Некорректный индекс задачи.")

    def view_current_tasks(self):
        current_tasks = [task for task in self.tasks if not task.completed]
        if current_tasks:
            print("Текущие задачи:")
            for index, task in enumerate(current_tasks):
                print(f"{index}. {task}")
        else:
            print("Нет текущих задач.")


# Пример использования
if __name__ == "__main__":
    task_manager = TaskManager()
    
    # Добавление задач
    task_manager.add_task("Купить молоко", "2023-10-15")
    task_manager.add_task("Написать отчет", "2023-10-20")
    
    # Просмотр текущих задач
    task_manager.view_current_tasks()
    
    # Отметка задачи как выполненной
    task_manager.mark_task_completed(0)
    
    # Просмотр текущих задач

    task_manager.view_current_tasks()
    
    # Редактирование задачи
    task_manager.edit_task(1, "Написать отчет по проекту", "2023-10-25")
    
    # Просмотр текущих задач
    task_manager.view_current_tasks()
    
    # Удаление задачи
    task_manager.delete_task(0)
    
    # Просмотр текущих задач
    task_manager.view_current_tasks()

"""
### Объяснение кода:
1. **Класс `Task`:** Определяет структуру задачи с атрибутами `description`, `due_date` и `completed`. Метод 
`mark_completed` позволяет отметить задачу как выполненную.
2. **Класс `TaskManager`:** Управляет списком задач и предоставляет методы для добавления, удаления, редактирования и 
просмотра задач.
3. **Пример использования:** В конце кода приведен пример использования класса `TaskManager`, который демонстрирует 
добавление, редактирование, удаление задач и просмотр текущих задач.

"""