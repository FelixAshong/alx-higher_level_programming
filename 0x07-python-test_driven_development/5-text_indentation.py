#!/usr/bin/python3
""" text_indentation"""


def text_indentation(text):
        """ text_indentation
        Arguments:
        @text: text to be changed"""
        if type(text) is not str:
                raise TypeError("text must be a string")
        text = text.strip()
        if len(text) == 0:
                return
        temp = text[0]
        delims = ['.', ':', '?']
        for char in text:
                if char == ' ' and temp in delims:
                        continue
                temp = char
                print(char, end='')
                if char in delims:
                        print()
                        print()
