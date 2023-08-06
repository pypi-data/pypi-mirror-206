# !/usr/bin/env python
# -*- coding:utf-8 -*-
from typing import Optional, Callable

from .collection.array import Array
from .collection.arraylist import ArrayList
from ._handler._str_handler import _strings
from .generic import T


class String(str):

    def __new__(cls, value):
        return str.__new__(cls, str(value))

    def __init__(self, value):
        if hasattr(value, "__len__"):
            self._length = len(value)
        else:
            self._length = 0

    def trip(self) -> 'String':
        """
        Clears the leading and trailing whitespace characters
        """
        return String(_strings.trip(self))

    def trip_start(self) -> 'String':
        """
        Clear the space at the end of the string
        """
        return String(_strings.trip_start(self))

    def trip_end(self) -> 'String':
        """
        Clear spaces at the beginning of the string
        """
        return String(_strings.trip_end(self))

    def trip_all(self) -> 'String':
        """
        Clear all whitespace characters
        """
        return String(_strings.trip_all(self))

    def equals(self, value: str) -> bool:
        """
        Directly judge whether it is equal or not
        """
        return _strings.equals(self, value)

    def equals_trip(self, value: str) -> bool:
        """
        After removing the first and last white space characters, it is judged
        """
        return _strings.equals_trip(self, value)

    def equals_ignore_case(self, value: str) -> bool:
        """
        Determine whether it is equal, ignore case.
        """
        return _strings.equals_ignore_case(self, value)

    def equals_trip_ignore_case(self, value: str) -> bool:
        """
        Determine whether it is equal, ignore case and trip.
        """
        return _strings.equals_trip_ignore_case(self, value)

    @property
    def is_empty(self) -> bool:
        """
        Judge whether the string is empty
        The first and last spaces will be removed before judgment
        """
        return _strings.is_empty(self)

    @property
    def is_not_empty(self) -> bool:
        """
        Judge whether the string is not empty
        The first and last spaces will be removed before judgment
        """
        return _strings.is_not_empty(self)

    @property
    def is_black(self) -> bool:
        """
        string is black,don't remove start and end spec
        """
        return _strings.is_black(self)

    @property
    def is_not_black(self) -> bool:
        """
        string isn't black,don't remove start and end spec
        """
        return _strings.is_not_black(self)

    def contains(self, target: str) -> bool:
        """
        src contains target
        """
        return _strings.contains(self, target)

    def not_contains(self, target: str) -> bool:
        """
        src not contains target
        """
        return _strings.not_contains(self, target)

    def trip_contains(self, target: str) -> bool:
        """
        after removing the leading and trailing spaces, determine that src contains target
        """
        return _strings.trip_contains(self, target)

    def trip_not_contains(self, target: str) -> bool:
        """
        after removing the leading and trailing spaces, determine that src not contains target
        """
        return _strings.trip_not_contains(self, target)

    def trip_all_contains(self, target: str) -> bool:
        """
        Remove the "space" from anywhere in the string and make sure that src contain the destination string
        :param target: The included string
        """
        return _strings.trip_all_contains(self, target)

    def trip_all_not_contains(self, target: str) -> bool:
        """
        Remove the "space" from anywhere in the string and make sure that src does not contain the destination string
        :param target: The included string
        """
        return _strings.trip_all_not_contains(self, target)

    def to_bool(self, default: bool = False) -> bool:
        """
        Converts the string bool type to a true bool type.
        :param default: If it is not of type string bool, the value returned by default.
        """
        return _strings.to_bool(self, default)

    def splitblack(self, maxsplit: int = -1) -> ArrayList:
        """
         Cut by a blank string
        """
        return ArrayList.of_item(_strings.splitblack(self, maxsplit))

    def abbreviate(self, abbrev_marker: str = "...", offset: int = 0, max_width: int = 0) -> 'String':
        """
        Shorten the string
        """
        return String(_strings.abbreviate(self, abbrev_marker, offset, max_width))

    def convert_to_camel(self) -> 'String':
        """snake to camel"""
        return String(_strings.convert_to_camel(self))

    def convert_to_pascal(self) -> 'String':
        """snake to pascal"""
        return String(_strings.convert_to_pascal(self))

    def convert_to_snake(self) -> 'String':
        """camel to snake"""
        return String(_strings.convert_to_snake(self))

    def last_index(self, substring: str, from_index: int = 0, to_index: int = 0) -> int:
        """
        Gets the position (start position) of the last occurrence of the specified character in the string.
        If from_index or to_index is specified, the returned position is relative.
        :param substring: Specifies the string retrieved.
        :param from_index: The location where the retrieval begins
        :param to_index: The location where the retrieval ended
        """
        return _strings.last_index(self, substring, from_index, to_index)


class StringBuilder(Array[T]):

    def __init__(self, sep: Optional[str] = "", start: Optional[str] = "", end: Optional[str] = ""):
        """
        :param sep: A connector for multiple elements when converted to a string
        :param start: After conversion to a string, the beginning of the string
        :param end: The end of the string after conversion to a string
        """
        self.__append = super().append
        self.__sep = str(sep)
        self.__start = str(start)
        self.__end = str(end)
        super(StringBuilder, self).__init__(list())

    def __str__(self) -> String:
        return self.string()

    def __repr__(self):
        return self.string()

    def string(self, call_has_index: Callable[[int, T], str] = None, call_no_index: Callable[[T], str] = None) \
            -> String:
        """
        Convert StringBuilder to string
        Provides two different callback functions for element handling,
        if you do not provide a processing callback function, it will be directly concatenated
        :param call_has_index: Pass in the element subscript and the element itself
                like:
                    s = StringBuilder()
                    s.append("a").append("b").append("c")
                    print(s.string(call_has_index=lambda i, v: f"{i}{v}"))  => 0a1b2c
        :param call_no_index: Only the element is passed in
                like:
                    s = StringBuilder()
                    s.append("a").append("b").append("c")
                    print(s..string(call_no_index=lambda v: f"value={v}")) => value=avalue=bvalue=c
        :no params:
                like:
                    s = StringBuilder()
                    s.append("a").append("b").append("c")
                    print(s..string() => 123
        """
        content = self.__start
        if issubclass(type(call_has_index), Callable):
            content += _strings.join_item((call_has_index(i, v) for i, v in enumerate(self)), self.__sep)
        elif issubclass(type(call_no_index), Callable):
            content += _strings.join_item((call_no_index(v) for v in self), self.__sep)
        else:
            content += _strings.join_item(self, self.__sep)
        content += self.__end
        return String(content)

    def append(self, __object: T) -> 'StringBuilder':
        """
        Add a character element
        """
        self.__append(__object)
        return self

    def is_any_empty(self) -> bool:
        """
        Validates multiple strings at the same time, and returns True as long as one string is empty
        Usage:
            StringUtils.is_any_Empty("a", "b", "") => True
        """
        return _strings.is_any_empty(self)

    def is_all_empty(self) -> bool:
        """
        Validates multiple strings at the same time, and returns True as long as all string is empty
        Usage:
            StringUtils.is_any_Empty("a", "b", "") => True
        """
        return _strings.is_all_empty(self)

    def is_no_empty(self) -> bool:
        """
        Validates multiple strings at the same time, and returns True as long as all string is not empty
        Usage:
            StringUtils.is_any_Empty("a", "b", "") => True
        """
        return _strings.is_no_empty(self)

    def is_any_black(self) -> bool:
        """
        Validates multiple strings at the same time, and returns True as long as one string is black
        Usage:
            StringUtils.is_any_Black("a", "b", " ") => True
        """
        return _strings.is_any_Black(self)

    def is_all_black(self) -> bool:
        """
        Validates multiple strings at the same time, and returns True as long as all string is black
        Usage:
            StringUtils.is_any_Black("a", "b", " ") => True
        """
        return _strings.is_all_Black(self)

    def is_no_black(self) -> bool:
        """
        Validates multiple strings at the same time, and returns True as long as all string is not black
        Usage:
            StringUtils.is_any_Black("a", "b", " ") => True
        """
        return _strings.is_no_Black(self)
