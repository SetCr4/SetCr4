import os, re, pathlib
from datetime import date, datetime
def inc_year(d: date) -> date: return date(d.year + 1, d.month, d.day)
bday = inc_year(datetime.strptime(os.environ.get("DOB", "1990-01-01"), "%Y-%m-%d"))
tday = date.today()
age = 0
while bday < tday:
    bday = inc_year(bday)
    age += 1
readme = pathlib.Path("README.md")
text = readme.read_text("utf-8")
readme.write_text(re.sub(r"<!-- MARKER:AGE -->(.*)<!-- EOM -->", f"<!-- MARKER:AGE -->{age}<!-- EOM -->", text), "utf-8")