class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        trie = {}

        temp = trie
        for word in dictionary:
            for c in word:
                temp = temp.setdefault(c, {})
            temp['.'] = '.'
            temp = trie
        
        def find(p):
            d = trie

            prefix = ""
            for c in p:
                prefix += c
                d = d.get(c)
                if d is None:
                    return False
                else:
                    if '.' in d:
                        return prefix

            return prefix if '.' in d else False

        words = sentence.split(" ")

        for i in range(len(words)):
            fword = find(words[i])
            if fword:
                words[i] = fword

        return " ".join(words)