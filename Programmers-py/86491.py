'''
86491: 최소직사각형
'''

def solution(sizes):
    size_w, size_h = 0,0
    for size in sizes:
        low,high = min(size), max(size)
        if size_w < low:
            size_w = low
        if size_h < high:
            size_h = high
    return size_w * size_h