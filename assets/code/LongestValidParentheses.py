class Solution:
    def longestValidParentheses(self, s):
        pilha = [-1]
        res =  0 
        for i in range(len(s)):
            if s[i] == '(':
                pilha.append(i)
            else:
                pilha.pop()
                if len(pilha) == 0:
                    pilha.append(i)
                else:
                    res = max(res, (i - pilha[-1]))
        return res
    
#Testes

s = Solution()
print(s.longestValidParentheses("(()"))
print(s.longestValidParentheses(")()())"))
print(s.longestValidParentheses(""))

#Resultado: Runtime 31ms Memory 14.43MB