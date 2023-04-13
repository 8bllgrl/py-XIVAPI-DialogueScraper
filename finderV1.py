import os
import csv
from pathlib import Path
from typing import List
import re

# Dialogue Finder V1


CHAR_NAME = "Cid"  # Change the name that you wish to look up here.
useScanner = False
total = 0
isInFileCount = 0
fullAbsoluteListOfFiles = []
basePath = os.path.abspath('')


def returnsFilepath_OLD():
    # TODO: Change this to the proper file locations.
    path = os.path.abspath(os.path.join(basePath, "src", "main", "resources", "csvdirectory"))
    print("location of csv files: ", path)
    print("---------------------------------------------------------------------------------------------------")
    return path


def returnsFilepath():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    csv_dir = os.path.join(current_dir, "resources", "csvdirectory")
    path = os.path.abspath(csv_dir)
    print("location of csv files: ", path)
    print("---------------------------------------------------------------------------------------------------")
    return path


def extended_readCSVFiles(csvFileList: List[str]) -> str:
    result = ""
    fullListOfNameInstances = []
    global total

    try:
        for path in csvFileList:
            with open(path, newline='', encoding='utf-8') as csvfile:
                reader = csv.reader(csvfile, delimiter=',')
                currentCSVContents = [row for row in reader]

                collectAllNameInstances(currentCSVContents, fullListOfNameInstances)
                total = len(fullListOfNameInstances)
                result = formatAllNameInstances(fullListOfNameInstances)

    except Exception as e:
        print("Failure inside of the method for iterating through the string array of csv names.")
        print(e)

    return result


def formatAllNameInstances(fullListOfNameInstances: List[str]) -> str:
    chararacterIsSpeaking = []
    characterIsMentioned = []
    formatter = []

    for name in fullListOfNameInstances:
        if containsSpeakerText(CHAR_NAME, name):
            chararacterIsSpeaking.append(name)
        elif containsCharacterName(CHAR_NAME, name):
            characterIsMentioned.append(name)

    formatter.append("Character is speaking:\n")
    for name in chararacterIsSpeaking:
        formatter.append(name + "\n\n")
    formatter.append("\n")
    formatter.append("Character is mentioned:\n")
    for name in characterIsMentioned:
        formatter.append(name + "\n\n")

    return ''.join(formatter)


def addUnderscoresAroundCharactername(character: str) -> str:
    return "_" + character + "_"


def addUnderscoreBeforeCharactername(character: str) -> str:
    return "_" + character


def containsSpeakerText(character: str, stringinput: str) -> bool:
    character = character.upper()
    return addUnderscoresAroundCharactername(character) in stringinput or addUnderscoreBeforeCharactername(
        character) in stringinput


def containsCharacterName(character: str, stringinput: str) -> bool:
    # Escapes the special characters in the input string
    escapedName = re.escape(character)

    # Make sure it matches the name surrounded by optional punctuation and whitespace
    pattern = r'(?i)(?:\b|\W|^)' + escapedName + r'(?:\b|\W|$)'

    # Compile the pattern into a regular expression object
    regex = re.compile(pattern)

    # Match that against the sentence
    match = regex.search(stringinput)
    if match:
        # If the name is found in the sentence, check if any words contain the name
        words = re.findall(r'\w+', stringinput)
        for word in words:
            if word.lower() == character.lower():
                return True

        return True
    else:
        # If the name is not found in the sentence, return false
        return False


def containsCaseInsensitive(s, s2):
    s2 = s2.upper()
    s = s.upper()
    return s in s2


def collectAllNameInstances(csvContents, target):
    alreadyDetected = False
    global isInFileCount
    for row in csvContents:
        for column in row:
            if containsCaseInsensitive(CHAR_NAME, column):
                if not alreadyDetected:
                    isInFileCount += 1
                alreadyDetected = True
                textFormatter = row[1] + " -- " + row[2]  # access row elements by index
                target.append(textFormatter)


def characterLookup():
    print("Welcome to my ffx|v dialogue scraper")
    CHAR_NAME = input("What is the name of the character you wish to look up?")
    return CHAR_NAME


def reset_string_builder(string_builder):
    string_builder.delete(0, string_builder.length())


def contains_case_insensitive(s, s2):
    s = s.upper()
    s2 = s2.upper()
    return s in s2


def writeToFile(finalizedText):
    # TODO: Change this to the proper file locations.
    pathname = os.path.join(basePath, "output",
                            CHAR_NAME.upper() + "_dialogue.txt")
    try:
        with open(pathname, 'w', encoding='utf-8') as file:
            file.write(finalizedText)
        print("Wrote to file:")
    except IOError:
        print("Could not write to file!")
    soutpath = os.path.abspath(pathname)
    print("location of '" + CHAR_NAME.upper() + "_dialogue.txt'" + " file :  ")
    print(soutpath)


def recursiveWrite(arr, index, level):
    global fullAbsoluteListOfFiles
    # terminate condition
    if index == len(arr):
        return

    # convert string to file object
    current_path = arr[index]
    current_file = None
    if os.path.isfile(current_path):
        fullAbsoluteListOfFiles.append(current_path.absolute())
        print(f"File {current_path} processed at level {level}")
    elif os.path.isdir(current_path):
        # recursion for sub-directories
        print(f"Directory {current_path} processed at level {level}")
        recursiveWrite(list(current_path.iterdir()), 0, level + 1)

    # recursion for main directory
    recursiveWrite(arr, index + 1, level)


def extendedMakeCsvFileList():
    returnStringArray = None
    csvLocation = returnsFilepath()
    folderDirectory = Path(csvLocation)

    if folderDirectory.exists() and folderDirectory.is_dir():
        arr = list(folderDirectory.iterdir())
        print("List of files and subdirectories in the directory:", arr)
        # Calling recursive method
        recursiveWrite(arr, 0, 0)
        print("List of absolute file paths:")
        print(fullAbsoluteListOfFiles)

        returnStringArray = [str(file) for file in fullAbsoluteListOfFiles]
        print("List of file paths as strings:")
        print(returnStringArray)

    return returnStringArray


def setCharName(charName):
    global CHAR_NAME
    CHAR_NAME = charName


def main():
    print("Loading CSV files...")
    csvFileList = extendedMakeCsvFileList()

    for s in csvFileList:
        print(s)

    print(":" + str(csvFileList))

    print("Loading all dialogue...")

    if useScanner:
        characterLookup()

    finalizedResult = extended_readCSVFiles(csvFileList)

    writeToFile(finalizedResult)

    print("---------------------------------------------------------------------------------------------------\n" +
          f"Done! {total} Instances of the name '{CHAR_NAME}' found in {isInFileCount} of {len(csvFileList)} total "
          f"files.")

    print(
        "Powered by xivapi. https://xivapi.com/ Created by 8bllgrl on github.  All Final Fantasy XIV content is "
        "property of Square Enix Co., LTD.")


main()
