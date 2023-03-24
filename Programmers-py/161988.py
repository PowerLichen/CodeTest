def solution(sequence):
    answer = 0
    
    pulse = 1
    pulse_sum1 = 0
    pulse_sum2 = 0
    
    for num in sequence:
        nxt_sum = pulse_sum1 + num * pulse
        if nxt_sum >= 0:
            pulse_sum1 = nxt_sum
            answer = max(answer, pulse_sum1)
        else:
            pulse_sum1 = 0
        
        pulse *= -1
        nxt_sum = pulse_sum2 + num * pulse
        if nxt_sum >= 0:
            pulse_sum2 = nxt_sum
            answer = max(answer, pulse_sum2)
        else:
            pulse_sum2 = 0
        
    return answer