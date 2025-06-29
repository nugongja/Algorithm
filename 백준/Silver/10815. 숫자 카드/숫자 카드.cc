#include <iostream>
#include <string>
#include <sstream>
#include <queue>
using namespace std;

int main() {
    int N;
    int M;
    
    cin >> N;
    cin.ignore();


    priority_queue<int, vector<int>, greater<int>> card;
    int tmp;
    for (int i = 0; i < N; i++) {
        cin >> tmp;
        card.push(tmp);
    }

    cin.ignore();


    cin >> M;
    cin.ignore();
    
    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> arr;
    for (int i = 0; i < M; i++) {
        cin >> tmp;
        arr.push({ tmp, i });
    }

    int* value = new int[M];
    while(!arr.empty()) {

        if (card.empty()) {
            value[arr.top().second] = 0;
            arr.pop();
            continue;
        }

        if (card.top() < arr.top().first) {
            card.pop();
        }
        else if (card.top() == arr.top().first) {
            card.pop();
            value[arr.top().second] = 1;
            arr.pop();
        }
        else {
            value[arr.top().second] = 0;
            arr.pop();
        }
    }

    for (int i = 0; i < M; i++) {
        cout << value[i] << " ";
    }

    return 0;
}