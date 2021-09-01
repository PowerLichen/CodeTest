// 2021 KAKAO BLIND
// 메뉴 리뉴얼

#include <string>
#include <vector>
#include <unordered_map>
#include <algorithm>

using namespace std;

bool selected[26];
int max_count;

//arr에서 num개 크기를 가진 조합
void getOrderSet(unordered_map<string, int>& orderlist, vector<char>& arr, int num, int idx) {
    if (num == 0) {
        string temp="";
        for (int i = 0; i < 26; i++) {
            if (selected[i])
                temp += i + 'A';
        }
        orderlist[temp]++;
        if (max_count < orderlist[temp])
            max_count = orderlist[temp];

    }
    for (int i = idx; i < arr.size(); i++) {
        if (selected[arr[i]-'A']) continue;
        selected[arr[i] - 'A'] = true;
        getOrderSet(orderlist, arr, num-1, i);
        selected[arr[i] - 'A'] = false;
    }    
}

vector<string> solution(vector<string> orders, vector<int> course) {
    vector<string> answer;
    vector<unordered_map<string, int>> orderset(course.size(), unordered_map<string, int>());
        
    for (int n = 0; n < course.size(); n++) {
        // 전역변수 초기화
        max_count = 0;
        for (int i = 0; i < 26; i++) {
            if (selected[i])
                selected[i] = false;
        }
        //가능한 조합 반환
        for (string order : orders) {
            vector<char> temp;
            for (char c : order) {
                temp.push_back(c);
            }
            getOrderSet(orderset[n], temp, course[n], 0);            
        }
        
        if (max_count > 1) {
            for (auto& i : orderset[n]) {
                if (i.second == max_count)
                    answer.push_back(i.first);
            }
        }
    }    
    // 오름차순 정렬
    sort(answer.begin(), answer.end());
    return answer;
}