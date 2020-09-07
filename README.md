# Session 7 - First Class Functions Part II

This assignment project is written in Python, and tested with pytest. It includes following files.
-session7.py      : This is the assignment code
-test_session7.py : This is pytest unit test. It tests completeness of assignment
-word_list.txt    : Test data for google profanity test. It contains google profanity words.
-profinity_test_data1.txt :  Test data for google profanity test. It contains paragraphs with google profanity words.

>This assignment checks understanding of following concepts:
- High level function filter,zip
- Reduce function
- lambda function
- Partial function
- List comprehension

> Description of Functions/Class
-**func_fib:**This function generates fibonacci series. It takes maximum value as input arguement and generates fibonacci sereies upto max value.
-**checkfib:**Solution of Q1: This function returns fibonacci numbers from given list of numbers. It uses filter and lambda.
-**sumn    :**Solution of Q2.1: This function add 2 iterables a and b such that a is even and b is odd. It uses list comprehension and zip.
-**removevowels:**Solution of Q2.2: strips every vowel from a string provided. It uses list comprehension.
-**relu    :**Solution of Q2.3: This function implements ReLu function using list comprehension.
-**sigmoid:** Solution of Q2.4: This function implements sigmoid function using list comprehension.
-**str_rotate:**Solution of Q2.5: takes a small character string and shifts all characters by 5 using list comprehension. At boundry it restarts from a.
-**checkprofanity:**Solution of Q3: This function takes a 200 word paragraph and checks if it contains google profanity words. First it reads good prfanity words list from word_list.txt file. Then it reads text from input file and stores it as list. Then it uses list comprehension expression **profanity_word** to check profanity word.
