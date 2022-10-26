# Enter your code here. Read input from STDIN. Print output to STDOUT

units = ['', 'One', 'Two', 'Three', 'Four',
         'Five', 'Six', 'Seven', 'Eight', 'Nine']
dozens = ['', 'Ten', 'Twenty', 'Thirty', 'Forty',
          'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']
eleven_to_nineteen = ['', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen',
                      'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen']
hundreds = ['', 'One Hundred', 'Two Hundred', 'Three Hundred', 'Four Hundred',
            'Five Hundred', 'Six Hundred', 'Seven Hundred', 'Eight Hundred', 'Nine Hundred']
numerical_places = ['', 'Thousand', 'Million', 'Billion', 'Trillion']


def partitionNumber(N):
    numberString = list(str(N))
    numberString = numberString[::-1]
    fragmentArray = []
    fragment = []
    cont = 0
    i = 0
    while i < len(numberString):
        fragment.append(numberString[i])
        cont = cont + 1
        i = i + 1
        if len(fragment) >= 3:
            fragmentArray.append(fragment)
            fragment = []
            cont = 0
    if (len(fragment) > 0):
        fragmentArray.append(fragment)
    return fragmentArray


def decodeFragment(fragment):
    number_to_word = ''
    if (len(fragment) >= 3):
        index_hundreds = int(fragment[len(fragment) - 1])
        if (index_hundreds != 0):
            number_to_word = number_to_word + hundreds[index_hundreds] + ' '
    if (len(fragment) >= 2):
        if (len(fragment) == 3):
            index_dozens = int(fragment[len(fragment) - 2])
            index_units = int(fragment[len(fragment) - 3])
        if (len(fragment) == 2):
            index_dozens = int(fragment[len(fragment) - 1])
            index_units = int(fragment[len(fragment) - 2])
        if (not (index_dozens == 1 and index_units != 0)):
            if (index_dozens != 0):
                number_to_word = number_to_word + dozens[index_dozens] + ' '
        else:
            number_to_word = number_to_word + eleven_to_nineteen[index_units]
            return number_to_word.strip()
    if (len(fragment) >= 1):
        if (len(fragment) == 3):
            index_units = int(fragment[len(fragment) - 3])
        if (len(fragment) == 2):
            index_units = int(fragment[len(fragment) - 2])
        if (len(fragment) == 1):
            index_units = int(fragment[len(fragment) - 1])
        if (index_units != 0):
            number_to_word = number_to_word + units[index_units] + ' '
    return number_to_word.strip()


def numberToWord(N):
    fragmentArray = partitionNumber(N)
    index = len(fragmentArray) - 1
    number_to_word = ''
    while index >= 0:
        word = decodeFragment(fragmentArray[index])
        if (word != ''):
            number_to_word = number_to_word + word + \
                ' ' + numerical_places[index] + ' '
        index = index - 1
    return number_to_word.strip()


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    word = numberToWord(n)
    print(word)
