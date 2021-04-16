'''
https://leetcode.com/problems/design-log-storage-system/

binary search
bisect:maintaining a list in sorted order
https://docs.python.org/3/library/bisect.html

'''


class LogSystem:
    def __init__(self):
        self.time_id_map = {}
        self.times = []
        self.granularity_filter = {'Year': 4, 'Month': 7, 'Day': 10, 'Hour':13, 'Minute':16, 'Second':19}
        self.start_min_range = '0000:01:01:00:00:00'
        self.end_max_range = '9999:12:31:59:59:59'
        

    def put(self, id: int, timestamp: str) -> None:
        self.time_id_map[timestamp] = id
        i = bisect.bisect(self.times, timestamp)
        self.times[i:i] = [timestamp]
        

    def retrieve(self, start: str, end: str, granularity: str) -> List[int]:
        k = self.granularity_filter[granularity]
        start = start[:k] + self.start_min_range[k:]
        end = end[:k] + self.end_max_range[k:]
        
        i = bisect.bisect_left(self.times, start)
        j = bisect.bisect_right(self.times, end)
        
        return [self.time_id_map[time_stamp] for time_stamp in self.times[i:j]]