import requests
from datetime import datetime, timedelta
import pytz
from pytz import timezone
from dateutil import parser


API_KEY = "" # your api key from the app
BASE_URL = "https://api.habitify.me"

headers = {"Authorization": API_KEY}

# 1.get week range
local_tz = timezone("Europe/Prague")
now = datetime.now(local_tz)

start = now - timedelta(days=now.weekday())
end = start + timedelta(days=6)

# ISO with explicit offset (CEST +02:00)
start_str = start.strftime("%Y-%m-%dT00:00:00+02:00")
end_str = end.strftime("%Y-%m-%dT23:59:59+02:00")

# 2.fetch habits
r = requests.get(f"{BASE_URL}/habits", headers=headers)
if r.status_code != 200:
    print("Failed to fetch habits:", r.text)
    exit()

habits = r.json().get("data", [])
log_lookup = {}

# 3. fetch logs per habit
for h in habits:
    hid, name = h["id"], h["name"]
    url = f"{BASE_URL}/logs/{hid}"
    params = {"from": start_str, "to": end_str}
    r2 = requests.get(url, headers=headers, params=params)

    if r2.status_code != 200:
        print(f"Logs error for {name}:", r2.text)
        continue

    for log in r2.json().get("data", []):

        for log in r2.json().get("data", []):
            utc_dt = parser.isoparse(log["created_date"])
            local_dt = utc_dt.astimezone(local_tz)
            date = local_dt.strftime("%Y-%m-%d")
            log_lookup[(hid, date)] = True

# 4. prepare HTML
days = [(start + timedelta(days=i)).strftime("%a %d") for i in range(7)]
html = f"""
<html>
<head>
  <meta charset="UTF-8">
  <title>Habitify Weekly Log</title>
  <style>
    body {{ font-family: Arial; background: #f7f7f7; padding: 2rem; }}
    table {{ border-collapse: collapse; width: 100%; background: white; box-shadow: 0 2px 10px #ccc; }}
    th, td {{ border: 1px solid #ddd; padding: 8px; text-align: center; }}
    th {{ background-color: #f2f2f2; }}
    td:first-child, th:first-child {{ text-align: left; }}
  </style>
</head>
<body>
<h2>This Week's Habits ({start.date()} to {end.date()})</h2>
<table>
<tr><th>Habit</th>""" + "".join(f"<th>{day}</th>" for day in days) + "</tr>"

# 5. fill rows
for h in habits:
    html += f"<tr><td>{h['name']}</td>"
    for i in range(7):
        date_key = (start + timedelta(days=i)).strftime("%Y-%m-%d")
        mark = "✅" if (h["id"], date_key) in log_lookup else "❌"
        html += f"<td>{mark}</td>"
    html += "</tr>\n"

html += "</table></body></html>"

# 6. save file
with open("weekly_log.html", "w", encoding="utf-8") as f:
    f.write(html)

print("HTML report saved as weekly_log.html")

