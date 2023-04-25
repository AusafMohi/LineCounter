#------------------------------------------------------------------------------- 
# Assignment:    Assignment 2B 
# 
# Program Name:  am_Assignment_2B.py  
#                
# 
# Purpose:       The purpose of this program is to read and display the 
#                top few lines and ending lines of a text file 
# 
# Author:        Ausaf Mohi 
#
# Course:        231CIS109.950 
# 
# Created:       09/03/2022 
# 
#------------------------------------------------------------------------------
#

import os.path 
from re import T



def main():
  
    print ("Welcome to heads or tails file operations \n", "\n", end="")
    print ("This program accepts a file name and the number of lines.", " \n", end="")
    print ("A positive number of lines displays from the beginning of the file" " \n", "\n", end="")
    print ("A negative number of lines displays from the end of the file.")

    filename = (input("\nEnter the file name:"))
    
    while len(filename) < 4: 
         filename = (input("Enter the file name:"))
   
    
    
    file_exist = os.path.exists(filename) # This value will either be True or False
    if (file_exist): 
        file = open(filename, "r" )
    else:
        print("File does not exist")
        exit()
        
   
    integer1 = (input("\nEnter a positive or negative integer:"))
    
    # turning the string the user inputted into an int type

    userinput1 = int(integer1) 
    
    if userinput1 >=0:
        
        print (f"\nBelow is the first {userinput1} for the file: {filename}")

        for num in range (userinput1): 
            print (file.readline(), end="") 

        print (">>>")    
    else: 
        
        print (f"\nBelow is the last {userinput1} for the file: {filename}")

        for line in (file.readlines() [userinput1:]):
            print (line, end="") 

        print ("\n>>>") 



main()





