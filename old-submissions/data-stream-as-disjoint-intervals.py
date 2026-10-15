from sortedcontainers import SortedDict


class SummaryRanges:
  def __init__(self):
    self.intervals = SortedDict()

  def addNum(self, val: int) -> None:
    if val in self.intervals:
      return

    lo = self._lowerKey(val)
    hi = self._higherKey(val)

    if lo >= 0 and hi >= 0 and self.intervals[lo][1] + 1 == val and val + 1 == hi:
      self.intervals[lo][1] = self.intervals[hi][1]
      del self.intervals[hi]
    elif lo >= 0 and self.intervals[lo][1] + 1 >= val:
      self.intervals[lo][1] = max(self.intervals[lo][1], val)
    elif hi >= 0 and val + 1 == hi:
      self.intervals[val] = [val, self.intervals[hi][1]]
      del self.intervals[hi]
    else:
      self.intervals[val] = [val, val]

  def getIntervals(self) -> list[list[int]]:
    return list(self.intervals.values())

  def _lowerKey(self, key: int):
    i = self.intervals.bisect_left(key)
    if i == 0:
      return -1
    return self.intervals.peekitem(i - 1)[0]

  def _higherKey(self, key: int):
    i = self.intervals.bisect_right(key)
    if i == len(self.intervals):
      return -1
    return self.intervals.peekitem(i)[0]