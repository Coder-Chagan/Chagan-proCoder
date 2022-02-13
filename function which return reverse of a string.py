def ispolindrome(s):
	return s == s[::-1]

s = "malayalam"
ans = ispolindrome(s)

if ans:
	print("yes")
else:
	print("no")