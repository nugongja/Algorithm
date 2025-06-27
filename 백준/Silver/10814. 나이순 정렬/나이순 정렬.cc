#include <iostream>
#include <queue>
#include <string>
#include <sstream>
#include <tuple>
using namespace std;

struct Compare {
   bool operator()(const tuple<int, int, string>& a, const tuple<int, int, string>& b) {
       if (get<0>(a) == get<0>(b)) {
           return get<1>(a) > get<1>(b);
       }
       return get<0>(a) > get<0>(b);
   }
};

int main() {
   int N;
   int tmp_age;
   string tmp_name;
   priority_queue<tuple<int, int, string>, vector<tuple<int, int, string>>, Compare> pq;

   cin >> N;
   cin.ignore();

   for (int i = 0; i < N; i++) {
       string line;
       getline(cin, line);

       istringstream iss(line);
       iss >> tmp_age >> tmp_name;

       pq.push({tmp_age, i, tmp_name});
   }

   while (!pq.empty()) {
       tuple<int, int, string> top = pq.top(); // Explicitly declare the type of the tuple
       int age = get<0>(top);
       int order = get<1>(top);
       string name = get<2>(top);

       cout << age << " " << name << "\n";
       pq.pop();
   }

   return 0;
}