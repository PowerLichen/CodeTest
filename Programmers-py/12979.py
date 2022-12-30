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
