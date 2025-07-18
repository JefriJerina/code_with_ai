#!/usr/bin/env python3
"""
VowelCounter.py - Simple vowel counting with data ingestion
"""

def count_vowels(word):
    """Count vowels in a word"""
    vowels = 'aeiouAEIOU'
    count = 0
    for char in word:
        if char in vowels:
            count += 1
    return count

def process_text_file(filename):
    """Read words from a text file and count vowels"""
    try:
        with open(filename, 'r') as file:
            content = file.read()
            words = content.split()
            
            print(f"Processing {len(words)} words from {filename}:")
            print("-" * 40)
            
            for word in words:
                vowel_count = count_vowels(word)
                print(f"'{word}' has {vowel_count} vowels")
                
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found")
    except Exception as e:
        print(f"Error reading file: {e}")

def process_user_input():
    """Get word from user input and count vowels"""
    word = input("Enter a word: ")
    vowel_count = count_vowels(word)
    print(f"'{word}' has {vowel_count} vowels")

def main():
    """Main function"""
    print("=== Vowel Counter ===")
    print("1. Count vowels in a word")
    print("2. Process words from a file")
    
    choice = input("Choose option (1 or 2): ")
    
    if choice == '1':
        process_user_input()
    elif choice == '2':
        filename = input("Enter filename: ")
        process_text_file(filename)
    else:
        print("Invalid choice")

if __name__ == "__main__":
    main()