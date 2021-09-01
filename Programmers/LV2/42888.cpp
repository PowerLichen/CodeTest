#include <string>
// KAKAO BLIND 2019
// 오픈 채팅방

#include <vector>
#include <sstream>
#include <unordered_map>
#include <utility>

using namespace std;

vector<string> split(const string& raw) {
    vector<string> ans;
    stringstream ss(raw);
    string temp;
    while (getline(ss, temp, ' ')) {
        ans.push_back(temp);
    }
    return ans;
}

vector<string> solution(vector<string> record) {
    vector<string> answer;
    unordered_map<string, string> user_list;
    vector<pair<string, bool>> chat_list;

    for (string query : record) {
        vector<string> querydata = split(query);
        if (query[0] == 'C') {
            user_list[querydata[1]] = querydata[2];
        }
        else if(query[0] == 'E') {
            chat_list.push_back(make_pair(querydata[1],true));
            user_list[querydata[1]] = querydata[2];
        }
        else {
            chat_list.push_back(make_pair(querydata[1], false));
        }
    }

    for (auto it = chat_list.begin(); it != chat_list.end(); it++) {
        string name = user_list[(*it).first];
        string state;
        if ((*it).second)
            state = "님이 들어왔습니다.";
        else
            state = "님이 나갔습니다.";
        answer.push_back(name + state);

    }
    return answer;
}