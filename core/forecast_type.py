from enum import Enum, unique


# what type of forecast we are parsing
@unique
class ForecastType(Enum):
    TODAY = 'today'
    WEEKDAYS = 'weekday'
    TENDAYS = 'tenday'
    WEEKEND = 'weekend'