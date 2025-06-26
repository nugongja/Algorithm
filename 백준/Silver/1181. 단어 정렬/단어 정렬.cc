#include <iostream>
#include <queue>
#include <string>
#include <unordered_set>
using namespace std;

int main() {
	int N;
	string tmp;
	priority_queue<pair<int, string>, vector<pair<int, string>>, greater<>> pq;
	unordered_set<string> seen;

	cin >> N;
	cin.ignore();

	while (N-- > 0) {
		getline(cin, tmp);
		if (seen.count(tmp)) continue; 
		seen.insert(tmp);
		pq.push({static_cast<int>(tmp.size()), tmp});
	}

	while (!pq.empty()) {
		cout << pq.top().second << "\n";
		pq.pop();
	}

	return 0;
}