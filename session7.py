# -*- coding: utf-8 -*-
import math
from random import randint
from functools import reduce,partial
def func_fib(lim:'max fibonacci value')->'return fibonacci series as list':
    '''returns fibonacci series as list
    Inputs: 
        Max value in fibonacci series
    Outputs:
        return fibonacci series as list'''
    fib=[0,1]
    i=2
    while fib[i-1]<=lim   :
        fib.append(fib[i-1]+fib[i-2])
        i=i+1
    return fib

#Question 1
# Generate fibonacci series
fiblist = func_fib(10000) 
#Check if given number is fibonacci using lambda,filter and list
checkfib=lambda checklist:list(filter(lambda n:n in fiblist,checklist))
#Question 2_1
#add 2 iterables a and b such that a is even and b is odd
sumn=lambda a,b:[x+y for x,y in list(zip(a,b)) if not x%2 and y%2]
#Question 2_2
#strips every vowel from a string provided (tsai>>t s)
vowels = ['a','e','i','o','u','A','E','I','O','U']
removevowels=lambda str:''.join([char for char in str if char not in vowels])
#Question 2_3
#ReLu function
relu = lambda lst:[max(0,RL) for RL in lst]
#Question 2_4
#sigmoid function
sigmoid = lambda lst:[math.exp(sgm)/(math.exp(sgm)+1) for sgm in lst]
#Question 2_5
#takes a small character string and shifts all characters by 5
str_rotate = lambda str:''.join(list(map(lambda char:chr((ord(char)-97+5)%26+97)if ord(char) >96 and ord(char) < 123  else char,str)))

#Question 3
def checkprofanity(inpfile_name:'Input text file')->'Google Profanity words used in text file':
    '''returns Google Profanity words used in text file
    Inputs: 
        text file
    Outputs:
        returns Google Profanity words used in text file'''
    #read Goolge Profanity word list
    inpfile_handle = open("word_list.txt","r")
    word_list=inpfile_handle.readlines()
    for i in range(len(word_list)):
        word_list[i]=word_list[i].rstrip('\n')

    inpfile_handle.close()
    #read inputfile text and store as list
    inpfile_handle = open(inpfile_name,"r")
    inpfile_text = inpfile_handle.read()

    inpfile_handle.close()
    #find profanity word using list comprehension
    profanity_word = lambda inpfile_text:[word for word in word_list if word in inpfile_text]

    return profanity_word(inpfile_text)
#Question 4_1
#add only even numbers in a list
sum_even=lambda nlist:reduce(lambda x,y:x+y if not y%2 else x,nlist,0)
#Question 4_2
#find the biggest character in a string (printable ascii characters)
biggest_char=lambda inpstr: reduce(lambda x,y:x if ord(x)>ord(y) else y,inpstr)
#Question 4_3
def add_3rd(x,y):
    if x==None:
        add_3rd.i=1
        return 0
    else:
        add_3rd.i+=1
        if not add_3rd.i%3:
            return x+y
        else:
            return x
#adds every 3rd number in a list
add_3rd_reduced=lambda inplist: reduce(add_3rd,inplist,None)
#Question 5
numplates_q5=lambda:['KA'+
                        str(randint(10,99))+
                        chr(randint(65,90))+
                        chr(randint(65,90))+
                        str(randint(1000,9999)) 
                        for i in range(15)]
#Question 6
numplates_q6=lambda state,series_strt,series_end:[state+
                                                    str(randint(10,99))+
                                                    chr(randint(65,90))+
                                                    chr(randint(65,90))+
                                                    str(randint(series_strt,series_end)) 
                                                    for i in range(15)]
numplates_partial_q6=partial(numplates_q6,series_strt=1000,series_end=9999)