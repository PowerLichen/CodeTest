// 월간 코드 챌린지?
// 2개 이하로 다른 비트

#include <vector>

using namespace std;

vector<long long> solution(vector<long long> numbers) {
    vector<long long> answer;
    for (long long num : numbers) {
        //짝수
        if ((num & 1) == 0)
            answer.push_back(num + 1);
        //홀수
        else {
            long long temp = num;
            long long count=0;
            while (true) {
                count++;
                temp = temp >> 1;
                if ((temp & 1) == 0)
                    break;
            }
            temp = (temp + 1) << 1;
            temp = temp << (count - 1);
            temp += ((long long)1 << (count - 1)) -1;
            answer.push_back(temp);
        }
    }

    return answer;
}