#include <iostream>
#include <vector>

using namespace std;

int jumpingOnClouds(vector<int> c) {
    int jumps{}, i{};
    int n = static_cast<int>(c.size());
    while (i < n - 1) {
        if (i + 2 < n && c.at(i + 2) != 1) {
            i += 2;
        } else {
            ++i;
        }
        ++jumps;
    }
    return jumps;
}

int main() {
    int n{}, c{};
    cin >> n;
    vector<int> clouds(n);
    for (int i = 0; i < n; ++i) {
        cin >> c;
        clouds.at(i) = c;
    }
    cout << jumpingOnClouds(clouds) << endl;
    return 0;
}