#include <bits/stdc++.h>
using namespace std;

const float pi = 3.14159265358979;

struct complex_num {
    double re, im;
};

struct polar {
    double freq, amp, phase;
    polar(double freq, double amp, double phase){
        freq = freq;
        amp = amp;
        phase = phase;
    }
};

vector<polar> dft(vector<complex_num> x){
    int N = x.size();
    vector<polar> X;
    for (int k = 0; k < N; k++){
        struct complex_num com_result;
        for (int n = 0; n < N; n++){
            float phi = (2 * pi * n * k) / N;
            com_result.re += x[n].re * cos(phi);
            com_result.im -= x[n].im * sin(phi);
        }
        com_result.re = com_result.re / N;
        com_result.im = com_result.im / N;

        double freq = k;
        double amp = sqrt(com_result.re * com_result.re + com_result.im * com_result.im);
        double phase = atan2(com_result.im, com_result.re);
        X.push_back({freq, amp, phase});
        // struct polar pol_result(freq, amp, phase);
        // X.emplace_back(pol_result);
    }
    return X;
}

int main(){
    vector<complex_num> a;
    for (int i = 0; i < 10; i++){
        struct complex_num temp;
        temp.re = i;
        temp.im = i;
        a.push_back(temp);
    }

    for (auto i = 0; i < 10; i++){
        cout << a[i].re << ' ' <<  a[i].im << ' ';
    }
    cout << endl;
    return 0;
}