def fizzbuzz(num):
    result = ''
    if num % 3 == 0:
        result += 'Fizz'
    if num % 5 == 0:
        result += 'Buzz'
    return result if len(result) > 0 else num

def main():
    for i in range(1,100):
        print(fizzbuzz(i))

if __name__ == '__main__':
    main()