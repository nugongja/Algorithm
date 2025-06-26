#include <iostream>
#include <queue>
#include <string>
#include <set>
using namespace std;

int main() {
	int N;
	string tmp;
	priority_queue<pair<int, string>, vector<pair<int, string>>, greater<pair<int, string>>> pq;
	set<string> seen;

	cin >> N;
	cin.ignore();

	while (N-- > 0) {
		getline(cin, tmp);
		if (seen.find(tmp) != seen.end()) {
			continue; // Skip duplicates
		}
		pq.push(make_pair(tmp.size(), tmp));
		seen.insert(tmp);
	}

	while (!pq.empty()) {
		cout << pq.top().second << "\n";
		pq.pop();
	}

	return 0;
}