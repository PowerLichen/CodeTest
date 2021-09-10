//2020 카카오 인턴십
//보석 쇼핑

#include <string>
#include <vector>
#include <unordered_map>

using namespace std;

vector<int> solution(vector<string> gems) {
    vector<int> answer(2, 0);
    unordered_map<string, int> cur_gems;

    //보석 개수 초기화
    for (string gem : gems) {
        cur_gems[gem];
    }
    int total_gem_cnt = cur_gems.size();
    int start = 0, end = 1;
    int cur_len;

    //맵 초기화
    cur_gems.clear();
    cur_gems[gems[0]]++;

    int min_len = 100001;

    while (start < end) {
        cur_len = end - start;
        if (cur_gems.size() == total_gem_cnt) {
            if (min_len > cur_len) {
                min_len = cur_len;
                answer[0] = start;
                answer[1] = end;
            }

            if (cur_gems[gems[start]] == 1)
                cur_gems.erase(gems[start]);
            else
                cur_gems[gems[start]]--;
            start++;
        }
        else {
            if (end == gems.size())
                break;
            cur_gems[gems[end]]++;
            end++;
        }
    }
    answer[0]++;
    return answer;
}