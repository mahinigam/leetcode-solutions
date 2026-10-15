class Solution:
  def wordBreak(self, s: str, wordDict: list[str]) -> list[str]:
    wordSet = set(wordDict)

    @functools.lru_cache(None)
    def wordBreak(s: str) -> list[str]:
      ans = []

      for i in range(1, len(s)):
        prefix = s[:i]
        suffix = s[i:]
        if prefix in wordSet:
          for word in wordBreak(suffix):
            ans.append(prefix + ' ' + word)

      if s in wordSet:
        ans.append(s)

      return ans

    return wordBreak(s)