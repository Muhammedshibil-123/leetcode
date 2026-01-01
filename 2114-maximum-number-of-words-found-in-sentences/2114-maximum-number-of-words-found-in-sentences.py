class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        result=[]
        for i in range(len(sentences)):
            word=sentences[i].split(' ')
            result.append(len(word))
        return max(result)