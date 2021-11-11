#include <bits/stdc++.h>
using namespace std;

const float pi = 3.14159265358979;

vector<complex<double>> dft(vector<complex<double>> x){
    int N = x.size();
    vector<complex<double>> X;
    for (int k = 0; k < N; k++){
        double re = 0;
        double im = 0;        
        for (int n = 0; n < N; n++){
            double phi = (2 * pi * k * n) / N;
            re += x[n].real() * cos(phi);
            im -= x[n].imag() * sin(phi);
        }
        complex<double> result (re, im);
        X.push_back(result);
    }
    return X;
}

int main(){
    vector<complex<double>> x;
    for (int i = 0; i < 100; i++){
        complex<double> adder (i, 0);
        complex<double> temp (0, 0);
        temp = temp + adder;
        x.push_back(temp);
    }
    vector<complex<double>> result;
    result = dft(x);
    for (auto i : result){
        cout << '(' << i.real() << ';' << i.imag() << "), ";
    }
    cout << endl;
    return 0;
}