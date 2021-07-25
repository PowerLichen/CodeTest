#include <iostream>
#include <cmath>

using namespace std;

int check_z[2][2] = { {0,1},{2,3} };

int z_check(int n, int r, int c) {
	if (n == 0)
		return 0;
	int num = pow(2, n - 1);

	return num*num * check_z[r / num][c / num] + z_check(n - 1, r % num, c % num);
}


int main() {
	int n, r, c;
	cin >> n >> r >> c;

	int result = z_check(n, r, c);
	cout << result;
}