class Solution:
    def minTimeToVisitAllPoints(self, points: list) -> list:
        """
        对角线时间短，位移长，优先对角线位移
        当x or y相等时，再竖直 or 水平位移
        再次分析：
        x差 和 y差最小数为对角线位移次数
        最大数-最小数 为水平or垂直位移次数
        """
        time = 0
        for i in range(len(points)-1):
            x1 = points[i][0]
            y1 = points[i][1]
            x2 = points[i+1][0]
            y2 = points[i+1][1]

            x_sub = abs(x1 - x2)
            y_sub = abs(y1 - y2)

            if x_sub >= y_sub:
                d_time = y_sub
                h_time = x_sub - y_sub
            else:
                d_time = x_sub
                h_time = y_sub - x_sub

            time += (d_time + h_time)

        return time


a = Solution().minTimeToVisitAllPoints([[1,1],[3,4],[-1,0]])
print(a)