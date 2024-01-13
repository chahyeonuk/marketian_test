
def problem_1():
    """
    코드 작성
    """

    number = int(input())
    
    if number == 0 or number ==1:
        print()
        print("소수의 개수 : 0")

    def is_prime(num):    
        for i in range(2, int(num**0.5)+1):
            if num % i == 0:
                return False
        return True

    count = 0
    for i in range(2, number):
        if is_prime(i):
            print(i, end=' ')
            count+=1
    print()
    print(f"소수의 개수: {count}")
    

def problem_2(phone_book):
    answer = True
    """
    코드 작성
    """
    index = 0
    while True:
        if not phone_book:
            break
        # list 객체 재선언
        temp_phone_book = list(phone_book)
        del temp_phone_book[index]

        for phone in temp_phone_book:
            if phone.startswith(phone_book[index]):
                answer = False
                break
        if not answer:
            break
        if len(phone_book)-1 == index:
            break
        index += 1
    
    print(answer)
    return answer
    
if __name__ == '__main__':
    problem_1()
    problem_2(["12","123","1235","567","88"])
    problem_2(["123","456","789"])