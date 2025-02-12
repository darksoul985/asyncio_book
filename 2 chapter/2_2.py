async def coroutine_add_one(number: int) -> int:
    return number + 1

def add_one(number: int) -> int:
    return number + 1

function_result = add_one(1)
coroutine_result = coroutine_add_one(1)

print(f'''Резульат функции равен {function_result},\n\rа его тип равен {type(function_result)}''')

print(f'''Резульат сопрограммы равен {coroutine_result},\n\rа его тип равен {type(coroutine_result)}''')