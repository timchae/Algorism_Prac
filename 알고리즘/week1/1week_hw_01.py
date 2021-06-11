input = 30


def find_prime_list_under_number(number):
    aaa = []
    for n in range(number+1):

        print(n)
        if n > 1:

            b = 0
            for a in range(n+1):

                if a > 0 and n % a ==0:
                    b += 1
                
            
            if b == 2:

                aaa.append(n)
    print(aaa)
    # 이 부분을 채워보세요!
    return aaa


result = find_prime_list_under_number(input)
print(result)