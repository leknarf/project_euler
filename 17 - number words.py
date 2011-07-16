words = {
    1 : 'one',
    2 : 'two',
    3 : 'three',
    4 : 'four',
    5 : 'five',
    6 : 'six',
    7 : 'seven',
    8 : 'eight',
    9 : 'nine',
    10 : 'ten',
    11 : 'eleven',
    12 : 'twelve',
    13 : 'thirteen',
    14 : 'fourteen',
    15 : 'fifteen',
    16 : 'sixteen',
    17 : 'seventeen',
    18 : 'eighteen',
    19 : 'nineteen',
    20 : 'twenty',
    30 : 'thirty',
    40 : 'forty',
    50 : 'fifty',
    60 : 'sixty',
    70 : 'seventy',
    80 : 'eighty',
    90 : 'ninety',
    100 : 'hundred', # This is incorrect, because we'll never print "one hundred"
    1000 : 'one thousand',
}

def speak(n):
    if n == 0:
        return ''
    if n in words:
        return words[n]
    if n < 100:
        teens = (n / 10) * 10
        return speak(teens) + ' ' + speak(n - teens)
    elif n > 100:
        hundreds = (n / 100) * 100
        if n - hundreds:
            return speak(hundreds / 100) + ' ' + speak(100) + ' and ' + speak(n - hundreds) 
        else:
            return speak(hundreds / 100) + ' ' + speak(100)
            
def count_letters(max_val):
    words = (speak(n) for n in range(1, max_val+1))
    words = (word.replace(' ', '') for word in words)
    return sum(len(word) for word in words)
    
print(count_letters(1000))