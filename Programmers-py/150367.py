def is_bintree(b_num, start, end, is_zero):
    if start > end:
        return 1

    mid = (start + end) // 2
    if is_zero and (b_num[mid] == "1"):
        return 0

    if b_num[mid] == "0":
        is_zero = True

    check_left = is_bintree(b_num, start, mid-1, is_zero)
    check_right = is_bintree(b_num, mid+1, end, is_zero)
    return check_left & check_right


def solution(numbers):
    result = []
    for num in numbers:
        b_num = str(bin(num))[2:]
        length = len(b_num)

        depth = 1
        while length > 2**depth - 1:
            depth += 1

        b_num = "0"*(2**depth - 1 - length) + b_num
        answer = is_bintree(b_num, 0, len(b_num)-1, False)
        result.append(answer)

    return result
