from enum import auto, unique
from .base_enum import BaseEnum


@unique
class Unit(BaseEnum):

    # enumeration for temp units
    # call generate_next_value property name as auto
    CELSIUS = auto()
    FAHRENHEIT = auto()