def fibonacci_docker(n):
    if n < 2:
        return n
    else:
        return fibonacci_docker(n - 2) + fibonacci_docker(n - 1)

if __name__ == '__main__':
    input_user = int(input('Write a number: '))
    print(f'The number {input_user} in the fibonacci sequence is: {fibonacci_docker(input_user)}')
    #print(fibonacci_docker(10))