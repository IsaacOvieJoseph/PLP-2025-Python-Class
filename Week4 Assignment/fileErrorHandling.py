"""File Read & Write Challenge 🖋️: 
Create a program that reads a file and writes a modified version to a new file.
Error Handling Lab 🧪: 
Ask the user for a filename and handle errors if it doesn’t exist or can’t be read.
"""

print("""         
             *** WELCOME TO ALLCAPSLOCKER !!! ***
      We are ready to help you capitalise all your letters 
      """)

# Get user's file path and desired output file name
raw_filePath = str(input("Kindly enter relative path of your file: "))
modified_filePath = str(input("what will you like to name my output file: ")) 

# Attempt to read the file and write the modified content to a new file
try:
    print("\n Reading your file...")
    fileToRead = open(raw_filePath,'r')
    fileToWrite = open(modified_filePath+".txt",'w')
    rawContent = fileToRead.read()
    modifiedContent = rawContent.upper()
    fileToWrite.write(modifiedContent)

except FileNotFoundError:
    print(f'\n--- ** {raw_filePath} DOES NOT EXIST ** ---\n Please check the file path and try again')
except FileExistsError or UnicodeDecodeError:
    print(f'-- ** Sorry, we encountered a problem while attempting to read your file ** --\n Please check the file and try again')
finally:
    print("\n Closing your file...")
    fileToRead.close()

fileToWrite.close()  # Close the output file after writing

print(f"Kindly find your output file [{modified_filePath}.txt] in the current directory")
