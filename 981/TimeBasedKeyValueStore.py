class TimeMap:
    def __init__(self):
        self.keys = {}


    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.keys:
            self.keys[key] = SortedDict()
  
        self.keys[key][timestamp] = value


    def get(self, key: str, timestamp: int) -> str:
        if key not in self.keys: 
            return ""

        iterator = self.keys[key].bisect_right(timestamp)
        if iterator == 0:
            return ""

        return self.keys[key].peekitem(iterator - 1)[1]
