// 멀쩡한 사각형

#include <cmath>

using namespace std;

int gcd(int a, int b) {
    if (b == 0) return a;
    return gcd(b, a % b);
}

long long solution(int w,int h) {
    long long answer = (long long)w * h;

    int gcf = gcd(w, h);

    double y0, y1;
    for (int i = 0; i < w / gcf; i++) {
        y0 = (double)i * h / w;
        y1 = y0 + (double)h / w;
        answer -= gcf*(ceil(y1) - floor(y0));
    }
    return answer;
}