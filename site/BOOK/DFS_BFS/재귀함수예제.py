# 무한 반복함수
def recursive_function():
    print("call recursive func() ")

    recursive_function()

recursive_function()


# 반복 제한 함수
def limit_recursive_function(i):
    # 100 회 제한
    if i == 100: return

    print(f'{i} time call recursive function')
    limit_recursive_function(i + 1)

limit_recursive_function()