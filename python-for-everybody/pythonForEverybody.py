## Assignment 2.2
# Write a program that uses raw_input to prompt a user for their name and then
#welcomes them. Note that raw_input will pop up a dialog box

# The code below almost works

name = input("Enter your name")
print("Hello %s" % name)

## Assignment 2.3
# Write a program to prompt the user for hours and rate per hour using raw_input
#to compute gross pay. Use 35 hours and a rate of 2.75 per hour to test the
#program (the pay should be 96.25).

# This first line is provided for you

hrs = float(input("Enter Hours:"))
rate = float(input("Enter Rate:"))
print(hrs * rate)

## Assignment 3.1

# 3.1 Write a program to prompt the user for hours and rate per hour using
#raw_input to compute gross pay.
# Pay the hourly rate for the hours up to 40 and 1.5 times the hourly rate
#for all hours worked above 40 hours.
# Use 45 hours and a rate of 10.50 per hour to test the program
#(the pay should be 498.75)

hrs = float(input("Enter Hours:"))
rate = float(input("Enter Rate:"))

if hrs <= 40:
    pay = hrs * rate
    print(pay)
else:
    pay = 40 * rate + (rate * 1.5 * (hrs - 40))
    print(pay)

## Assignemt 3.3
# Write a program to prompt for a score between 0.0 and 1.0. If the score
#is out of range, print an error. If the score is between 0.0 and 1.0, print a
# grade using the following table:
# Score Grade
# >= 0.9 A
# >= 0.8 B
# >= 0.7 C
# >= 0.6 D
# < 0.6 F
# If the user enters a value out of range, print a suitable error message and
#exit. For the test, enter a score of 0.85.

inp = input("Enter Score: ")

try:
    score = float(inp)
except:
    print("Error! Enter numerical value")
    quit()

if score < 0 and score > 10:
    print ; "Error! The value entered is out of range"
    quit()
elif score >= 0.9:
    print('A')
elif score >= 0.8:
    print('B')
elif score >= 0.7:
    print('C')
elif score >= 0.6:
    print('D')
else:
    print('F')

## Assignment 4.6

# Write a program to prompt the user for hours and rate per hour using
#raw_input to compute gross pay.
# Award time-and-a-half for the hourly rate for all hours worked above 40 hours.
# Put the logic to do the computation of time-and-a-half in a function called
#computepay() and use the function to do the computation.
# The function should return a value. Use 45 hours and a rate of 10.50 per hour
# to test the program (the pay should be 498.75)

def computepay(h,r):
    if h <= 40:
        return h * r
    else:
        return 40 * r + (r * 1.5 * (h - 40))

h = float(input("Enter Hours:"))
r = float(input("Enter Rate:"))
p = computepay(h,r)
print(p)


## Assignment 5.2

# Write a program that repeatedly prompts a user for integer numbers until
#the user enters 'done'.
# Once 'done' is entered, print out the largest and smallest of the numbers.
# If the user enters anything other than a valid number catch it with a
#try/except and put out an appropriate
# message and ignore the number

largest = None
smallest = None
while True:
    num = input("Enter a number: ")

    # Handle extreme cases
    if num == "done" : break
    #print num
    try:
        intg = int(num)
    except:
        print("Invalid input")
        continue

    # Do the work
    if largest is None or intg > largest:
        largest = intg
    if smallest is None or intg < smallest:
        smallest = intg

print("Maximum is", largest)
print("Minimum is", smallest)

# Exercise 7.1. Write a program to read through a file and print the
# contents of thefile (line by line) all in upper case.
def readwords():
    fname = input("Enter file name: ")
    try:
        fhand = open(fname)
    except:
        print('File cannot be opened:', fname)
        exit()

    for line in fhand:
        words = line.rstrip()
        print(words.upper())

readwords()
#
# Exercise 7.2. Write a program to prompt for a file name, and
# #then read through the file and look for lines of the form
#
# X-DSPAM-Confidence: 0.8475
#
# When you encounter a line that starts with “X-DSPAM-Confidence:” pull apart
# the line to extract the floating-point number on the line. Count these lines and
# then compute the total of the spam confidence values from these lines. When you
# reach the end of the file, print out the average spam confidence
#Modify the program that prompts the user for the file
# name so that it prints a funny message when the user types in the exact file name
# “na na boo boo”.
# '''

def findnumbers():
    fname = input("Enter file name: ")

    if fname == "na na boo boo":
        print("NA NA BOO BOO TO YOU - You have been punk'd!")
        exit()

    try:
        fhand = open(fname, 'r')
    except:
        print('File cannot be opened:', fname)
        exit()

    total = 0
    floats = []
    for line in fhand:
        if line.strip().startswith('X-DSPAM-Confidence:'):
            flt = float(line.split(':')[1].strip())
            floats.append(flt)
            total += flt

    average = total/len(floats)

    print('Average spam confidence:', average)

findnumbers()

# Exercise 8.1 Write a function called chop that takes a list and modifies it, remov-
# ing the first and last elements, and returns None.
# Then write a function called middle that takes a list and returns a new list that
# contains all but the first and last elements.
lst = ['a','b','c']
def chop(lst):
    del lst[0]
    del lst[-1]
    print(lst)
chop(lst)

lst = ['a','b','c']
def middle(lst):
    rest = lst[1:]
    mddl = rest[:-1]
    print(mddl)
middle(lst)

# Exercise 8.2 Figure out which line of the above program is still not properly
# guarded. See if you can construct a text file which causes the program to
# fail and then modify the program so that the line is properly guarded and
# test it to make sure it handles your new text file.

# Exercise 8.3 Rewrite the guardian code in the above example without two
# if statements. Instead, use a compound logical expression using the and
# logical operator with a single if statement.

# We can cause an IndexError by passing this program a line which
# starts with "From" but containing nothing else. This passes the first test, the
# length of the line is > 0. The second test checks if the line starts with
# "From" and the program proceeds to try to print words[2] which does not exist.
# We can guard against this case by adding an "or" test to check that the line
# contains a 3rd item.
#
def debug():
  fhand = open('mbox-short.txt')
  count = 0
  for line in fhand:
      words = line.split()
      # print 'Debug:', words
      if len(words) == 0 or len(words) < 3 and words[0] != 'From': continue
      print(words[2])
debug()


# Exercise 8.4 Download a copy of the file from www.py4inf.com/code/romeo.
# txt
# Write a program to open the file romeo.txt and read it line by line. For each line,
# split the line into a list of words using the split function.
# For each word, check to see if the word is already in a list. If the word is not in the
# list, add it to the list.
# When the program completes, sort and print the resulting words in alphabetical
# order.
# Enter file: romeo.txt
# ['Arise', 'But', 'It', 'Juliet', 'Who', 'already',
# 'and', 'breaks', 'east', 'envious', 'fair', 'grief',
# 'is', 'kill', 'light', 'moon', 'pale', 'sick', 'soft',
# 'sun', 'the', 'through', 'what', 'window',
# 'with', 'yonder']

def romeo():
    fname = input("Enter file name: ")

    try:
        fhand = open(fname, 'r')
    except:
        print('File cannot be opened:', fname)
        exit()

    words = []
    for line in fhand:
        makewords = line.split()

        for word in makewords:
            if word in words: continue

            else:
                words.append(word)

    words.sort()
    print(words)

romeo()

# Exercise 8.5 Write a program to read through the mail box data and when you
# find line that starts with “From”, you will split the line into words using the split
# function. We are interested in who sent the message, which is the second word on
# the From line.

# From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008


# You will parse the From line and print out the second word for each From line,
# then you will also count the number of From (not From:) lines and print out a
# count at the end.

def mail():
    fname = input("Enter file name: ")

    try:
        fhand = open(fname, 'r')
    except:
        print('File cannot be opened:', fname)
        exit()

    count = 0
    for line in fhand:
        delimiter = ' '
        makewords = line.split(delimiter)

        if len(makewords) == 0 or len(makewords) < 3 :continue

        if makewords[0] != 'From' : continue

        print(makewords[1])

        count += 1

    print('There were', count, 'lines in the file with From as the first word')

mail()

# Exercise 8.6 Rewrite the program that prompts the user for a list of numbers and
# prints out the maximum and minimum of the numbers at the end when the user
# enters “done”. Write the program to store the numbers the user enters in a list
# and use the max() and min() functions to compute the maximum and minimum
# numbers after the loop completes.

def numbers():

    numberlst = []
    while True:
        userinput = input("Enter a number: ")

        if userinput == "done":
            break
        try:
            number = float(userinput)
        except:
            print("Invalid, please try again")

        numberlst.append(userinput)

    print('Maximum:',max(numberlst))
    print('Manimum:',min(numberlst))

numbers()

# Exercise 9.1 Write a program that reads the words in words.txt and stores them
# as keys in a dictionary. It doesn’t matter what the values are. Then you can use
# the in operator as a fast way to check whether a string is in the dictionary.

def dictcounter():

    fname = input("Enter file name: ")
    dictionary = dict()

    try:
        fhand = open(fname, 'r')
    except:
        print('File cannot be opened:', fname)
        exit()

    for line in fhand:
        words = line.split()
        for word in words:
            dictionary[word] = word

        return word_dict

dictcounter()

# Exercise 9.2 Write a program that categorizes each mail message by which day
# of the week the commit was done. To do this look for lines that start with “From”,
# then look for the third word and keep a running count of each of the days of the
# week. At the end of the program print out the contents of your dictionary (order
# does not matter).

def mailcat():

    fname = input("Enter file name: ")

    try:
        fhand = open(fname, 'r')
    except:
        print('File cannot be opened:', fname)
        exit()

    dictionary = dict()

    for line in fhand:
        words = line.split()
        if len(words) == 0 or len(words) < 3 :continue
        if words[0] != 'From' : continue
        date = words[2]
        if date not in dictionary:
            dictionary[date] = 1
        else:
            dictionary[date] += 1

    print(dictionary)

mailcat()

#mbox-short.txt


# Exercise 9.3 Write a program to read through a mail log, build a histogram using
# a dictionary to count how many messages have come from each email address,
# and print the dictionary.
# Enter file name: mbox-short.txt
# {'gopal.ramasammycook@gmail.com': 1, 'louis@media.berkeley.edu': 3,
# 'cwen@iupui.edu': 5, 'antranig@caret.cam.ac.uk': 1,
# 'rjlowe@iupui.edu': 2, 'gsilver@umich.edu': 3,
# 'david.horwitz@uct.ac.za': 4, 'wagnermr@iupui.edu': 1,
# 'zqian@umich.edu': 4, 'stephen.marquard@uct.ac.za': 2,
# 'ray@media.berkeley.edu': 1}


def mailsource():

    fname = input("Enter file name: ")

    try:
        fhand = open(fname, 'r')
    except:
        print('File cannot be opened:', fname)
        exit()

    dictionary = dict()

    for line in fhand:
        words = line.split()
        if len(words) == 0 or len(words) < 3 :continue
        if words[0] != 'From' : continue
        date = words[1]
        if date not in dictionary:
            dictionary[date] = 1
        else:
            dictionary[date] += 1

    print(dictionary)

mailsource()

# Exercise 9.4 Add code to the above program to figure out who has the most mes-
# sages in the file.
# After all the data has been read and the dictionary has been created, look through
# the dictionary using a maximum loop (see Section 5.7.2) to find who has the most
# messages and print how many messages the person has.
# Enter a file name: mbox-short.txt
# cwen@iupui.edu 5
# Enter a file name: mbox.txt
# zqian@umich.edu 19

def mailsource():

    fname = input("Enter file name: ")

    try:
        fhand = open(fname, 'r')
    except:
        print('File cannot be opened:', fname)
        exit()

    dictionary = dict()

    for line in fhand:
        words = line.split()
        if len(words) == 0 or len(words) < 3 :continue
        if words[0] != 'From' : continue
        date = words[1]
        if date not in dictionary:
            dictionary[date] = 1
        else:
            dictionary[date] += 1

    maximum = None
    for mail in dictionary:
        if maximum is None or dictionary[mail] > maximum:
            maximum = dictionary[mail]
            sender = mail
    print(sender, maximum)

mailsource()

# Exercise 9.5 This program records the domain name (instead of the address)
# where the message was sent from instead of who the mail came from (i.e., the
# whole email address). At the end of the program, print out the contents of your
# dictionary.
# python schoolcount.py
# Enter a file name: mbox-short.txt s
# {'media.berkeley.edu': 4, 'uct.ac.za': 6, 'umich.edu': 7,
# 'gmail.com': 1, 'caret.cam.ac.uk': 1, 'iupui.edu': 8}

def domain():

    fname = input("Enter file name: ")

    try:
        fhand = open(fname, 'r')
    except:
        print('File cannot be opened:', fname)
        exit()

    dictionary = dict()

    for line in fhand:
        words = line.split()
        if len(words) == 0 or len(words) < 3 :continue
        if words[0] != 'From' : continue

        mail = words[1]
        address = mail.split("@")
        mailaddress = address[0]

        if mailaddress not in dictionary:
            dictionary[mailaddress] = 1
        else:
            dictionary[mailaddress] += 1

    print(dictionary)

domain()

# Exercise 10.1 Revise a previous program as follows: Read and parse the “From”
# lines and pull out the addresses from the line. Count the number of messages from
# each person using a dictionary.
# After all the data has been read, print the person with the most commits by creating
# a list of (count, email) tuples from the dictionary. Then sort the list in reverse order
# and print out the person who has the most commits.
# Sample Line:
# From stephen.marquard@uct.ac.za Sat Jan
# 5 09:14:16 2008
# Enter a file name: mbox-short.txt
# cwen@iupui.edu 5
# Enter a file name: mbox.txt
# zqian@umich.edu 195


def mailsource():

    fname = input("Enter file name: ")

    try:
        fhand = open(fname, 'r')
    except:
        print('File cannot be opened:', fname)
        exit()

    dictionary = dict()

    for line in fhand:
        words = line.split()
        if len(words) == 0 or len(words) < 3 :continue
        if words[0] != 'From' : continue
        date = words[1]
        if date not in dictionary:
            dictionary[date] = 1
        else:
            dictionary[date] += 1

    maximum = None
    for mail in dictionary:
        if maximum is None or dictionary[mail] > maximum:
            maximum = dictionary[mail]
            sender = mail
    print(sender, maximum)

mailsource()

# Exercise 10.2 This program counts the distribution of the hour of the day for
# each of the messages. You can pull the hour from the “From” line by finding the
# time string and then splitting that string into parts using the colon character. Once
# you have accumulated the counts for each hour, print out the counts, one per line,
# sorted by hour as shown below


# Sample Execution:
# python timeofday.py
# Enter a file name: mbox-short.txt
# 04 3
# 06 1
# 07 1
# 09 2
# 10 3
# 11 6
# 14 1
# 15 2
# 16 4
# 17 2
# 18 1
# 19 1

# From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008

def hour():

    fname = input("Enter file name: ")

    try:
        fhand = open(fname, 'r')
    except:
        print('File cannot be opened:', fname)
        exit()

    dictionary = dict()

    for line in fhand:
        words = line.split()
        if len(words) == 0 or len(words) < 3 :continue
        if words[0] != 'From' : continue

        time = words[5]
        hour = time.split(":")
        timehour = hour[0]

        if timehour not in dictionary:
            dictionary[timehour] = 1
        else:
            dictionary[timehour] += 1

    lst = list()
    for key, val in dictionary.items():
        lst.append( (key, val) )
    lst.sort()
    for key, val in lst:
        print(key, val)

hour()
#
# Exercise 10.3 Write a program that reads a file and prints the letters in decreasing
# order of frequency. Your program should convert all the input to lower case and
# only count the letters a-z. Your program should not count spaces, digits, punctua-
# tion, or anything other than the letters a-z. Find text samples from several different
# languages and see how letter frequency varies between languages. Compare your
# results with the tables at wikipedia.org/wiki/Letter_frequencies.

def hour():

    import string

    fname = input("Enter file name: ")

    try:
        fhand = open(fname, 'r')
    except:
        print('File cannot be opened:', fname)
        exit()


    dictionary = dict()

    for line in fhand:

        line = line.translate(None, string.punctuation)
        line = line.lower()
        words = line.split()

        for word in words:

            word = ''.join(i for i in word if not i.isdigit())

            for i in word:

                if ir not in dictionary:
                    dictionary[i] = 1
                else:
                    dictionary[i] += 1

    lst = list()
    for key, val in dictionary.items():
        lst.append( (key, val) )
    lst.sort()
    for key, val in lst:
        print(key, val)

hour()

#Exercise 11.1 Write a simple program to simulate the operation of the grep
# command on Unix. Ask the user to enter a regular expression and count
# the number of lines that matched the regular expression.

def grep():
	import re
	fname = input("Enter file name: ")
	rename = input("Enter regular expresion: ")

	try:
		fhand = open(fname)
	except:
		print('File cannot be opened:', fname)
		exit()

	count = 0

	for line in fhand:
		line = line.rstrip()
		x = re.findall(rename, line)

		if len(x) > 0:
			count = count + 1

	print(fname  + " had " + str(count) + " lines that matched " + rename)

grep()

# Exercise 11.2 Write a program to look for lines of the form
# New Revision: 39772
# and extract the number from each of the lines using a regular expression
# and thefindall() method. Compute the average of the numbers and print out
# the average.

def grep():
	import re
	fname = input("Enter file name: ")

	try:
		fhand = open(fname)
	except:
		print('File cannot be opened:', fname)
		exit()

	count = 0

	for line in fhand:
		line = line.rstrip()
		x = re.findall('New Revision: 39772', line)

		if len(x) > 0:
			count = count + 1

	print(fname  + " had " + str(count) + " lines that matched " + rename)

grep()

# Assignment 1
def sqlite3db():

	import sqlite3

	conn = sqlite3.connect('emaildb.sqlite')
	cur = conn.cursor()

	cur.execute('DROP TABLE IF EXISTS Counts')

	cur.execute('CREATE TABLE Counts (org TEXT, count INTEGER)')

	fname = input('Enter file name: ')
	if (len(fname) < 1): fname = 'mbox-short.txt'
	fh = open(fname)
	for line in fh:
	    if not line.startswith('From: '): continue
	    pieces = line.split()
	    email = pieces[1]
	    cur.execute('SELECT count FROM Counts WHERE email = ? ', (email,))
	    row = cur.fetchone()
	    if row is None:
	        cur.execute('''INSERT INTO Counts (email, count)
	                VALUES (?, 1)''', (email,))
	    else:
	        cur.execute('UPDATE Counts SET count = count + 1 WHERE email = ?',
	                    (email,))
	conn.commit()

	# https://www.sqlite.org/lang_select.html
	sqlstr = 'SELECT email, count FROM Counts ORDER BY count DESC LIMIT 10'

	for row in cur.execute(sqlstr):
	    print(str(row[0]), row[1])

	cur.close()

sqlite3db()


# Assignment 2
# Code: create db, create table (org, count) and count number emails per organization
# Note: week 2 assessment from the Coursera MOOC Using Databases with Python

def sqlite3db():

	import sqlite3

	#Connecting to the file in which we want to store our db
	conn = sqlite3.connect('emaildb.sqlite')
	cur = conn.cursor()

	#Deleting any possible table that may affect this assignment
	cur.execute('DROP TABLE IF EXISTS Counts')

	#Creating the table we're going to use
	cur.execute('''
	CREATE TABLE Counts (org TEXT, count INTEGER)''')

	#Indicating the file from where we'll read the data
	fname = input('Enter file name: ')
	if (len(fname) < 1): fname = 'mbox.txt'
	fh = open(fname)
	for line in fh:
		if not line.startswith('From: '): continue
		pieces = line.split()
		email = pieces[1]
		parts = email.split('@')
		org = parts[-1]

    	#Updating the table with the correspondent information
		cur.execute('SELECT count FROM Counts WHERE org = ? ', (org,))
		row = cur.fetchone()
		if row is None:
			cur.execute('''INSERT INTO Counts (org, count) VALUES (?, 1)''', (org,))
		else:
			cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?', (org,))

	# We commit the changes after they've finished because this speeds up the
	# execution and, since our operations are not critical, a loss wouldn't suppose
	# any problem
	conn.commit()

	# Getting the top 10 results and showing them
	# https://www.sqlite.org/lang_select.html
	sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'

	for row in cur.execute(sqlstr):
	    print(str(row[0]), row[1])

    cur.close()

sqlite3db()

# Assignment 3
# Code: read an iTunes export file in XML and create a properly normalized db
# with these tables (track, album, artist, genre)
# Note: week 3 assessment from the Coursera MOOC Using Databases with Python

def itunesdb():

    import xml.etree.ElementTree as ET
    import sqlite3

    conn = sqlite3.connect('trackdb.sqlite')
    cur = conn.cursor()

    # Make some fresh tables using executescript()
    cur.executescript('''
    DROP TABLE IF EXISTS Artist;
    DROP TABLE IF EXISTS Genre;
    DROP TABLE IF EXISTS Album;
    DROP TABLE IF EXISTS Track;

    CREATE TABLE Artist (
        id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        name    TEXT UNIQUE
    );

    CREATE TABLE Genre (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
    );

    CREATE TABLE Album (
        id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        artist_id  INTEGER,
        title   TEXT UNIQUE
    );

    CREATE TABLE Track (
        id  INTEGER NOT NULL PRIMARY KEY
            AUTOINCREMENT UNIQUE,
        title TEXT  UNIQUE,
        album_id  INTEGER,
        genre_id INTEGER
    );
    ''')


    fname = input('Enter file name: ')
    if ( len(fname) < 1 ) : fname = 'Library.xml'

    # <key>Track ID</key><integer>369</integer>
    # <key>Name</key><string>Another One Bites The Dust</string>
    # <key>Artist</key><string>Queen</string>
    # <key>Genre</key><string>X</string>
    def lookup(d, key):
        found = False
        for child in d:
            if found : return child.text
            if child.tag == 'key' and child.text == key :
                found = True
        return None

    stuff = ET.parse(fname)
    all = stuff.findall('dict/dict/dict')
    print('Dict count:', len(all))
    for entry in all:
        if ( lookup(entry, 'Track ID') is None ) : continue

        name = lookup(entry, 'Name')
        artist = lookup(entry, 'Artist')
        album = lookup(entry, 'Album')
        genre = lookup(entry, 'Genre')

        if name is None or artist is None or album is None or genre is None:
            continue

        print(name, artist, album, genre)

        cur.execute('''INSERT OR IGNORE INTO Artist (name)
            VALUES ( ? )''', ( artist, ) )
        cur.execute('SELECT id FROM Artist WHERE name = ? ', (artist, ))
        artist_id = cur.fetchone()[0]

        cur.execute('''INSERT OR IGNORE INTO Album (title, artist_id)
            VALUES ( ?, ? )''', ( album, artist_id ) )
        cur.execute('SELECT id FROM Album WHERE title = ? ', (album, ))
        album_id = cur.fetchone()[0]

        cur.execute('''INSERT OR IGNORE INTO Genre (name)
            VALUES ( ? )''', ( genre, ) )
        cur.execute('SELECT id FROM Genre WHERE name = ? ', (genre, ))
        genre_id = cur.fetchone()[0]

        cur.execute('''INSERT OR REPLACE INTO Track
            (title, album_id, genre_id)
            VALUES ( ?, ?, ?)''',
            ( name, album_id, genre_id) )

        conn.commit()

itunesdb()

# Assignment 4
# Code: read a roster data in JSON format, parse it, and produce a db
# containing User, Course, and Member tables, with role column stores in Member table
# Note: week 4 assessment from the Coursera MOOC Using Databases with Python

# User, Course, and Member tables

def rosterdb():
    import json
    import sqlite3

    conn = sqlite3.connect('rosterdb.sqlite')
    cur = conn.cursor()

    # Do some setup
    cur.executescript('''
    DROP TABLE IF EXISTS User;
    DROP TABLE IF EXISTS Member;
    DROP TABLE IF EXISTS Course;

    CREATE TABLE User (
        id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        name   TEXT UNIQUE
    );

    CREATE TABLE Course (
        id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        title  TEXT UNIQUE
    );

    CREATE TABLE Member (
        user_id     INTEGER,
        course_id   INTEGER,
        role        INTEGER,
        PRIMARY KEY (user_id, course_id)
    )
    ''')

    fname = input('Enter file name: ')
    if len(fname) < 1:
        fname = 'roster_data_sample.json'

    # [
    #   [ "Charley", "si110", 1 ],
    #   [ "Mea", "si110", 0 ],

    str_data = open(fname).read()
    json_data = json.loads(str_data)

    for entry in json_data:

        name = entry[0];
        title = entry[1];
        role = entry[2];

        print((name, title, role))

        cur.execute('''INSERT OR IGNORE INTO User (name)
            VALUES ( ? )''', ( name, ) )
        cur.execute('SELECT id FROM User WHERE name = ? ', (name, ))
        user_id = cur.fetchone()[0]

        cur.execute('''INSERT OR IGNORE INTO Course (title)
            VALUES ( ? )''', ( title, ) )
        cur.execute('SELECT id FROM Course WHERE title = ? ', (title, ))
        course_id = cur.fetchone()[0]

        cur.execute('''INSERT OR REPLACE INTO Member
            (user_id, course_id, role) VALUES ( ?, ?, ? )''',
            ( user_id, course_id, role ) )
        conn.commit()

rosterdb()
