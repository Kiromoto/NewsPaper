from todo import Todo, todos, create_todo, find_todos


def test_create_todo():
    result = create_todo("kek")
    assert isinstance(result, Todo)
    assert result in todos


def test_find_todo():
    to_find_one = create_todo("kek")
    not_to_find = create_todo("lol")
    to_find_two = create_todo("keke")
    search_result = find_todos("ke")
    assert to_find_one in search_result
    assert to_find_two in search_result
    assert not_to_find not in search_result
