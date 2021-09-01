//2019 카카오 개발자
// 튜플

#include <string>
#include <vector>
#include <algorithm>

using namespace std;

bool cmp(vector<int> a, vector<int> b) {
    return a.size() < b.size();
}

vector<int> stov_sort(string tuple) {
    vector<int> temp;
    int num = 0;
    // string to vector
    for (char ch : tuple) {
        if (ch != ',') {
            num *= 10;
            num += ch - '0';
        }
        else {
            temp.push_back(num);
            num = 0;
        }
    }
    temp.push_back(num);

    sort(temp.begin(), temp.end());

    return temp;
}

vector<int> solution(string s) {
    vector<int> answer;
    vector<vector<int>> tuples;
    int idx = 1;
    int len = 0;
    for (int i = 1; i < s.size(); i++) {
        if (s[i] == '}') {            
            tuples.push_back(stov_sort(s.substr(idx + 1, --len)));            
            idx = i + 2;
            len = 0;
            i++;
        }
        else {
            len++;
        }
    }
    sort(tuples.begin(), tuples.end(), cmp);

    answer.push_back(tuples[0][0]);
    for (int i = 1; i < tuples.size(); i++) {
        vector<int> temp(1);
        set_difference(tuples[i].begin(), tuples[i].end(), tuples[i - 1].begin(), tuples[i - 1].end(), temp.begin());
        answer.push_back(temp[0]);
    }
    return answer;
}