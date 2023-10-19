import re,os,time

def search (match):
    m_check = 0 ## to check if a match is found or not
    time.sleep(1)
    print()
    
    for i in os.listdir('Surahs/'): ## looping through all the files in the folder
        with open('Surahs/' +i , mode = 'r') as f:
            f_content = f.read().lower() ## spliting and storing each line/verse as elemnt in a list

            for line in f_content:
                ## searching for a match in each line, if match is found printing the file name and the line index+1 which will be the verse number
                if re.search(r'(verse \d:)[.]*\b'+match+r'\b[.]*',line):
                    x=i.split('.')
                    a = re.search(r'(verse \d:)[.]*\b'+match+r'\b[.]*',line)
                    print(x[0]+' '+a.group())
                    m_check += 1

    ## chechking if a match is found        
    if m_check == 0:
        time.sleep(1)
        print('No Match Found')

## loop for runing the whole programe
while True:
    print()
    state = input('1: Search word\n2: Read\n3: Quit\nChose the operation you want to perform: ')

    if state == '1':
        search(input('\nEnter the word you want to search: '))
    elif state == '3':
        print('\nClosing...Allah Hafiz!!')
        time.sleep(3)
        break
    elif state == '2':
        r_Sname = input('\nEnter the name of the surah you want to read: ')
        r_Anum = int(input('Enter the ayah no of ayah you want to read: '))
        
        with open('Surahs/'+r_Sname+'.txt' , mode = 'r') as f:
            f_content = f.read().lower().split('\n')
            print('\nIn the name of Allah the most benificient and merciful.\n'+f_content[r_Anum-1])
    else:
        print('\nInvalid input')
        continue
