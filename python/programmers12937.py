def solution(num):
    if num % 2 == 0:
        answer = "Even"
    else:
        answer = "Odd"
    return answer

def main():
    number = int(input())
    answer = solution(number)
    print(answer)
    
if __name__ == '__main__':
    main()