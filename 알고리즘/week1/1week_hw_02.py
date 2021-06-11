input = "111101100011000"


def find_count_to_turn_out_to_all_zero_or_all_one(string):
    status = 1
    num = 0
    for st in string:
        
        a = string[0]

        if st != a and status == 1:
            status = 0
            num += 1 
        elif status == 0 and st == a:
            status = 1

        



    # 이 부분을 채워보세요!
    return num


result = find_count_to_turn_out_to_all_zero_or_all_one(input)
print(result)



