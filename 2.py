def num_in_fibonacci(num):
    first = 0
    second = 1
    if (num == first or num == second):
        return 'O numero pertence a sequencia'
    while True:
        next = first + second
        if (num == next):
            return 'O numero pertence a sequencia'
        elif (num < next):
            return 'O numero nao pertence a sequencia'
        first = second
        second = next
            
def main():
    n = int(input())
    print(num_in_fibonacci(n))

main()