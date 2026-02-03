def solution(nums):
    answer = 0
    phone = len(nums)//2
    phone_nums = set(nums)
    if len(phone_nums) <= phone:
        answer = len(phone_nums)
    else:
        answer = phone
    return answer