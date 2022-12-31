"""
12979: 기지국 설치
n 만큼의 일렬로 된 아파트가 있고,  stations 위치에 타워가 설립되어 있다.
이 때, 타워가 w 만큼의 전파 범위를 가지고 있을 때 몇개를 더 세우면 아파트 전체를 커버할 수 있는가?
"""
def get_station_num(space, station_size):
    if space < 0:
        return 0

    result = space // station_size
    if space % station_size != 0:
        result += 1

    return result


def solution(n, stations, w):
    answer = 0
    station_size = (2 * w) + 1
    start = 1
    for station in stations:
        end = station - w - 1
        if start <= end:
            space = end-start+1
            answer += get_station_num(space, station_size)

        start = station + w + 1

    space = n-start+1
    answer += get_station_num(space, station_size)

    return answer
