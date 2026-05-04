from unittest.mock import Mock
from datetime import datetime

tuesday = datetime(year=2026, month=5, day=5)
print(tuesday)
sunday = datetime(year=2026, month=5, day=10)
print(sunday)
new_year = datetime(year=2026, month=12, day=31)
print(new_year)

datetime = Mock()
print(datetime)


def is_weekday():
    today = datetime.today()
    return 0 <= today.weekday() < 5


datetime.today.return_value = tuesday
print(datetime.today())
print(is_weekday())
assert is_weekday(), "Not workday!"

datetime.today.return_value = sunday
print(datetime.today())
print(is_weekday())
assert is_weekday(), "Not workday!"

# datetime.today.return_value = new_year
# print(datetime.today())
# print(is_weekday())
# assert is_weekday(), "Not workday!"
