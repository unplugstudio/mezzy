from __future__ import absolute_import, unicode_literals

from datetime import date, datetime

from operator import attrgetter

from django import template
from django.utils.timezone import now

register = template.Library()


@register.filter
def next_start_dt(event, after_date=None):
    """
    Get the first occurrence of an event after a given date.
    If no occurrence is found, the first occurrence is returned.
    """
    if not isinstance(after_date, (date, datetime)):
        after_date = now()
    dt = event.dateandtimes.filter(day__gte=after_date).first()
    if dt is None:
        return event.dateandtimes.first()
    return dt


@register.filter
def annotate_start_dts(events, after_date=None):
    """
    Annotate each Event in a queryset with the next upcoming occurrence (EventDateTime).
    Then sort by this new computed field.
    """
    for event in list(events):
        event.next_start_dt = next_start_dt(event, after_date)
    return sorted(events, key=attrgetter('next_start_dt.day'))
