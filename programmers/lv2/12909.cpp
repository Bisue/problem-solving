// 올바른 괄호
// https://school.programmers.co.kr/learn/courses/30/lessons/12909

#include <string>
#include <stack>

using namespace std;

bool solution(string s)
{
    stack<char> st;
    
    for (char ch: s) {
        if (st.empty()) {
            st.push(ch);
        } else if (ch == ')' && st.top() == '(') {
            st.pop();
        } else {
            st.push(ch);
        }
    }
    
    return st.empty();
}
