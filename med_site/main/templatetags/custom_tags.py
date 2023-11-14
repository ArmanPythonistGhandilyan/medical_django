from django import template
from datetime import datetime, timedelta

register = template.Library()

@register.filter
def current_date_plus_x_days(value):
    if value:
        try:
            days = int(value)
        except ValueError:
            days = 0
        new_date = datetime.now() + timedelta(days=days)
        formatted_date = new_date.strftime("%Y-%m-%d")
        weekday = new_date.strftime("%A")  # Format to get the weekday
        return f"{formatted_date} {weekday}"
    return value

