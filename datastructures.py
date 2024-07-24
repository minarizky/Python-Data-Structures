def weekday_name(day_of_week):
    """Return name of weekday.
    
        >>> weekday_name(1)
        'Sunday'
        
        >>> weekday_name(7)
        'Saturday'
        
    For days not between 1 and 7, return None
    
        >>> weekday_name(9)
        >>> weekday_name(0)
    """
    days = {
        1: 'Sunday',
        2: 'Monday',
        3: 'Tuesday',
        4: 'Wednesday',
        5: 'Thursday',
        6: 'Friday',
        7: 'Saturday'
    }
    return days.get(day_of_week)

def last_element(lst):
    """Return last item in list (None if list is empty).
    
        >>> last_element([1, 2, 3])
        3
        
        >>> last_element([]) is None
        True
    """
    if lst:
        return lst[-1]
    return None

def number_compare(a, b):
    """Report on whether a>b, b>a, or b==a
    
        >>> number_compare(1, 1)
        'Numbers are equal'
        
        >>> number_compare(-1, 1)
        'Second is greater'
        
        >>> number_compare(1, -2)
        'First is greater'
    """
    if a > b:
        return 'First is greater'
    elif b > a:
        return 'Second is greater'
    else:
        return 'Numbers are equal'

def reverse_string(phrase):
    """Reverse string,

        >>> reverse_string('awesome')
        'emosewa'

        >>> reverse_string('sauce')
        'ecuas'
    """
    return phrase[::-1]

def single_letter_count(word, letter):
    """How many times does letter appear in word (case-insensitively)?
    
        >>> single_letter_count('Hello World', 'h')
        1
        
        >>> single_letter_count('Hello World', 'z')
        0
        
        >>> single_letter_count("Hello World", 'l')
        3
    """
    return word.lower().count(letter.lower())

def multiple_letter_count(phrase):
    """Return dict of {ltr: frequency} from phrase.

        >>> multiple_letter_count('yay')
        {'y': 2, 'a': 1}

        >>> multiple_letter_count('Yay')
        {'Y': 1, 'a': 1, 'y': 1}
    """
    return {char: phrase.count(char) for char in phrase}

def list_manipulation(lst, command, location, value=None):
    """Mutate lst to add/remove from beginning or end.

    - lst: list of values
    - command: command, either "remove" or "add"
    - location: location to remove/add, either "beginning" or "end"
    - value: when adding, value to add

    remove: remove item at beginning or end, and return item removed

        >>> lst = [1, 2, 3]

        >>> list_manipulation(lst, 'remove', 'end')
        3

        >>> list_manipulation(lst, 'remove', 'beginning')
        1

        >>> lst
        [2]

    add: add item at beginning/end, and return list

        >>> lst = [1, 2, 3]

        >>> list_manipulation(lst, 'add', 'beginning', 20)
        [20, 1, 2, 3]

        >>> list_manipulation(lst, 'add', 'end', 30)
        [20, 1, 2, 3, 30]

        >>> lst
        [20, 1, 2, 3, 30]

    Invalid commands or locations should return None:

        >>> list_manipulation(lst, 'foo', 'end') is None
        True

        >>> list_manipulation(lst, 'add', 'dunno') is None
        True
    """
    if command == 'remove':
        if location == 'beginning':
            return lst.pop(0)
        elif location == 'end':
            return lst.pop()
    elif command == 'add':
        if location == 'beginning':
            lst.insert(0, value)
            return lst
        elif location == 'end':
            lst.append(value)
            return lst
    return None

def is_palindrome(phrase):
    """Is phrase a palindrome?

    Return True/False if phrase is a palindrome (same read backwards and
    forwards).

        >>> is_palindrome('tacocat')
        True

        >>> is_palindrome('noon')
        True

        >>> is_palindrome('robert')
        False

    Should ignore capitalization/spaces when deciding:

        >>> is_palindrome('taco cat')
        True

        >>> is_palindrome('Noon')
        True
    """
    normalized = ''.join(char.lower() for char in phrase if char.isalnum())
    return normalized == normalized[::-1]

def frequency(lst, search_term):
    """Return frequency of term in lst.
    
        >>> frequency([1, 4, 3, 4, 4], 4)
        3
        
        >>> frequency([1, 4, 3], 7)
        0
    """
    return lst.count(search_term)

def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'
    """
    return ''.join(
        char.swapcase() if char.lower() == to_swap.lower() else char
        for char in phrase
    )

def multiply_even_numbers(nums):
    """Multiply the even numbers.
    
        >>> multiply_even_numbers([2, 3, 4, 5, 6])
        48
        
        >>> multiply_even_numbers([3, 4, 5])
        4
        
    If there are no even numbers, return 1.
    
        >>> multiply_even_numbers([1, 3, 5])
        1
    """
    product = 1
    for num in nums:
        if num % 2 == 0:
            product *= num
    return product

def capitalize(phrase):
    """Capitalize first letter of first word of phrase.

        >>> capitalize('python')
        'Python'

        >>> capitalize('only first word')
        'Only first word'
    """
    return phrase.capitalize()

def compact(lst):
    """Return a copy of lst with non-true elements removed.

        >>> compact([0, 1, 2, '', [], False, (), None, 'All done'])
        [1, 2, 'All done']
    """
    return [item for item in lst if item]

def intersection(l1, l2):
    """Return intersection of two lists as a new list::
    
        >>> intersection([1, 2, 3], [2, 3, 4])
        [2, 3]
        
        >>> intersection([1, 2, 3], [1, 2, 3, 4])
        [1, 2, 3]
        
        >>> intersection([1, 2, 3], [3, 4])
        [3]
        
        >>> intersection([1, 2, 3], [4, 5, 6])
        []
    """
    return [item for item in l1 if item in l2]

def partition(lst, fn):
    """Partition lst by predicate.
     
     - lst: list of items
     - fn: function that returns True or False
     
     Returns new list: [a, b], where `a` are items that passed fn test,
     and `b` are items that failed fn test.

        >>> def is_even(num):
        ...     return num % 2 == 0
        
        >>> def is_string(el):
        ...     return isinstance(el, str)
        
        >>> partition([1, 2, 3, 4], is_even)
        [[2, 4], [1, 3]]
        
        >>> partition(["hi", None, 6, "bye"], is_string)
        [['hi', 'bye'], [None, 6]]
    """
    return [
        [item for item in lst if fn(item)],
        [item for item in lst if not fn(item)]
    ]

def mode(nums):
    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of times.

        >>> mode([1, 2, 1])
        1

        >>> mode([2, 2, 3, 3, 2])
        2
    """
    return max(set(nums), key=nums.count)

def calculate(operation, a, b, make_int=False, message='The result is'):
    """Perform operation on a + b, possibly truncating to an integer,
    and returning with a message.
    
    - operation: 'add', 'subtract', 'multiply', or 'divide'
    - a and b: values to operate on
    - make_int: (optional, defaults to False) if True, truncate result to integer
    - message: (optional) message to use (defaults to 'The result is')
    
    Returns "[message] [result]"
    
        >>> calculate('add', 2.5, 4)
        'The result is 6.5'
        
        >>> calculate('subtract', 4, 1.5)
        'The result is 2.5'
        
        >>> calculate('multiply', 1.5, 2)
        'The result is 3.0'
        
        >>> calculate('divide', 10, 4)
        'The result is 2.5'
        
        >>> calculate('add', 2.5, 4, make_int=True)
        'The result is 6'
        
        >>> calculate('subtract', 4, 1.5, make_int=True)
        'The result is 2'
        
        >>> calculate('multiply', 1.5, 2, make_int=True)
        'The result is 3'
        
        >>> calculate('divide', 10, 4, make_int=True)
        'The result is 2'
        
        >>> calculate('divide', 10, 4, message='I got')
        'I got 2.5'
    """
    if operation == 'add':
        result = a + b
    elif operation == 'subtract':
        result = a - b
    elif operation == 'multiply':
        result = a * b
    elif operation == 'divide':
        result = a / b
    else:
        return None

    if make_int:
        result = int(result)
    
    return f"{message} {result}"

def friend_date(a, b):
    """Given two friends, do they have any hobbies in common?
    
    - a: friend #1, a tuple of (name, age, list-of-hobbies)
    - b: friend #2, a tuple of (name, age, list-of-hobbies)
    
    Returns True if they have any hobbies in common, False is not.
    
        >>> elmo = ('Elmo', 5, ['hugging', 'being nice'])
        >>> sauron = ('Sauron', 5000, ['killing hobbits', 'chess'])
        >>> gandalf = ('Gandalf', 10000, ['waving wands', 'chess'])
        
        >>> friend_date(elmo, sauron)
        False
        
        >>> friend_date(sauron, gandalf)
        True
    """
    return bool(set(a[2]) & set(b[2]))

def triple_and_filter(nums):
    """Return new list of tripled nums for those nums divisible by 4.
    
        >>> triple_and_filter([1, 2, 3, 4])
        [12]
        
        >>> triple_and_filter([6, 8, 10, 12])
        [24, 36]
        
        >>> triple_and_filter([1, 2])
        []
    """
    return [num * 3 for num in nums if num % 4 == 0]

def extract_full_names(people):
    """Return list of names, extracting from first+last keys in people dicts.
    
        >>> names = [{'first': 'Ada', 'last': 'Lovelace'}, {'first': 'Grace', 'last': 'Hopper'}]
        >>> extract_full_names(names)
        ['Ada Lovelace', 'Grace Hopper']
    """
    return [f"{person['first']} {person['last']}" for person in people]

def sum_floats(nums):
    """Return sum of floating point numbers in nums.
    
        >>> sum_floats([1.5, 2.4, 'awesome', [], 1])
        3.9
        
        >>> sum_floats([1, 2, 3])
        0
    """
    return sum(num for num in nums if isinstance(num, float))

def list_check(lst):
    """Are all items in lst a list?
    
        >>> list_check([[1], [2, 3]])
        True
        
        >>> list_check([[1], "nope"])
        False
    """
    return all(isinstance(item, list) for item in lst)

def remove_every_other(lst):
    """Return a new list of every other item.
    
        >>> remove_every_other([1, 2, 3, 4, 5])
        [1, 3, 5]
        
        >>> remove_every_other([5, 6, 7, 8])
        [5, 7]
        
        >>> remove_every_other([1])
        [1]
    """
    return lst[::2]

def sum_pairs(nums, goal):
    """Return tuple of first pair of nums that sum to goal.
    
        >>> sum_pairs([1, 2, 2, 10], 4)
        (2, 2)
        
        >>> sum_pairs([4, 2, 10, 5, 1], 6)
        (4, 2)
        
        >>> sum_pairs([5, 1, 4, 8, 3, 2], 7)
        (4, 3)
        
        >>> sum_pairs([11, 20, 4, 2, 1, 5], 100)
    """
    seen = set()
    for num in nums:
        diff = goal - num
        if diff in seen:
            return (diff, num)
        seen.add(num)
    return ()

def vowel_count(phrase):
    """Return frequency map of vowels, case-insensitive.
    
        >>> vowel_count('rithm school')
        {'i': 1, 'o': 2}
        
        >>> vowel_count('HOW ARE YOU? i am great!') 
        {'o': 2, 'a': 2, 'e': 2, 'u': 1, 'i': 1}
    """
    phrase = phrase.lower()
    vowels = 'aeiou'
    return {vowel: phrase.count(vowel) for vowel in vowels if vowel in phrase}

def titleize(phrase):
    """Return phrase in title case (each word capitalized).
    
        >>> titleize('this is awesome')
        'This Is Awesome'
        
        >>> titleize('oNLy cAPITALIZe fIRSt')
        'Only Capitalize First'
    """
    return phrase.title()

def find_factors(num):
    """Find factors of num, in increasing order.
    
        >>> find_factors(10)
        [1, 2, 5, 10]
        
        >>> find_factors(11)
        [1, 11]
        
        >>> find_factors(111)
        [1, 3, 37, 111]
        
        >>> find_factors(321421)
        [1, 293, 1097, 321421]
    """
    return [i for i in range(1, num + 1) if num % i == 0]

def includes(collection, sought, start=None):
    """Is sought in collection, starting at index start?
    
        >>> includes([1, 2, 3], 1)
        True
        
        >>> includes([1, 2, 3], 1, 2)
        False
        
        >>> includes("hello", "o")
        True
        
        >>> includes(('Elmo', 5, 'red'), 'red', 1)
        True
        
        >>> includes({1, 2, 3}, 1)
        True
        
        >>> includes({1, 2, 3}, 1, 3)
        False
    """
    if isinstance(collection, (list, tuple, str)):
        return sought in collection[start:] if start is not None else sought in collection
    elif isinstance(collection, set):
        return sought in collection
    elif isinstance(collection, dict):
        return sought in collection.values()
    return False

def repeat(phrase, num):
    """Return phrase, repeated num times.
    
        >>> repeat('*', 3)
        '***'
        
        >>> repeat('abc', 2)
        'abcabc'
        
        >>> repeat('abc', 0)
        ''
        
    Ignore illegal values of num and return None:
    
        >>> repeat('abc', -1) is None
        True
        
        >>> repeat('abc', 'nope') is None
        True
    """
    if not isinstance(num, int) or num < 0:
        return None
    return phrase * num

def truncate(phrase, n):
    """Return truncated-at-n-chars version of phrase.
    
    If the phrase is longer than n, make sure the end of the new
    phrase has an ellipsis ("...") and is no longer than n.
    
        >>> truncate("Hello World", 6)
        'Hel...'
        
        >>> truncate("Problem solving is the best!", 10)
        'Problem...'
        
        >>> truncate("Yo", 100)
        'Yo'
        
        >>> truncate("Woah", 4)
        'W...'
        
    The smallest legal value of n is 3; if less, return a message:
    
        >>> truncate("Woah", 2)
        'Truncation must be at least 3 characters.'
    """
    if n < 3:
        return 'Truncation must be at least 3 characters.'
    if len(phrase) <= n:
        return phrase
    return phrase[:n-3] + '...'

def two_list_dictionary(keys, values):
    """Given keys and values, make dictionary of those.
    
        >>> two_list_dictionary(['x', 'y', 'z'], [9, 8, 7])
        {'x': 9, 'y': 8, 'z': 7}
        
    If there are fewer values than keys, remaining keys should have value
    of None:
    
        >>> two_list_dictionary(['a', 'b', 'c', 'd'], [1, 2, 3])
        {'a': 1, 'b': 2, 'c': 3, 'd': None}
        
    If there are fewer keys, ignore remaining values:
    
        >>> two_list_dictionary(['a', 'b'], [1, 2, 3, 4])
        {'a': 1, 'b': 2}
    """
    return {key: values[i] if i < len(values) else None for i, key in enumerate(keys)}

def sum_range(nums, start=0, end=None):
    """Return sum of numbers from start...end.
    
    - start: where to start (inclusive)
    - end: where to stop (inclusive)
    
    If end is None, go through end of list.
    
        >>> nums = [1, 2, 3, 4]
        
        >>> sum_range(nums)
        10
        
        >>> sum_range(nums, 1)
        9
        
        >>> sum_range(nums, end=2)
        6
        
        >>> sum_range(nums, 1, 3)
        9
    """
    end = end if end is not None else len(nums) - 1
    return sum(nums[start:end+1])

def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
    """
    return sorted(str(num1)) == sorted(str(num2))

def nth(lst, n):
    """Return the item at index n (return None if n is out of range).
    
        >>> lst = ['a', 'b', 'c', 'd']
        
        >>> nth(lst, 1)
        'b'
        
        >>> nth(lst, -2)
        'c'
        
        >>> nth(lst, 4) is None
        True
    """
    if -len(lst) <= n < len(lst):
        return lst[n]
    return None

def find_the_duplicate(nums):
    """Find duplicate number in nums.
    
    Given a list of nums with, at most, one duplicate, return the duplicate.
    If there is no duplicate, return None
    
        >>> find_the_duplicate([1, 2, 1, 4, 3, 12])
        1
        
        >>> find_the_duplicate([6, 1, 9, 5, 3, 4, 9])
        9
        
        >>> find_the_duplicate([2, 1, 3, 4]) is None
        True
    """
    seen = set()
    for num in nums:
        if num in seen:
            return num
        seen.add(num)
    return None

def min_max_keys(d):
    """Return tuple (min-keys, max-keys) in d.
    
        >>> min_max_keys({2: 'a', 7: 'b', 1: 'c', 10: 'd', 4: 'e'})
        (1, 10)
        
        >>> min_max_keys({"apple": "red", "cherry": "red", "berry": "blue"})
        ('apple', 'cherry')
    """
    keys = d.keys()
    return (min(keys), max(keys))

def sum_up_diagonals(matrix):
    """Given a matrix [square list of lists], return sum of diagonals.
    
    Sum of TL-to-BR diagonal along with BL-to-TR diagonal:
    
        >>> m1 = [
        ...     [1, 2],
        ...     [3, 4],
        ... ]
        
        >>> sum_up_diagonals(m1)
        10
        
        >>> m2 = [
        ...    [1, 2, 3],
        ...    [4, 5, 6],
        ...    [7, 8, 9],
        ... ]
        
        >>> sum_up_diagonals(m2)
        30
    """
    return sum(matrix[i][i] + matrix[i][len(matrix)-1-i] for i in range(len(matrix)))

def count_values(d):
    """Return number of unique values in dictionary.
    
        >>> count_values({1: 1, 2: 2, 3: 3})
        3
        
        >>> count_values({1: 1, 2: 2, 3: 2})
        2
        
        >>> count_values({1: 1, 2: 1, 3: 1})
        1
    """
    return len(set(d.values()))

def find_greater_numbers(nums):
    """Return the number of times a number is followed by a greater number.
    
    For example, for [1, 2, 3], the answer is 3:
    - the 1 is followed by the 2 and the 3
    - the 2 is followed by the 3
    
    Examples:
    
        >>> find_greater_numbers([1, 2, 3])
        3
        
        >>> find_greater_numbers([6, 1, 2, 7])
        4
        
        >>> find_greater_numbers([5, 4, 3, 2, 1])
        0
        
        >>> find_greater_numbers([])
        0
    """
    count = 0
    for i, num in enumerate(nums):
        for j in range(i + 1, len(nums)):
            if nums[j] > num:
                count += 1
    return count

def two_oldest_ages(ages):
    """Return two distinct oldest ages as tuple (second-oldest, oldest).
    
        >>> two_oldest_ages([1, 2, 10, 8])
        (8, 10)
        
        >>> two_oldest_ages([6, 1, 9, 10, 4])
        (9, 10)
        
    Even if more than one person has the same age, this should return
    two *distinct* oldest ages:
    
        >>> two_oldest_ages([1, 5, 5, 2])
        (2, 5)
    """
    unique_ages = list(set(ages))
    unique_ages.sort()
    return (unique_ages[-2], unique_ages[-1])

def is_odd_string(word):
    """Is the sum of the character-positions odd?
    
    Word is a simple word of uppercase/lowercase letters without punctuation.
    
    For each character, find its "character position" ("a"=1, "b"=2, etc).
    
    Return True/False, depending on whether sum of those numbers is odd.
    
    For example, these sum to 1, which is odd:
    
        >>> is_odd_string('a')
        True
    
    These sum to 4, which is not odd:
    
        >>> is_odd_string('aaaa')
        False
    
    Example word with an odd sum:
    
        >>> is_odd_string('amazing')
        True
    """
    return sum((ord(char) - ord('a') + 1) for char in word.lower()) % 2 == 1

def valid_parentheses(parens):
    """Are the parentheses validly balanced?
    
        >>> valid_parentheses("()")
        True
        
        >>> valid_parentheses("()()")
        True
        
        >>> valid_parentheses("(()())")
        True
        
        >>> valid_parentheses(")(")
        False
        
        >>> valid_parentheses("((())")
        False
    """
    stack = []
    for char in parens:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if not stack:
                return False
            stack.pop()
    return not stack
