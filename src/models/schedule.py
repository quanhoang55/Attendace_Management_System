#==========================================================================
# IMPORTS & CONFIGURATION
#==========================================================================
from enum import IntEnum
from dataclasses import dataclass
from typing import Optional
#==========================================================================
# CLASSES / DATA STRUCTURE: Weekday-List, Period-List, Room-List
#==========================================================================

class WeekdayList(IntEnum):
    MODAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    SUNDAY = 7

class Room(IntEnum):
    NO1 = 1
    NO2 = 2
    NO3 = 3
    NO4 = 4
    NO5 = 5

# Uncertain, Change it Later
# period_list = []

#==========================================================================
# CLASSES / DATA STRUCTURE: Schedule
#==========================================================================
@dataclass
class Schedule:
    weekday: WeekdayList
    period: int
    room: Room