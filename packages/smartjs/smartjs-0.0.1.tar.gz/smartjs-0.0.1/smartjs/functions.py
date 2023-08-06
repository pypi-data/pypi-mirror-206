__all__ = [
        'age',
        'list_filtered',
        'list_of_strings',
        'join',
        'dict_filtered',
        'split',
        'now',
        'normalize',
        'camel_case',
        'today_isoformat',
        'today',
        'now_isoformat',
        'cap_words_case',
        'slug',
        'split_lines',
        'remove_whitespace_before_final_point',
        'remove_extra_whitespaces',
        'repr_dict',
        'remove_html_extra_whitespaces',
        'capitalize',
        'get_words',
        'split_strip',
        'string_to_number',
        'get_list_of_numbers',
        'get_string_list_of_digits',
        'only_decimals',
        'get_group_or_return_none',
        'get_group_or_return_value',
        'get_iso_datetimes',
        'get_iso_dates',
        'get_first_iso_datetime',
        'get_first_iso_date'
]

import calendar
import re
import datetime
from typing import Sequence, Callable, Optional, Union
from unidecode import unidecode


Number = Union[int, float]


YEAR_PATTERN = re.compile(r'\b(19|20)\d{2}\b')

DAY_PATTERN = re.compile(r'\b([0-2]\d|3[0-1])\b')

MONTH_PATTERN = re.compile(r'\b(0\d|1[0-2])\b')

ISO_DATE_PATTERN = re.compile(r'(19|20)(\d{2})(-)(01|02|03|04|05|06|07|08|09|10|11|12)(-)([0-3]\d)')

ISO_DATETIME_PATTERN = re.compile(r'(19|20)(\d{2})(-)(01|02|03|04|05|06|07|08|09|10|11|12)(-)([0-3]\d)(T)([0-1]\d|2[0-3])(:)([0-5]\d)(?::[0-5]\d)?')


def normalize(string: str) -> str:
    return ' '.join(unidecode(string).split()).lower()


def repr_dict(data: dict, sep=", ") -> str:
    return join([f'{k}="{v}"' for k, v in dict_filtered(data).items()], sep=sep)


def remove_extra_whitespaces(value: str) -> str:
    return remove_whitespace_before_final_point(re.sub(r'\s+', ' ', value))


def remove_whitespace_before_final_point(value: str) -> str:
    return re.sub(f'\s\.', '.', value)


def remove_html_extra_whitespaces(string: str) -> str:
    return remove_extra_whitespaces(re.sub(r'\s+>', '>', string))


def age(start: datetime.date, end: datetime.date = None) -> float:
    end = end or datetime.date.today()
    return (((end - start).days - calendar.leapdays(start.year, end.year)) / 365).__round__(2)


def list_filtered(items: Sequence, func: Callable = lambda x: x not in [None, '']) -> list:
    return list(filter(func, items))


def list_of_strings(items: Sequence) -> list[str]:
    return [str(i) for i in list_filtered(items)]


def join(items: Sequence, sep: str = ' ', end: str = '') -> str:
    return sep.join(list_of_strings(items)) + end


def dict_filtered(data: dict, function: Callable = lambda x: x not in [None, '', " "]) -> dict:
    new = dict()
    for key, value in data.items():
        if function(value):
            new[key] = value
    return new


def split(value: str, pattern: str = r'\s') -> list[str]:
    return list_filtered([i.strip() for i in re.split(pattern, value)])


def split_lines(value: str, pattern: str = r'\n\r|\n') -> list[str]:
    return split(value, pattern)


def now() -> datetime.datetime:
    return datetime.datetime.now(tz=datetime.timezone(offset=datetime.timedelta(hours=-3)))


def now_isoformat() -> str:
    return now().isoformat()[:16]


def today() -> datetime.date:
    return now().date()


def today_isoformat() -> str:
    return today().isoformat()


def slug(value: str) -> str:
    return normalize(join([item for item in re.split(r'([A-Z][a-z]+)(?=[A-Z])|\s', value) if item], sep="_")).lower()


def camel_case(value: str) -> str:
    items = [*re.split(r'[-_]', slug(value))]
    return ''.join([items[0], *[i.title() for i in items[1:]]])


def cap_words_case(value: str) -> str:
    return join([i.capitalize() for i in re.split(r'[-_]', slug(value))], sep='')


def capitalize(value: str) -> str:
    return join([i.capitalize() for i in re.split(r'\s|\s+', value)])


def get_words(value: str) -> list[str]:
    return re.findall(r'\w+', value)


def split_strip(value: str, pattern: str = r'\s+|\s'):
    return [item.strip() for item in re.split(pattern, value.strip())]


def get_string_list_of_digits(value: str) -> list[str]:
    return re.findall(r'\d+[,./]\d+|\d+', value)


def string_to_number(value: str) -> Optional[Number]:
    if isinstance(value, str):
        value = re.sub(r',', '.', value)
        if '.' in value:
            return float(value)
        return int(value)
    return None


def get_list_of_numbers(value: str) -> list[Number]:
    return [string_to_number(v) for v in list_filtered(get_string_list_of_digits(value))]


def only_decimals(value: str) -> str:
    if isinstance(value, str):
        return ''.join([i for i in value if i.isdecimal()])
    return value


def get_group_or_return_value(pattern: re.Pattern, value: str):
    if isinstance(value, str):
        match = pattern.search(value)
        if match:
            return match.group()
    return value


def get_group_or_return_none(pattern: re.Pattern, value: str):
    if isinstance(value, str):
        match = pattern.search(value)
        if match:
            return match.group()
    return None


def get_first_iso_date(value: str) -> Optional[str]:
    return get_group_or_return_none(ISO_DATE_PATTERN, value)


def get_first_iso_datetime(value: str) -> Optional[str]:
    return get_group_or_return_none(ISO_DATETIME_PATTERN, value)


def get_iso_dates(value: str) -> list[Optional[str]]:
    result = ISO_DATE_PATTERN.findall(value)
    if result:
        return [join(i, sep='') for i in result]
    return []

def get_iso_datetimes(value: str) -> list[Optional[str]]:
    result = ISO_DATETIME_PATTERN.findall(value)
    if result:
        return [join(i, sep='') for i in result]
    return []
