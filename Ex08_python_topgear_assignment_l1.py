#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  4 14:32:19 2018

@author: arv
"""

str1="""Python is a widely used high-level programming langauage for \
general-purpose prograaming, created by Guido van Rossum and first released \
in 1991. An interpreted language, Python has a design philosophy which \
emphasizes code readability (notably using whitespace indentation to delimit \
code blocks rather than curly braces or keywords), and a syntax which \
allows programmers to concpets in fewer lines of code than possible \
languages such as C++ or Java. The language provides constructs inteneded \
to enable writing clear programs on both a small scale and a large scale. \
Python featues a dynamic type system and sutomatic memory management and \
supports multiple programming paradgms,including object-oriented, imperative, \
functional programming, and procedural styles. It has a large and \
comprehensive standard library. Python interpreters are available for \
many operating systems, allowing Python code to run on a wide variety of \
systems. CPython , the reference implementation of Python, is opne source \
software and has a community-based development model, as do nearly all of \
its variant implementations. CPython os managed by the non-profit Python \
Software Foundation."""

# Function to create a dict with the list of following words
def set_key(dictionary, key, value):
    if key not in dictionary:
        dictionary[key] = [value]
    elif value not in dictionary[key]:
            dictionary[key].append(value)

# Function to process the input srting
# Takes word as input and returns the list of following words
def prediceFollowingWord(word):
    dictionary_word = {}
    wordList=str1.split()
    for wordAsKey in wordList:
        idx = 0
        for wordAsValue in wordList:
            idx+=1
            if wordAsKey == wordAsValue and idx<len(wordList):
                    set_key(dictionary_word, wordAsKey, wordList[idx])
            
    return dictionary_word[word]
    
print(prediceFollowingWord('Python'))

