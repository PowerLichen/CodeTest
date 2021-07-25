#include <iostream>
#include <vector>

using namespace std;

int result[41] = { -1 };

int fibonacci(int n) {
    if (n == 0) {
        result[0] = 0;
        return 0;
    }
    if (n == 1) {
        result[1] = 1;
        return 1;
    }
    if (result[n]>0)
        return result[n];
    
    return result[n] = fibonacci(n-1) + fibonacci(n-2);
}

int main() {
    int count;
    cin >> count;

    int max = -1;

    vector<int> numbers(count);
    for (int i = 0; i < count; i++) {
        cin >> numbers[i];
    }

    for (int i = 0; i < count; i++) {
        int num = numbers[i];
        if (num > max) {
            fibonacci(num);
            max = num;
        }
        if (num == 0)
            cout << 1<<' ' << 0<<endl;
        else {
            cout << result[num - 1] << ' ' << result[num] << endl;
        }
    }
}