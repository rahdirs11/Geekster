#include <iostream>
#include <string>

std::string numToWord(int number) {
    std::string word[] = {"one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen", "twenty", "twenty one", "twenty two", "twenty three", "twenty four", "twenty five", "twenty six", "twenty seven", "twenty eight", "twenty nine"};
    return word[number - 1];
}


std::string timeInWords(int h, int m) {
    std::string time{};
    if (m == 0) {
        time = numToWord(h);
        return time + " o' clock";
    } else {
        if (m < 30) {
            time = numToWord(h);
            if (m != 15) {
                return m == 1? "one minute past " + time: numToWord(m) + " minutes past " + time;
            } else {
                return "quarter past " + time;
            }
        }
        else if (m == 30) {
            time = numToWord(h);
            return "half past " + numToWord(h);
        } else {
            time = numToWord(h + 1);
            if (60 - m == 15) {
                return "quarter to " + time;
            } else {
                return numToWord(60 - m) + " minutes to " + time;
            }
        }
    }
}


int main() {
    int h{}, m{};
    std::cin >> h >> m;
    std::cout << timeInWords(h, m) << std::endl;
    return 0;
}