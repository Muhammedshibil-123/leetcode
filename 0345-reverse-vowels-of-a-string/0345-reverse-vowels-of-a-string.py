class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels=[]
        indnumber=[]
        for i in range(len(s)):
            if s[i]=="A" or s[i]=="a" or  s[i]=='E' or s[i]=='e' or s[i]=='I' or s[i]=='i' or s[i]=='O' or s[i]=='o'or s[i]=='U' or s[i]=='u':
                vowels.append(s[i])
                indnumber.append(i)
            else:
                continue
        vowelsR=vowels[::-1]
        print(vowelsR,indnumber)
        
        f=list(s)
        for i in range(len(vowelsR)):
            f[indnumber[i]]=vowelsR[i]
        return ''.join(f)
            

            