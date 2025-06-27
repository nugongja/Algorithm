#include <iostream>
#include <string>
#include <sstream>
#include <queue>
#include <cmath>
using namespace std;

int main() {
    int N;
    string line;
    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<>> pq;
    
    cin >> N;
    cin.ignore();

    int* value = new int[N];


    getline(cin, line);

    istringstream iss(line);
    int num;
    int index = 0;
    while (iss >> num) {
        pq.push({ num, index++ });
    }

    int tmp = -pow(10, 9)-1;
    int count = -1;
    while (!pq.empty()) {
        pair<int, int> current = pq.top(); pq.pop();
        if (tmp < current.first) {
            value[current.second] = ++count;
            tmp = current.first;
        }
        else {
            value[current.second] = count;
        }
    }

    for (int i = 0; i < N; i++) {
        cout << value[i] << " ";
    }


    delete[] value;

    return 0;
}