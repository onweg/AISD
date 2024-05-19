import csv

def to_numbers(nameFile):
    num = []
    with open(nameFile, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            num += [StringToInt(row[0].lower())]

    a = nameFile.split('.')
    
    
    with open(a[0]+"_res.csv", 'w') as file:
        writer = csv.writer(file)
        for n in num:
            writer.writerow(
            [n]
        )

def operationOnNumbers(str):
    split = str.split()
    if len(split) != 3:
        print("Неверный формат")

    num1 = int(split[0])
    num2 = int(split[2])
    operator = split[1]

    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num2 == 0:
            return "Деление на ноль невозможно"
        return num1 / num2
    elif operator == '%':
        if num2 == 0:
            return "Брать остаток от деления от нуля невозможно"
        return num1 % num2
    elif operator == '^':
        return num1 ** num2
    else:
        return "Неверный формат"
        
def IntToStr(num):

    units = ["ноль", "один", "два", "три", "четыре", "пять", "шесть", "семь", "восемь", "девять",
             "десять", "одиннадцать", "двенадцать", "тринадцать", "четырнадцать", "пятнадцать",
             "шестнадцать", "семнадцать", "восемнадцать", "девятнадцать"]

    tens = ["", "", "двадцать", "тридцать", "сорок", "пятьдесят", "шестьдесят", "семьдесят", "восемьдесят", "девяносто"]

    hunders = ["", "сто", "двести", "триста", "четыреста", "пятьсот", "шестьсот", "семьсот", "восемьсот", "девятьсот"]

    message = hunders[num//100] + ' '
    message += units[num%100] if 0 <= num%100 <= 19 else tens[(num%100)//10] + ' ' + units[num%10]
    return message
    
def StringToInt(str):
    split = str.split()

    units = {"ноль":0,"один":1,"два":2,"три":3, "четыре":4, "пять":5, "шесть":6, "семь":7, "восемь":8, "девять":9,
             "десять":10, "одиннадцать":11, "двенадцать":12, "тринадцать":13, "четырнадцать":14, "пятнадцать":15,
             "шестнадцать":16, "семнадцать":17, "восемнадцать":18, "девятнадцать":19}

    tens = {"двадцать":20, "тридцать":30, "сорок":40, "пятьдесят":50, "шестьдесят":60, "семьдесят":70, "восемьдесят":80, "девяносто":90}

    hundreds = {"сто":100,"двести":200,"триста":300,"четыреста":400,"пятьсот":500,"шестьсот":600,"семьсот":700,"восемьсот":800,"девятьсясот":900}

    answer = 0

    for word in split:
        if word in units:
            answer += units[word]
        elif word in tens:
            answer += tens[word]
        elif word in hundreds:
            answer += hundreds[word]
        else:
            return "Неверное число"

    return (answer)


def operationsOnStrings(str):
    split = str.split()
    num1 = 0
    num2 = 0
    str_num = ""
    operation = ["плюс", "минус", "умножить"]

    for word in split:
        if word in operation:
            num1 = StringToInt(str_num)
            oper = word
            str_num = ""
        else:
            str_num += word + ' '
    num2 = StringToInt(str_num)

    if oper == "плюс":
        return IntToStr(num1 + num2)
    if oper == "минус":
        return IntToStr(num1-num2)
    if oper == "умножить":
        return IntToStr(num1*num2)

