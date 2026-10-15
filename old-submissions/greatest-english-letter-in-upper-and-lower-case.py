class Solution:
    def greatestLetter(self, s: str) -> str:
        # ans = '`'
        # st = 'abcdefghijklmnopqrstuvwxyz'

        # for ch in st:
        #     if ch in s and ch.upper() in s:
        #         if ord(ch) > ord(ans):
        #             ans = ch

        # return ans.upper() if ans != '`' else ""

        s = set(s)
        st = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

        for ch in reversed(st):
            if ch in s and ch.lower() in s:
                return ch

        return ""