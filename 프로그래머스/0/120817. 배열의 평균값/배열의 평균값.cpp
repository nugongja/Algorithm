#include <string>
#include <numeric>
#include <vector>

using namespace std;

double solution(vector<int> numbers) {
    double answer = 0;
    int len = numbers.size();
    int sum = accumulate(numbers.begin(), numbers.end(), 0);

    answer = static_cast<double>(sum) / len;

    return answer;
}
