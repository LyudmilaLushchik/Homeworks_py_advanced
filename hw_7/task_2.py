from task_1 import Stack


stack = '[([])((([[[]]])))]{()}'

def balance(stack_to_check):
    sets = {'(': ')', '{': '}', '[': ']'}
    result_stack = Stack()
    for el in stack_to_check:
        if el in sets.keys():
            result_stack.push(el)
        elif not result_stack.is_empty() and sets.get(result_stack.peek()) == el:
            result_stack.pop()
        else:
            break

    if result_stack.is_empty():
        return 'Cбалансированно'
    else:
        return 'Несбалансированно'

print(balance(stack))