def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
        return True
    
def sum_of_prime(start, end):
    return sum(n for n in range(start, end + 1)if is_prime(n))

# start = int(input("Enter the start of the range:"))
# end = int(input("Enter the end of the range:"))
# print(f"sum of prime number between{start} and {end}:{sum_of_prime(start,end)}")

def length_converter(value, direction):
    """convert length between meters and feet."""
    if direction.upper() == 'M':
        print(value,"M==", round(value * 3.28084, 2),"F")
    elif direction.upper() == 'F':
        print(value,"F==",round(value/3.28084, 2),"M")       
    else:
        raise ValueError("Invalid conversion direction. use 'M' or 'F'.")
    
def count_consonants(s):
    """Count the number of consonants in a string without using inbuilt functions."""
    consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    count = 0
    for i in s:
        if i in consonants:
            count+=1
    return count

        

def min_max_finder(): 
    """Find the smallest and large numbers in a list.""" 
    n = int(input("how many number do you wnat to enter?"))

    if n <= 0:
        print("invalid input. Enter at least one number.")
        return
    numbers = []
    for i in range(n):
        num = int(input(f"Enter number{i+1}: "))
        numbers.append(num)

    min_num = numbers[0]
    
    max_num = numbers[0]

    for num in numbers:
        if num < min_num:
            min_num = num
        if num > max_num:
            max_num = num
    
    print(f"smallest: {min_num}, Largest: {max_num}")


def is_palindrome(s):
    """check if a text string is a palidrome(ignoring case and space)."""
    cleaned = []
    for char in s:
        if char.isalpha():
            cleaned.append(char.upper())
    
    reversed_cleaned = cleaned.copy()
    reversed_cleaned.reverse()

    if cleaned == reversed_cleaned:
        return True
    else:
        return False
    
    


def word_counter(filename):
    """counter occurrences of specific words in a text file."""
    target_words = {"the":0, "was":0, "and":0}
    
    try:
        with open(filename, 'r') as file:
            for line in file:
                words = line.split()

                for word in words:
                    cleaned_word = "".join(char.lower() for char in word if char.isalnum())
                    if cleaned_word in target_words:
                        target_words[cleaned_word] += 1

    except FileNotFoundError:
        return "File not found."
    return target_words

while True:
    print("Menu ")
    print("1. Prime number sum calculator")
    print("2. Length unit converter")
    print("3. Consonant counter")
    print("4. Min-Max number finder")
    print("5. Palindrome checker")
    print("6. word counter")
    print("Exit")

    choice = input("select an option (1-7): ")
    if choice == '1':
        try:
            start = int(input("Enter start of range: "))
            end = int(input("Enter end of range"))
            print("Sum of primes:", (start, end))
        except ValueError:
            print("Invalid input. PLease enter integers.")



    elif choice == '2':
        value = float(input("Enter length value:"))
        direction = input("Enter ''M'for meters to feet or 'F' for feet to meteres")
        length_converter(value, direction)
            
            
    elif choice == '3':
        text = input("Enter a text string: ")
        print("Number of consonants:", count_consonants(text))

    elif choice == '4':
        min_max_finder()


    elif choice == '5':
            text = input("Enter a text string:")
            print("Palindrome check:", is_palindrome(text))

    elif choice == '6':
            filename = input("Enter the filename: ")
            print("word count:", word_counter(filename))

    elif choice == '7':
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please select a valid option")

 
