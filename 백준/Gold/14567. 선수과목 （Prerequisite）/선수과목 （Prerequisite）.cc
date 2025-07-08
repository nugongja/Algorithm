#include <iostream>
#include <string>
#include <vector>
#include <numeric>
using namespace std;

void solution() {
    int N, M, A, B;
    cin >> N >> M;

    vector<int> answer(N, 1);
    vector<vector<int>> parent(N);


    for (int i = 0; i < M; i++) {
        cin >> A >> B;
        parent[B - 1].push_back(A - 1);
    }

    for (int i = 0; i < N; i++) {
        for (int p : parent[i]) {
            answer[i] = max(answer[p] + 1, answer[i]);
        }
    }

    
    for (int k : answer) {
        cout << k << ' ';
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    solution();

    return 0;
}