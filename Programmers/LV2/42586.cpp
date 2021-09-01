//기능 개발

#include <string>
#include <vector>

using namespace std;

vector<int> solution(vector<int> progresses, vector<int> speeds) {
    vector<int> answer;
    int len = progresses.size();
    int end_idx = 0;
    int count = 0;
    while (end_idx< len) {
        for (int i = 0; i < len; i++) {
            if (progresses[i] < 100)
                progresses[i] += speeds[i];
        }
        if (progresses[end_idx] >= 100) {
            int i;
            for (i = end_idx; i< len && progresses[i] >= 100; i++)
                count++;
            answer.push_back(count);
            count = 0;
            end_idx = i;
        }
    }
    return answer;
}

//다른 풀이
vector<int> solution_other(vector<int> progresses, vector<int> speeds) {
    vector<int> answer;

    int day;
    int max_day = 0;
    for (int i = 0; i < progresses.size(); ++i)
    {
        day = (99 - progresses[i]) / speeds[i] + 1;

        if (answer.empty() || max_day < day)
            answer.push_back(1);
        else
            ++answer.back();

        if (max_day < day)
            max_day = day;
    }

    return answer;
}