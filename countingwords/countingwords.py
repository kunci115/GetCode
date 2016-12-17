# -*- coding: utf-8 -*-
"""
Created on Thu Dec 15 10:42:06 2016
author : Rino Alfian
"""
vowels = 'aeiou'
hilangkantb = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
bacateks = open("TeksUji.txt", "r+")
str = bacateks.read()
words = str.split()
words.sort()
no_punct = ""
#menghilangkan tanda baca
for char in words:
   if char not in hilangkantb:
       no_punct = no_punct + char
#mengurutkan kata
for word in words:  
	print(word)
   
#menghitung huruf vocal
count = {}.fromkeys(vowels,0)

for char in str:
   if char in count:
       count[char] += 1
print(count)
