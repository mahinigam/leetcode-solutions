class ExamTracker:

    def __init__(self):
        self.times = []
        self.prefix_sums = []

    def record(self, time: int, score: int) -> None:
        midway = (time, score)

        self.times.append(time)
        if self.prefix_sums:
            self.prefix_sums.append(self.prefix_sums[-1] + score)
        else:
            self.prefix_sums.append(score)

    def totalScore(self, startTime: int, endTime: int) -> int:
        left = bisect.bisect_left(self.times, startTime)
        right = bisect.bisect_right(self.times, endTime) - 1

        if left > right:
            return 0

        total = self.prefix_sums[right]
        if left > 0:
            total -= self.prefix_sums[left - 1]
        return total


# Your ExamTracker object will be instantiated and called as such:
# obj = ExamTracker()
# obj.record(time,score)
# param_2 = obj.totalScore(startTime,endTime)