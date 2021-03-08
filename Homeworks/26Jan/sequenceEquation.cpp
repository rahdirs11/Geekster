#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

vector<int> permutationEquation(vector<int> p) {
    vector<int> result;
    for (int i = 1; i <= static_cast<int>(p.size()); ++i) {
        int iIndex = distance(p.begin(), find(p.begin(), p.end(), i)) + 1;
        int y = distance(p.begin(), find(p.begin(), p.end(), iIndex)) + 1;
        result.push_back(y);
    }
    return result;
}


int main() {
    int n{}, v{};
    cin >> n;
    vector<int> p;
    for (int i = 0; i < n; ++i) {
        cin >> v;
        p.push_back(v);
    }
    for (auto value: permutationEquation(p)) {
        cout << value << " ";
    }
    cout << endl;
    return 0;
}