# for git test operation

def add(x, y):
    '''두 숫자를 덧셈'''
    return x + y

def subtract(x, y):
    '''두 숫자를 뺄셈'''
    return x - y

def multiply(x, y):
    '''두 숫자를 곱셈'''
    return x * y

def divide(x, y):
    '''두 숫자를 나눗셈 (0으로 나누는 경우는 처리 불가)'''
    if y == 0:
        return 'Error: Division by zero!'
    return x / y

if __name__ == '__main__':
    # 사용자로부터 숫자를 입력받습니다.
    num1 = float(input('첫 번째 숫자를 입력하세요: '))
    num2 = float(input('두 번째 숫자를 입력하세요: '))

    # 각각의 연산을 수행하고 결과를 출력합니다.
    print('{} + {} = {}'.format(num1, num2, add(num1, num2)))


##Git test 1

##Git Test Num 22222222222222222222222222222222

##Git Test Num 3

