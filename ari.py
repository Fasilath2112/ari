import os

def calculate_ari(char_count, word_count, sentence_count):
    return 4.71 * (char_count / word_count) + 0.5 * (word_count / sentence_count) - 21.43

def grade_level(ari):
    if ari < 1:
        return "Kindergarten (5-6 years old)"
    elif ari < 2:
        return "First Grade (6-7 years old)"
    elif ari < 3:
        return "Second Grade (7-8 years old)"
    elif ari < 4:
        return "Third Grade (8-9 years old)"
    elif ari < 5:
        return "Fourth Grade (9-10 years old)"
    elif ari < 6:
        return "Fifth Grade (10-11 years old)"
    elif ari < 7:
        return "Sixth Grade (11-12 years old)"
    elif ari < 8:
        return "Seventh Grade (12-13 years old)"
    elif ari < 9:
        return "Eighth Grade (13-14 years old)"
    elif ari < 10:
        return "Ninth Grade (14-15 years old)"
    elif ari < 11:
        return "Tenth Grade (15-16 years old)"
    elif ari < 12:
        return "Eleventh Grade (16-17 years old)"
    elif ari < 13:
        return "Twelfth Grade (17-18 years old)"
    else:
        return "College (18-22 years old)"

# Main code starts here
filename = input("Enter the filename: ")

if not os.path.isfile(filename):
    print(f"The file {filename} does not exist.")
else:
    # Read the file content
    file = open(filename, 'r')
    text = file.read()
    file.close()

    char_count = len(text)
    word_count = len(text.split())
    sentence_count = text.count('.') + text.count('!') + text.count('?')

    print("Characters:", char_count)
    print("Words:", word_count)
    print("Sentences:", sentence_count)

    if sentence_count == 0:
        sentence_count = 1

    ari = calculate_ari(char_count, word_count, sentence_count)

    print("Automated Readability Index: {:.2f}".format(ari))

    grade = grade_level(ari)
    print("Grade Level:", grade)
