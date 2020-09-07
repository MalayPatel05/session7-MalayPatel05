# -*- coding: utf-8 -*-
import pytest
import string
import inspect
import re
import session7 as session_ut
import math
import sys
import os.path

def test_TC00_01_indentations():
    ''' Returns pass if used four spaces for each level of syntactically \
    significant indenting.'''
    lines = inspect.getsource(session_ut)
    spaces = re.findall('\n +.', lines)
    for space in spaces:
        assert len(space) % 4 == 2, "Your script contains misplaced indentations"
        assert len(re.sub(r'[^ ]', '', space)) % 4 == 0, "Your code indentation does not follow PEP8 guidelines"

def test_TC00_02_function_name_had_cap_letter():
    functions = inspect.getmembers(session_ut, inspect.isfunction)
    for function in functions:  
        assert len(re.findall('([A-Z])', function[0])) == 0, "You have used Capital letter(s) in your function names"

def test_TC00_02_readme_exists():
    assert os.path.isfile("README.md"), "README.md file missing!"

#TestData=[(Test Data 01),(Test Data 02)....]
TestData_TC02=[([1,13,16,22,1597],[1,13,1597])]
@pytest.mark.parametrize("test_data,expected",TestData_TC02)
def test_TC01_q1_fibonaci(test_data,expected):
    assert session_ut.checkfib(test_data) == expected

TestData_TC03=[([1,2,3,4,5,6,8],
                [1,3,5,6,8,3,4],[5,9])]
@pytest.mark.parametrize("a,b,expected",TestData_TC03)
def test_TC03_q2_1_add(a,b,expected):
    assert session_ut.sumn(a,b) == expected

TestData_TC04=[('tsai','ts'),
               ('thisa ise a soturing','ths s  strng')]
@pytest.mark.parametrize("test_data,expected",TestData_TC04)
def test_TC04_q2_2_add(test_data,expected):
    assert session_ut.removevowels(test_data) == expected

TestData_TC05=[([1,-2,3.5,4,-5,-6,8],[1,0,3.5,4,0,0,8])]
@pytest.mark.parametrize("test_data,expected",TestData_TC05)
def test_TC05_q2_3_relu(test_data,expected):
    assert session_ut.relu(test_data) == expected

TestData_TC07=[('tsai','yxfn'),
               ('uvwxyz','zabcde')]
@pytest.mark.parametrize("test_data,expected",TestData_TC07)
def test_TC07_q2_5_rotate_string(test_data,expected):
    assert session_ut.str_rotate(test_data) == expected

TestData_TC08=[('profinity_test_data1.txt',['5hit', 'ass', 'balls', 'nutsack', 'wang'])]
@pytest.mark.parametrize("test_data,expected",TestData_TC08)
def test_TC08_q3_01_input_file_size_check(test_data,expected):
    readme = open(test_data, "r")
    readme_words = readme.read().split()
    readme.close()
    assert len(readme_words) >= 200, "Add atleast 200 words"
@pytest.mark.parametrize("test_data,expected",TestData_TC08)
def test_TC08_q3_02_google_prafanity_check(test_data,expected):
    assert session_ut.checkprofanity(test_data) == expected

TestData_TC09_1=[([1,2,3,4,5,6],12)]
@pytest.mark.parametrize("test_data,expected",TestData_TC09_1)
def test_TC09_q4_1_addevennumber(test_data,expected):
    assert session_ut.sum_even(test_data) == expected

TestData_TC09_2=[('biggest character','t')]
@pytest.mark.parametrize("test_data,expected",TestData_TC09_2)
def test_TC09_q4_2_biggest_char(test_data,expected):
    assert session_ut.biggest_char(test_data) == expected

TestData_TC09_3=[([1,2,3,4,5,6,7,8,9,10],18)]
@pytest.mark.parametrize("test_data,expected",TestData_TC09_3)
def test_TC09_q4_3_add_third(test_data,expected):
    assert session_ut.add_3rd_reduced(test_data) == expected