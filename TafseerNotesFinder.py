import os       ## modules required for thr program to work
import re
import time
import pyttsx3
readout = pyttsx3.init()

def search_word(word):       ## Search function that looks for matches and return the verses with matches
    word_boundary = r'\b'
    pattern = fr'Verse (\d+):(.+?)(?=Verse \d+:|$)'       ## This verse pattern devides the files by consicutive verses
    verse_pattern = re.compile(word_boundary + word + word_boundary, re.IGNORECASE)
    matches = []

    for i in os.listdir('Surahs/'):       ## Looping through the files
        with open('Surahs/' + i, mode='r') as f:
            f_content = f.read()
            verses = re.findall(pattern, f_content, re.IGNORECASE | re.DOTALL)
            for verse_no, v_content in verses:
                if verse_pattern.search(verse_no) or verse_pattern.search(v_content):
                    matches.append((i, verse_no.strip(), v_content.strip()))

    return matches

def read_mode():
    surah_name = input("\nEnter the surah name: ")
    verse_number = input("Enter the verse number: ")
    time.sleep(1)
    try:
        with open(f'Surahs/{surah_name}.txt', mode='r') as f:
            f_content = f.read()
            verse_pattern = re.compile(r'Verse (\d+):(.+?)(?=Verse \d+:|$)', re.IGNORECASE | re.DOTALL)
            verses = verse_pattern.findall(f_content)
            
            for verse_no, v_content in verses:
                if verse_no.strip() == verse_number:
                    print(f"\nVerse {verse_no.strip()} from {surah_name}:\n\nIn the name of Allah the most beneficent and merciful,\n\n{v_content.strip()}\n")
                    verse = 'In the name of Allah the most beneficent and merciful. '+ v_content.strip()
                    readout.say(verse)
                    readout.runAndWait()
                    break
            else:
                print(f"\nVerse {verse_number} not found in {surah_name}\n")
    except:
        print ('\nNo such file found: Please try again!\n')
                

while True:
    
    print("=== Tafseer Notes Search Tool ===")
    user_input = input("Enter 1 for searching a word\nEnter 2 for read mode\nEnter 3 for quitting: ")

    match user_input:
        case '1':
            s_word = input("Enter a word to search: ")
            result = search_word(s_word)
            if result:  
                print(f"Search Results for '{s_word}':")
                for surah, verse_no, v_content in result:
                    x = surah.split('.')
                    print(f"\n{x[0]} - Verse {verse_no}\n")
            else:
                print("\nNo matches were found\n")
                
        case '2':
            read_mode()
            
        case '3':
            print('\nClosing, Allah Hafiz!!')
            readout.say('Closing, Allah Hafiz!')
            readout.runAndWait()
            time.sleep(1)
            break

        case _:
            print('\nInvalid input, Please enter 1,2 or 3\n')
