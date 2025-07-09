#include <iostream>
#include <queue>
#include <vector>
#include <climits>
using namespace std;

const int INF = INT_MAX;


vector<int> Dijkstra(const vector<vector<pair<int, int>>>& graph, int start) {
    int V = graph.size();
    vector<int> dist(V, INF);
    dist[start] = 0;

    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<>> pq;
    pq.push({ 0, start });


    while (!pq.empty()) {
        pair<int, int> top = pq.top();
        int curr_dist = top.first;
        int curr_node = top.second;
        pq.pop();

        if (curr_dist > dist[curr_node]) continue;
        for (const auto& p : graph[curr_node]) {
            int next_weight = p.first;
            int next_node = p.second;
            int next_dist = curr_dist + next_weight;

            if (next_dist < dist[next_node]) {
                dist[next_node] = next_dist;
                pq.push({ next_dist, next_node });
            }
        }
    }

    return dist;

}

int solution() {
    int V;
    cin >> V;

    vector<vector<pair<int, int>>> graph(V);

    for (int i = 0; i < V; i++) {
        int from;
        cin >> from;

        --from; // 0-based index로 변환

        while (true) {
            int to;
            cin >> to;
            if (to == -1) break;

            int dist;
            cin >> dist;
            graph[from].push_back({ dist, to - 1 }); // 거리, 정점 번호 (0-based)
        }
    }

    int endpoint_1 = -1;

    vector<int> dist_from_0 = Dijkstra(graph, 0);
    int max_tmp = 0;

    for (int i = 0; i < V; i++) {
        if (dist_from_0[i] != INF && dist_from_0[i] > max_tmp) {
            max_tmp = dist_from_0[i];
            endpoint_1 = i;
        }
    }


    vector<int> dist_from_endpoint_1 = Dijkstra(graph, endpoint_1);
    int max_length = 0;

    for (int i = 0; i < V; i++) {
        if (dist_from_endpoint_1[i] != INF && dist_from_endpoint_1[i] > max_length) {
            max_length = dist_from_endpoint_1[i];
            endpoint_1 = i;
        }
    }

    cout << max_length << endl;

    return 0;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    solution();

    return 0;
}