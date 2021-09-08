// 2021 KAKAO BLIND RECRUITMENT
// 광고 삽입

#include <string>
#include <vector>
#define MIN(a,b) (a<b)?a:b;

using namespace std;

int parseTime(string time) {
    int result = 0;
    for (int i = 0; i < time.size(); i++) {
        int first = time[i++] - '0';
        int second = time[i++] - '0';
        result += first * 10 + second;
        if (i > 6) break;
        result *= 60;
    }

    return result;
}
string valueToTime(int time) {
    int hh = time / 3600;
    string hh_str = (hh < 10) ? "0" + to_string(hh) : to_string(hh);
    int mm = time % 3600 / 60;
    string mm_str = (mm < 10) ? "0" + to_string(mm) : to_string(mm);
    int ss = time % 60;
    string ss_str = (ss < 10) ? "0" + to_string(ss) : to_string(ss);

    return hh_str + ":" + mm_str + ":" + ss_str;
}
string solution(string play_time, string adv_time, vector<string> logs) {

    vector<pair<int, int>> play_data;
    int play_end = parseTime(play_time);
    int adv_len = parseTime(adv_time);
    vector<int> rt_count(play_end + 1, 0);

    for (string log : logs) {
        int log_play = parseTime(log.substr(0, 8));
        int log_end = parseTime(log.substr(9));
        //play_data.push_back(make_pair((log_play), parseTime(log_end)));
        rt_count[log_play] += 1;
        rt_count[log_end] -= 1;
    }
    // 각 시간별 시청자 수
    for (int i = 1; i <= play_end; i++) {
        rt_count[i] += rt_count[i - 1];
    }

    long long max_play_time = 0;
    for (int i = 0; i <= adv_len; i++) {
        max_play_time += rt_count[i];
    }
    long long cur_play_time = max_play_time;
    int result_time = 0;
    for (int i = 0; i <= play_end - adv_len; i++) {
        cur_play_time += rt_count[i + adv_len] - rt_count[i];
        if (cur_play_time > max_play_time) {
            max_play_time = cur_play_time;
            result_time = i + 1;
        }
    }
    string answer = valueToTime(result_time);
    return answer;
}