todos = []


class Todo:
    def __init__(self, text):
        self.text = text


def create_todo(text):
    result = Todo(text)
    todos.append(result)
    return result


def find_todos(search_text):
    return [
        todo for todo in todos
        if search_text in todo.text
    ]
