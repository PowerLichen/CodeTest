#include <iostream>
#include <string>

using namespace std;

int main() {
	int n, m;
	string s;
	int cnt = 0;

	cin >> n >> m;
	cin >> s;

	for (int i = 0; i < m; i++) {
		if (s[i] == 'I' && s[i+1] == 'O') {
			int check = 0;
			while (s[i + 1] == 'O' && s[i + 2] == 'I') {
				i += 2;
				check++;
				if (s[i] == 'I' && check == n) {
					check--;
					cnt++;
				}
			}
		}
	}

	cout << cnt;
}