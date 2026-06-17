#==========================================================================
# IMPORTS & CONFIGURATION
#==========================================================================
from enum import IntEnum
from dataclasses import dataclass
#==========================================================================
# CLASSES / DATA STRUCTURE: Weekday, Period, Room
#==========================================================================
class Weekday(IntEnum):
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    SUNDAY = 7

class Period(IntEnum):
    WEEK1 = 1
    WEEK2 = 2
    WEEK3 = 3
    WEEK4 = 4
    WEEK5 = 5

class Room(IntEnum):
    NO1 = 1
    NO2 = 2
    NO3 = 3
    NO4 = 4
    NO5 = 5

#==========================================================================
# CLASSES / DATA STRUCTURE: Schedule
#==========================================================================
@dataclass
class Schedule:
    weekday: Weekday
    period: Period
    room: Room