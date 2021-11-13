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
    string temp;
    vector<complex<double>> x, y;
    vector<complex<double>> result_x, result_y;
    ifstream x_data, y_data;
    x_data.open("/home/supperman/Documents/linhtinh/x.txt", ios::in);
    y_data.open("/home/supperman/Documents/linhtinh/y.txt", ios::in);
    ofstream res_x, res_y;
    res_x.open("/home/supperman/Documents/linhtinh/(Python & C++) Fourier Transform and Epicycle/result_x.txt", ios::out | ios::app);
    res_y.open("/home/supperman/Documents/linhtinh/(Python & C++) Fourier Transform and Epicycle/result_y.txt", ios::out | ios::app); 
    while(x_data >> temp){
        float temp_0 = stof(temp);
        complex<double> adder (temp_0, 0);
        cout << adder.real() << ' ' << adder.imag() << endl;
        x.push_back(adder); 
    }
    while (y_data >> temp){
        float temp_0 = stof(temp);
        complex<double> adder (temp_0, 0);
        cout << adder.real() << ' ' << adder.imag() << endl;
        y.push_back(adder);
    }
    result_x = dft(x);
    result_y = dft(y);
    for (unsigned int k = 0; k < result_x.size() - 1; k++){
        int freq = k;
        float amp_x = abs(result_x.at(k));
        float phase_x = arg(result_x.at(k));
        float amp_y = abs(result_y.at(k));
        float phase_y = arg(result_y.at(k));

        res_x << "[" << freq << ", " << amp_x << ", " << phase_x << "]" << endl;
        cout << result_x.at(k) << endl;

        res_y << "[" << freq << ", " << amp_y << ", " << phase_y << "]" << endl;
        cout << result_y.at(k) << endl;

    }
    x_data.close();
    y_data.close();
    res_x.close();
    res_y.close();
    cout << "DONE!" << endl;
    return 0;
}