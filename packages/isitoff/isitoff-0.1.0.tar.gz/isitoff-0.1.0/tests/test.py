from datetime import date

from src.isitoff import Isitoff

isitoff = Isitoff()
today = date.today()
mp = isitoff.get_gregorian(today)

print(mp.is_holiday)
print(mp["events"])
