'''
120863: 다항식 더하기
'''
def term_to_int(n_str):
    if n_str == '':
        return 1
    return int(n_str)
    

def solution(polynomial):
    terms = polynomial.split(' + ')
    
    lin, cnst = 0, 0
    for term in terms:
        if term[-1] == "x":
            lin += term_to_int(term[:-1])
        else:
            cnst += term_to_int(term)
            
    result = list()
    if lin > 0:
        if lin == 1:
            result.append('x')
        else:
            result.append(f'{lin}x')
    if cnst > 0:
        result.append(f'{cnst}')
        
    return ' + '.join(result)