## ---------- Challenge: Love Calculator ---------- ##
# 💪 This is a difficult challenge! 💪 
# You are going to write a function called calculate_love_score() that tests the compatibility between two names.  To work out the love score between two people: 
# 1. Take both people's names and check for the number of times the letters in the word TRUE occurs.   
# 2. Then check for the number of times the letters in the word LOVE occurs.   
# 3. Then combine these numbers to make a 2 digit number and print it out. 
# e.g.
# name1 = "Angela Yu" name2 = "Jack Bauer"
# T occurs 0 times 
# R occurs 1 time 
# U occurs 2 times 
# E occurs 2 times 
# Total = 5 
# L occurs 1 time 
# O occurs 0 times 
# V occurs 0 times 
# E occurs 2 times 
# Total = 3 
# Love Score = 53
# Example Input 
# calculate_love_score("Kanye West", "Kim Kardashian")
# Example Output
# 42

def calculate_love_score(name1, name2):
    # Combine both names and convert to lowercase
    names = (name1 + name2).lower()

    # Count letters in "TRUE"
    true_score = (
        names.count("t") +
        names.count("r") +
        names.count("u") +
        names.count("e")
    )

    # Count letters in "LOVE"
    love_score = (
        names.count("l") +
        names.count("o") +
        names.count("v") +
        names.count("e")
    )

    # Combine the scores
    final_score = int(str(true_score) + str(love_score))

    print(final_score)


# Example
calculate_love_score("Angela Yu", "Jack Bauer")