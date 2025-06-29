#include <iostream>
#include <unordered_set>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int N,M, tmp;

    cin >> N;
    unordered_set<int> card;
    for (int i = 0; i < N; i++) {
        cin >> tmp;
        card.insert(tmp);
    }


    cin >> M;
    for (int i = 0; i < M; i++) {
        cin >> tmp;
        if (card.count(tmp) > 0) {
            cout << "1 ";
        }
        else {
            cout << "0 ";
        }
    }

    
    

    return 0;
}