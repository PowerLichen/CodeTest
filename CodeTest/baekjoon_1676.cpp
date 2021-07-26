#include <iostream>
using namespace std;
#define MIN(a,b) (a<b ? a: b)

int main() {
	int n;
	cin >> n;
	int num_five = 0;

	for (int i = 5; i <= n; i *=5) {
		num_five += n / i;
	}

	cout << num_five <<endl;
}