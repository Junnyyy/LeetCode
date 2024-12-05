import datetime

class Solution:
  def daysBetweenDates(self, date1: str, date2: str) -> int:
    isoDate1 = datetime.date.fromisoformat(date1)
    isoDate2 = datetime.date.fromisoformat(date2)
    
    delta = isoDate1 - isoDate2
    
    return abs(delta.days)
    
