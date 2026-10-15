class Solution:
  def successfulPairs(self, spells: list[int], potions: list[int], success: int) -> list[int]:
    potions.sort()

    def firstIndexSuccess(spell: int):
      l = 0
      r = len(potions)
      while l < r:
        m = (l + r) // 2
        if spell * potions[m] >= success:
          r = m
        else:
          l = m + 1
      return l

    return [len(potions) - firstIndexSuccess(spell) for spell in spells]