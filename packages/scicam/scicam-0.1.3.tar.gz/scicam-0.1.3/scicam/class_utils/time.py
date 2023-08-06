import time

class TimeUtils:
    
    @property
    def running_for_seconds(self):
        return time.time() - self.start_time
       
    def tick(self, target):

        get = self._last_ticks.get(target, 0)
        answer = (get + target) < self._time_s# or get == 0

        if answer:
            self._last_ticks[target] = self._time_s
        
        return answer
