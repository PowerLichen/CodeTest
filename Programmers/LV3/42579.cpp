//해시
//베스트 앨범

#include <string>
#include <vector>
#include <unordered_map>
#include <algorithm>

using namespace std;

vector<int> solution(vector<string> genres, vector<int> plays) {
    vector<int> answer;
    vector<vector<int>> m_info;
    vector<string> genre_list;
    unordered_map <string, vector<int>> datas;

    for (int i = 0; i < genres.size(); i++) {
        string target = genres[i];
        int play_time = plays[i];

        switch (datas[target].size()) {
        case 0:
            genre_list.push_back(target);
            datas[target].push_back(0);
        case 1:
            datas[target].push_back(i);
            break;
        case 2:
            if (plays[datas[target][1]] < play_time) {
                datas[target].push_back(datas[target][1]);
                datas[target][1] = i;
            }
            else {
                datas[target].push_back(i);
            }
            break;
        default:
            if (plays[datas[target][1]] < play_time) {
                datas[target][2] = datas[target][1];
                datas[target][1] = i;
            }
            else if (plays[datas[target][2]] < play_time)
                datas[target][2] = i;
        }
        datas[target][0] += play_time;
    }

    for (string genre : genre_list) {
        m_info.push_back(datas[genre]);
    }
    sort(m_info.begin(), m_info.end(), greater<>());
    for (vector<int> v : m_info) {
        for (int i = 1; i < v.size(); i++)
            answer.push_back(v[i]);
    }
    return answer;
}