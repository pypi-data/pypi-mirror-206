#!/usr/bin/env python
# -*- coding:utf-8 -*-
from typing import Iterable, List

from .._handler._str_handler import _strings
from ..character import String
from ..classes import StaticClass


class StringUtils(metaclass=StaticClass):
    """
    string backend
    """

    @staticmethod
    def trip(value: str) -> String:
        """
        Clears the leading and trailing whitespace characters
        """
        return String(value).trip()

    @staticmethod
    def trip_start(value: str) -> String:
        """
        Clear the space at the end of the string
        """
        return String(value).trip_start()

    @staticmethod
    def trip_end(value: str) -> String:
        """
        Clear spaces at the beginning of the string
        """
        return String(value).trip_end()

    @staticmethod
    def trip_all(value: str) -> String:
        """
        Clear all whitespace characters
        """
        return String(value).trip_all()

    @staticmethod
    def equals(left: str, right: str) -> bool:
        """
        Directly judge whether it is equal or not
        :param left:
        :param right:
        :return:
        """
        return _strings.equals(left, right)

    @staticmethod
    def equals_trip(left: str, right: str) -> bool:
        """
        After removing the first and last white space characters, it is judged
        """
        return _strings.equals_trip(left, right)

    @staticmethod
    def equals_ignore_case(left: str, right: str) -> bool:
        """
        Determine whether it is equal, ignore case.
        """
        return _strings.equals_ignore_case(left, right)

    @staticmethod
    def equals_trip_ignore_case(left: str, right: str) -> bool:
        """
        Determine whether it is equal, ignore case and trip.
        """
        return _strings.equals_trip_ignore_case(left, right)

    @staticmethod
    def equals_any(src: str, target: str) -> bool:
        """
        Any element of the original string and the target string number array are equal.
        """
        return _strings.equals_any(src, target)

    @staticmethod
    def equals_all(src: str, target: str) -> bool:
        """
        All elements of the original string and target string number arrays are equal.
        """
        return _strings.equals_all(src, target)

    @staticmethod
    def equals_any_trip(src: str, target: str) -> bool:
        """
        Any element of the original string and the target string number array are equal.
        will trip.
        """
        return _strings.equals_any_trip(src, target)

    @staticmethod
    def equals_all_trip(src: str, target: str) -> bool:
        """
        All elements of the original string and target string number arrays are equal.
        will trip.
        """
        return _strings.equals_all_trip(src, target)

    @staticmethod
    def equals_any_ignore_case(src: str, target: str) -> bool:
        """
        Any element of the original string and the target string number array are equal.
        ignore case.
        """
        return _strings.equals_any_ignore_case(src, target)

    @staticmethod
    def equals_all_ignore_case(src: str, target: str) -> bool:
        """
        All elements of the original string and target string number arrays are equal.
        ignore case.
        """
        return _strings.equals_all_ignore_case(src, target)

    @staticmethod
    def equals_any_trip_ignore_case(src: str, target: str) -> bool:
        """
        Any element of the original string and the target string number array are equal.
        ignore case and trip.
        """
        return _strings.equals_any_trip_ignore_case(src, target)

    @staticmethod
    def equals_all_trip_ignore_case(src: str, target: str) -> bool:
        """
        All elements of the original string and target string number arrays are equal.
        ignore case and trip.
        """
        return _strings.equals_all_trip_ignore_case(src, target)

    @staticmethod
    def is_empty(value: str) -> bool:
        """
        Judge whether the string is empty
        """
        return _strings.is_empty(value)

    @staticmethod
    def is_not_empty(value: str) -> bool:
        """
        Judge whether the string is not empty
        """
        return _strings.is_not_empty(value)

    @staticmethod
    def is_any_empty(*strings: str, item: Iterable[str] = None) -> bool:
        """
        Validates multiple strings at the same time, and returns True as long as one string is empty
        Usage:
            StringUtils.is_any_Empty("a", "b", "") => True
        """
        iterator = list(strings)
        if item:
            iterator.extend(item)
        return _strings.is_any_empty(iterator)

    @staticmethod
    def is_all_empty(*strings: str, item: Iterable[str] = None) -> bool:
        """
        Validates multiple strings at the same time, and returns True as long as all string is empty
        Usage:
            StringUtils.is_any_Empty("a", "b", "") => True
        """
        iterator = list(strings)
        if item:
            iterator.extend(item)
        return _strings.is_all_empty(iterator)

    @staticmethod
    def is_no_empty(*strings: str, item: Iterable[str] = None) -> bool:
        """
        Validates multiple strings at the same time, and returns True as long as all string is not empty
        Usage:
            StringUtils.is_any_Empty("a", "b", "") => True
        """
        iterator = list(strings)
        if item:
            iterator.extend(item)
        return _strings.is_no_empty(iterator)

    @staticmethod
    def is_black(value: str) -> bool:
        """
        string is black, the first and last spaces will be removed before judgment
        """
        return _strings.is_black(value)

    @staticmethod
    def is_not_black(value: str) -> bool:
        """
        string isn't black,the first and last spaces will be removed before judgment
        """
        return _strings.is_not_black(value)

    @staticmethod
    def is_any_black(*strings, item: Iterable[str] = None) -> bool:
        """
        Validates multiple strings at the same time, and returns True as long as one string is black
        Usage:
            StringUtils.is_any_Black("a", "b", " ") => True
        """
        iterator = list(strings)
        if item:
            iterator.extend(item)
        return _strings.is_any_Black(iterator)

    @staticmethod
    def is_all_black(*strings, item: Iterable[str] = None) -> bool:
        """
        Validates multiple strings at the same time, and returns True as long as all string is black
        Usage:
            StringUtils.is_any_Black("a", "b", " ") => True
        """
        iterator = list(strings)
        if item:
            iterator.extend(item)
        return _strings.is_all_Black(iterator)

    @staticmethod
    def is_no_black(*strings, item: Iterable[str] = None) -> bool:
        """
        Validates multiple strings at the same time, and returns True as long as all string is not black
        Usage:
            StringUtils.is_any_Black("a", "b", " ") => True
        """
        iterator = list(strings)
        if item:
            iterator.extend(item)
        return _strings.is_no_Black(iterator)

    @staticmethod
    def splitblack(value, maxsplit: int = -1) -> List:
        """
         Cut by a blank string
        """
        return _strings.splitblack(value, maxsplit)

    @staticmethod
    def abbreviate(value: str, abbrev_marker: str = "...", offset: int = 0, max_width: int = 0) -> String:
        """
        Shorten the string
        """
        return String(_strings.abbreviate(value, abbrev_marker, offset, max_width))

    @staticmethod
    def contains(src: str, target: str) -> bool:
        """
        src contains target
        """
        return _strings.contains(src, target)

    @staticmethod
    def not_contains(src: str, target: str) -> bool:
        """
        src not contains target
        """
        return _strings.not_contains(src, target)

    @staticmethod
    def trip_contains(src: str, target: str) -> bool:
        """
        after removing the leading and trailing spaces, determine that src contains target
        """
        return _strings.trip_contains(src, target)

    @staticmethod
    def trip_not_contains(src: str, target: str) -> bool:
        """
        after removing the leading and trailing spaces, determine that src not contains target
        """
        return _strings.trip_not_contains(src, target)

    @staticmethod
    def trip_all_contains(src: str, target: str) -> bool:
        """
        Remove the "space" from anywhere in the string and make sure that src contain the destination string
        :param src: origin string
        :param target: The included string
        """
        return _strings.trip_all_contains(src, target)

    @staticmethod
    def trip_all_not_contains(src: str, target: str) -> bool:
        """
        Remove the "space" from anywhere in the string and make sure that src does not contain the destination string
        :param src: origin string
        :param target: The included string
        """
        return _strings.trip_all_not_contains(src, target)

    @staticmethod
    def to_bool(value: str, default: bool = False) -> bool:
        """
        Converts the string bool type to a true bool type.
        :param value: string bool type.
        :param default: If it is not of type string bool, the value returned by default.
        """
        return _strings.to_bool(value, default)

    @staticmethod
    def join(*iterable: str, sep: str = "") -> String:
        """
        You can receive elements for any type of iteration object for join operations.
        """
        return String(_strings.join_item(iterable, sep))

    @staticmethod
    def join_item(iterable: Iterable[str], sep: str = "") -> String:
        return String(_strings.join_item(iterable, sep))

    @staticmethod
    def convert_to_camel(value: str) -> String:
        """snake to camel"""
        return String(_strings.convert_to_camel(value))

    @staticmethod
    def convert_to_pascal(value: str) -> String:
        """snake to pascal"""
        return String(_strings.convert_to_pascal(value))

    @staticmethod
    def convert_to_snake(value: str) -> String:
        """camel to snake"""
        return String(_strings.convert_to_snake(value))


__all__ = [StringUtils]
