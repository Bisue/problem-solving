# 최장 길이 공통 부분 문자열
# https://study.helloalgo.co.kr/study/1019/room/604/6616

"""
LCS1: ~ Subsequence
LCS2: ~ Substring
이 문제는 LCS1 인듯?
"""

"""
LCS1:
dp[i][j]: S[:i], T[:j]의 LCS1
dp[i][j] = if S[i] == T[j] then dp[i-1][j-1] + 1
           else then max(dp[i-1][j], dp[i][j-1])
		   
LCS2:
dp[i][j]: S[i], T[j]를 꼭 포함하는 S[:i], T[:j]의 LCS2
dp[i][j] = if S[i] == T[j] then dp[i-1][j-1] + 1
           else then 0
"""

S = input()
T = input()

dp = [[0 for _ in range(len(T)+1)] for _ in range(len(S)+1)]
for i in range(1, len(S)+1):
	for j in range(1, len(T)+1):
		if S[i-1] == T[j-1]:
			dp[i][j] = dp[i-1][j-1] + 1
		else:
			dp[i][j] = max(dp[i-1][j], dp[i][j-1])

#for row in dp:
#  	 print(row)
print(dp[len(S)][len(T)])
