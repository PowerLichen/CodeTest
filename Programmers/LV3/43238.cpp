// 이분탐색
// 입국심사

#include <vector>
#include <algorithm>

using namespace std;

long long solution(int n, vector<int> times) {
    long long answer = 0;
    long long left = 0;
    long long right = (long long)(*max_element(times.begin(), times.end())) * n;
    while (left <= right) {
        long long middle = (left + right) / 2;
        long long result = 0;
        for (int time : times)
            result += middle / time;

        if (result >= n) {
            right = middle - 1;
            answer = middle;
        }
        else {
            left = middle + 1;
        }
    }
    return answer;
}