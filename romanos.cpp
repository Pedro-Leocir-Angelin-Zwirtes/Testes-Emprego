#include <iostream>
#include <vector>
#include <string>

using namespace std;

int main(int argc, char const *argv[]) {
    int n_recebido, i, j, x;

    vector<string> numeros_romanos = {
        "M","CM", "D", "CD", "C", "XC", "L", "XL", "X",
        "IX", "V", "IV", "I"
    };
    
    vector<int> numeros = {
        1000,900,500,400,100,90,50,40,10,9,5,4,1
    };
    
    string romanos = "";
    
    cin >> n_recebido;
    
    for (i = 0; i < 13; i++){
        j = n_recebido / numeros[i];
        for (x = 1; x <= j; ++x){
            romanos = romanos + numeros_romanos[i];
        }
        n_recebido = n_recebido - numeros[i] * j;
    }
    cout << romanos;
    
    return 0;
    
}
