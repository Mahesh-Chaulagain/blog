from datetime import datetime

today = datetime.now()

date = {
            "month": today.strftime("%B"),  # get full month name
            "day": today.day,
            "year": today.year
        }

print(date["month"], date["day"], date["year"])