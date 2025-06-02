YEARS=["Year","2025","2026","2027","2028","2029","2030"]
MONTHS={
    "January":"01",
    "February":"02",
    "March":"03",
    "April":"04",
    "May":"05",
    "June":"06",
    "July":"07",
    "August":"08",
    "September":"09",
    "October":"10",
    "November":"11",
    "December":"12"
    }

def get_years():
    return YEARS

def get_months():
    months=list(MONTHS.keys())
    months.insert(0,"Month")
    return months

def get_days():
    days=[]
    for i in range(1,32):
        days.append(str(i).zfill(2))
    days.insert(0,"Day")
    return days

def get_numeric_month(m):
    return MONTHS[m]


