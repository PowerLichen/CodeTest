def solution(A, B):
    answer = 0
    pa, pb = 0, 0
    end = len(B)
    A.sort(reverse=True)
    B.sort(reverse=True)
    
    while pa < len(A) and pb < end:
        if A[pa] <B[pb]:
            answer += 1
            pb += 1
        else:            
            end -= 1
        pa += 1
            
    return answer


solution(	[5, 1, 3, 7], [2, 2, 6, 8])