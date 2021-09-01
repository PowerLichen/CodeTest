// 2018 KAKAO BLIND
// 방금그곡

#include <sstream>
#include <string>
#include <vector>

using namespace std;
vector<string> parsing_info(string s) {
    vector<string> result;
    istringstream ss(s);
    string token;
    result.reserve(3);

    while (getline(ss, token, ',')) {
        result.push_back(token);
    }
    return result;
}

int get_play_length(string start, string end) {
    int start_h = stoi(start.substr(0, 2));
    int end_h = stoi(end.substr(0, 2));
    int hour_len = 
        (start_h <= end_h) ? end_h - start_h : end_h + 24 - start_h;

    return hour_len * 60 + (stoi(end.substr(3, 2)) - stoi(start.substr(3, 2)));
}

string solution(string m, vector<string> musicinfos) {
    string answer = "(None)";
    int answer_music_len = 0;
    for (string raw : musicinfos) {
        vector<string> info = parsing_info(raw);
        int play_len = get_play_length(info[0], info[1]);
        //현재 찾은 곡 보다 재생시간이 짧은 경우 skip
        if (answer_music_len > play_len)
            continue;

        string music = info[3];
        int melody_len = 0;
        for (char ch : music)
            if (ch != '#') melody_len++;

        int cur_music = 0;
        //play data
        bool find = false;
        for (int i = 0; cur_music < play_len; i++) {
            if (music[i % music.size()] == m[0]) {
                int cur_melody;
                for (cur_melody = 1; cur_melody < m.size(); cur_melody++) {
                    if (music[(i + cur_melody) % music.size()] != m[cur_melody])
                        break;
                }
                if (cur_melody == m.size() && music[(i + cur_melody) % music.size()] != '#') {
                    find = true;
                    break;
                }
            }
            if (music[i % music.size()] != '#')
                cur_music++;
        }

        if (find) {
            if (answer_music_len < play_len) {
                answer = info[2];
                answer_music_len = play_len;
            }
        }
    }
    return answer;
}