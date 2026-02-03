def solution(phone_book):
    phone_set = set(phone_book)

    for phone in phone_book:
        temp = ""
        for ch in phone:
            temp += ch
            if temp in phone_set and temp != phone:
                return False
    return True

phone_book=["119", "97674223", "1195524421"]
# print(phone_book)
solution(phone_book)
# 두개를 &연산했을때 존재하고, 그걸로 된 원소가 있으면 ok