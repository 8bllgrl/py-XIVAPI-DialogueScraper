import os
import csv
from pathlib import Path
from typing import List
import re

# Convert over the V2 of the program and then add on the scanner fixes, as well as the character name lookup.
# Consider names like graha tia


CHAR_NAME = "Cid"  # Change the name that you wish to look up here.
DIALOGUE_COLUMN = 2
SPEAKER_COLUMN = 1

useScanner = True
total = 0
fullAbsoluteListOfFiles = []
isInFileCount = 0
basePath = os.path.abspath('')


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
                result = format_all_name_instances(fullListOfNameInstances)

    except Exception as e:
        print("Failure inside of the method for iterating through the string array of csv names.")
        print(e)

    return result


def format_all_name_instances(full_list_of_name_instances):
    # for v2
    cutscene_occurrence = []
    character_is_mentioned = []

    formatter = ""

    for name_instance in full_list_of_name_instances:
        if "VOICEMAN" in name_instance:
            cutscene_occurrence.append(name_instance)
        else:
            character_is_mentioned.append(name_instance)

    for cutscene in cutscene_occurrence:
        formatter += " " + cutscene + "\n"

    formatter += "\n"

    for character in character_is_mentioned:
        formatter += " " + character + "\n"

    return formatter


def containsCaseInsensitive(s, s2):
    s2 = s2.upper()
    s = s.upper()
    return s in s2


def collectAllNameInstances(csvContents, target):
    alreadyDetected = False
    global isInFileCount
    for j in range(len(csvContents)):
        if containsCaseInsensitive(CHAR_NAME, csvContents[j][1]):
            if not alreadyDetected:
                isInFileCount += 1
            alreadyDetected = True
            currentCsvNameInstances = []
            textFormatter = ""

            while "<If(PlayerParameter(4))>her<Else/>his</If>" in csvContents[j][DIALOGUE_COLUMN]:
                csvContents[j][DIALOGUE_COLUMN] = csvContents[j][DIALOGUE_COLUMN].replace(
                    "<If(PlayerParameter(4))>her<Else/>his</If>", "[his/her]")

            while "─" in csvContents[j][DIALOGUE_COLUMN]:
                csvContents[j][DIALOGUE_COLUMN] = csvContents[j][DIALOGUE_COLUMN].replace("─", "--")

            while "â\u20AC€" in csvContents[j][DIALOGUE_COLUMN]:
                csvContents[j][DIALOGUE_COLUMN] = csvContents[j][DIALOGUE_COLUMN].replace("â\u20ac€", "-")

            while "<Highlight>ObjectParameter(1)</Highlight>" in csvContents[j][
                DIALOGUE_COLUMN] or "<Split(<Highlight>ObjectParameter(1)</Highlight>, ,1)/>" in csvContents[j][
                DIALOGUE_COLUMN]:
                csvContents[j][DIALOGUE_COLUMN] = csvContents[j][2].replace(
                    "<Split(<Highlight>ObjectParameter(1)</Highlight>, ,1)/>", "[WARRIOR OF LIGHT]")
                csvContents[j][DIALOGUE_COLUMN] = csvContents[j][2].replace("<Highlight>ObjectParameter(1)</Highlight>",
                                                                            "[WARRIOR OF LIGHT]")

            while "<Emphasis>" in csvContents[j][DIALOGUE_COLUMN] or "</Emphasis>" in csvContents[j][DIALOGUE_COLUMN]:
                csvContents[j][DIALOGUE_COLUMN] = csvContents[j][2].replace("<Emphasis>", "*")
                csvContents[j][DIALOGUE_COLUMN] = csvContents[j][2].replace("</Emphasis>", "*")

            if "VOICEMAN" in csvContents[j][SPEAKER_COLUMN]:
                textFormatter += "C>> "
            else:
                textFormatter += "Q>> "

            textFormatter += csvContents[j][DIALOGUE_COLUMN] + "\n"
            target.append(textFormatter)
            resetStringBuilder(textFormatter)


def resetStringBuilder_OLD(string_builder: str):
    print("Reached string builder")
    string_builder[0:string_builder.length()] = ""


def resetStringBuilder(string_builder):
    string_builder = ""


def writeToFile(finalizedText):
    pathname = os.path.join(basePath, "output",
                            CHAR_NAME.upper() + "_dialogueABRIDGED.txt")
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
    elif os.path.isdir(current_path):
        # recursion for sub-directories
        recursiveWrite(list(current_path.iterdir()), 0, level + 1)

    # recursion for main directory
    recursiveWrite(arr, index + 1, level)


def extendedMakeCsvFileList():
    returnStringArray = None
    csvLocation = returnsFilepath()
    folderDirectory = Path(csvLocation)

    if folderDirectory.exists() and folderDirectory.is_dir():
        arr = list(folderDirectory.iterdir())
        # Calling recursive method
        recursiveWrite(arr, 0, 0)

        returnStringArray = [str(file) for file in fullAbsoluteListOfFiles]

    return returnStringArray


def characterLookup():
    print("Welcome to my ffx|v dialogue scraper -- VERSION 2")
    CHAR_NAME = input("What is the name of the character you wish to look up?\n")
    return CHAR_NAME


def main():
    print("Loading CSV files...")
    csvFileList = extendedMakeCsvFileList()

    print("Loading all dialogue...")

    global CHAR_NAME
    if useScanner:
        CHAR_NAME = characterLookup()

    finalizedResult = extended_readCSVFiles(csvFileList)

    writeToFile(finalizedResult)

    print("---------------------------------------------------------------------------------------------------\n" +
          f"Done! {total} Instances of the name '{CHAR_NAME}' found in {isInFileCount} of {len(csvFileList)} total "
          f"files.")

    print(
        "Powered by xivapi. https://xivapi.com/ Created by 8bllgrl on github.  All Final Fantasy XIV content is "
        "property of Square Enix Co., LTD.")


main()
