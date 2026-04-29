#!/usr/bin/env python3
import calendar, json, os, subprocess, time, re
from datetime import date

CACHE = "/tmp/waybar_weather"

def get_weather():
    try:
        if os.path.exists(CACHE) and time.time() - os.path.getmtime(CACHE) < 1800:
            return open(CACHE).read().strip()
        r = subprocess.run(
            ["curl", "-sf", "wttr.in/?format=j1"],
            capture_output=True, text=True, timeout=5
        )
        d = json.loads(r.stdout)
        c = d['current_condition'][0]
        w = d['weather'][0]
        cond = c['weatherDesc'][0]['value']
        icons = {
            'sunny': '☀️', 'clear': '🌙', 'partly': '⛅', 'cloud': '☁️',
            'overcast': '☁️', 'rain': '🌧️', 'drizzle': '🌦️',
            'snow': '❄️', 'thunder': '⛈️', 'fog': '🌫️', 'mist': '🌫️'
        }
        icon = next((v for k, v in icons.items() if k in cond.lower()), '🌡️')
        result = f"{icon}  {cond}    {c['temp_F']}°F    ↑{w['maxtempF']}°F  ↓{w['mintempF']}°F"
        open(CACHE, 'w').write(result)
        return result
    except:
        return open(CACHE).read().strip() if os.path.exists(CACHE) else "Weather unavailable"

def display_len(s):
    return len(re.sub(r'<[^>]+>', '', s))

def pad_line(s, width):
    return s + ' ' * (width - display_len(s))

def add_border(lines):
    inner_w = max(display_len(l) for l in lines)
    top = '┌' + '─' * (inner_w + 2) + '┐'
    bot = '└' + '─' * (inner_w + 2) + '┘'
    result = [top]
    for line in lines:
        result.append('│ ' + pad_line(line, inner_w) + ' │')
    result.append(bot)
    return result

def get_calendar():
    today = date.today()
    month_lines = []

    for i in range(2):
        month = today.month + i
        year = today.year
        if month > 12:
            month -= 12
            year += 1

        cal = calendar.TextCalendar(calendar.MONDAY)
        lines = cal.formatmonth(year, month).strip().split('\n')
        out = []
        for line in lines:
            if year == today.year and month == today.month and str(today.day) in line.split():
                line = re.sub(
                    r'\b' + str(today.day) + r'\b',
                    f'<span color="#ff6b6b"><b>{today.day}</b></span>',
                    line, count=1
                )
            out.append(line)
        month_lines.append(add_border(out))

    # Pad both to same height
    max_lines = max(len(m) for m in month_lines)
    col_width = max(display_len(l) for l in month_lines[0])
    for m in month_lines:
        while len(m) < max_lines:
            m.append(' ' * col_width)

    combined = []
    for i in range(max_lines):
        combined.append(pad_line(month_lines[0][i], col_width) + '   ' + month_lines[1][i])

    return '\n'.join(combined)

weather = get_weather()
cal_text = get_calendar()
tooltip = f"<span size='large'>{weather}</span>\n\n<tt>{cal_text}</tt>"

print(json.dumps({"text": "󰃵", "tooltip": tooltip}))
