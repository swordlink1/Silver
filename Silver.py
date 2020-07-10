# Silver 0.3.2 Public Beta

import os # cd and dir
import sys

while True:
    precommand = input("Silver BETA> ")
    checkcommand = precommand.replace(" ", "") # Check if the command entered was blank or spammed with spaces
    postcommand = precommand.split(" ")
    postcommand.pop(0)
    if precommand.startswith("echo"):
        for word in postcommand:
            print(word, end = ' ')
        print("")
    elif precommand.startswith("print"):
        for word in postcommand:
            print(word)
    elif precommand.startswith("readfile"):
        try:
            filename = ""
            for word in postcommand:
                filename = filename + str(word)
            file = open(filename, "r")
            print(file.read())
            file.close()
        except FileNotFoundError:
            print("The file does not exist. Make sure your file doesn't have spaces.")
    elif precommand.startswith("writefile"):
        try:
            filename = ""
            for word in postcommand:
                filename = filename + str(word)
            file = open(filename, "w")
            postcommand.pop(0)
            towrite = input("What contents do you want to overwrite the contents of the file with?")
            postcommand = towrite.split(" ")
            for word in postcommand:
                byteswritten = file.write(word + " ")
            print("Successfully wrote", str(byteswritten), "bytes")
        except FileNotFoundError:
            print("The file does not exist. Make sure your file doesn't have spaces.")
    elif precommand.startswith("dir"):
        files = os.listdir(".")
        for file in files:
            print(file)
    elif precommand.startswith("cd"):
        try:
            dirname = ""
            for word in postcommand:
                dirname = dirname + str(word)
            os.chdir(dirname)
        except FileNotFoundError:
            print("Please enter a directory that exists and try again.")
        except NotADirectoryError:
            print("Please enter a directory and try again.")
    elif precommand.startswith("help"):
        print("echo - Prints out whatever you type")
        print("print - Prints out whatever you type with a new line after each word")
        print("help - Prints out the commands")
        print("readfile - Reads a file")
        print("writefile - Overwrites the content of an file")
        print("makefile - Makes a file")
    elif checkcommand == "":
        continue
    else:
        print(precommand, "is not a valid command. You are using a case sensitive terminal.")