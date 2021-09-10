#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int to_numtime(string time) {
	int result = 0;
	//HH
	result += (time[0] - '0') * 10 + (time[1] - '0');
	result *= 60;
	//MM
	result += (time[3] - '0') * 10 + (time[4] - '0');

	return result;
}
string to_time(int t_num) {
	string time = "00:00";
	time[0] += t_num / 600;
	time[1] += (t_num / 60) % 10;
	time[3] += (t_num % 60) / 10;
	time[4] += (t_num % 60) % 10;
	return time;
}

string solution(int n, int t, int m, vector<string> timetable) {
	sort(timetable.begin(), timetable.end(), less<>());

	// bus_time 09:00 = 9*60 = 540
	int last_bus_time = 540 + (n - 1) * t;
	int last_member;
	int idx = 0;
	//���� ������ ��� ������
	for (int bus_time = 540; bus_time < 540 + (n - 1) * t; bus_time += t) {
		for (int i = 0; i < m; i++) {
			if (idx == timetable.size())
				break;
			int t_num = to_numtime(timetable[idx]);
			if (t_num > bus_time) {
				break;
			}
			idx++;
		}
	}
	//������ ��ٸ��� idx ���
	int idx_last;
	for (idx_last = idx; idx_last < timetable.size(); idx_last++) {
		if (to_numtime(timetable[idx_last]) > last_bus_time)
			break;
	}
	int result_time;
	//���� ���
	if (idx_last - idx < m) {
		//���� ��� �¿��� �ڸ��� ����
		result_time = last_bus_time;
	}
	else {
		//���� ��� �� ���¿�
		result_time = to_numtime(timetable[idx + m - 1]) - 1;
	}

	return to_time(result_time);
}