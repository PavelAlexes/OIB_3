alphabet = [
    ['АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя,.?! 123456789_<>+-']
]

arrCode = [
    [
        'ЙФЯЧЫЦУВСМАКЕПИТРНГОЬБЛШЩДЮЖЗЭХЪЁйфячыцувсмакепитрнгоьблшщдюжзэхъё123456789_<>+-,.? !',
        '123456789_<>+-,.?!йфячыцувсмакепитрнгоьблшщдюжзэхъёЙФЯЧЫЦУВСМАКЕПИТРНГОЬБЛШЩДЮЖЗЭХЪ Ё',
        'УФХЦЧШЩЬЫЪЭЮЯАБВ56789_<>+-,.? !ГДЁЕЖЗИЙКЛМНОПРСТ1234уфхцчшщьыъэюяабвгдёежзийклмнопрст'
    ],
    [
        'С456789_<>+-,.? !ТУФХЦЧШЩЬЫЪЭЮЯАБВГДЕЁЖЗИЙКЛМНОПРстуфхцчшщьыъэю123яабвгдеёжзийклмнопр',
        'ЗИЙКЛМНОПРстуфхцчшщьыъэ123яабвгдеёжзийклмнопрС456789_<>+-,.? !ТУФХЦЧШЩЬЫЪЭЮЯАБВГДЕЁЖ',
        'РСТ1234уфхцчшщьыъэюяабвгдёежзийклмнопрстУФХЦЧШЩЬЫЪЭЮЯАБВ56789_<>+-,.? !ГДЁЕЖЗИЙКЛМНОП'
    ],
    [
        'БЛШЩДЮЖЗЭХЪЁйфячыцувсмакепитрнгоьблшщдюжзэхъё123456789_<>+-,.? !ЙФЯЧЫЦУВСМАКЕПИТРНГОЬ',
        ',.?!хъёЙФЯЧЫЦ123456789_<>+-УВСМАКЕПИТРНГОЬБЛШЩДЮЖЗЭХЪ Ёйфячыцувсмакепитрнгоьблшщдюжзэ',
        'У-,.? !ГДЁЕЖЗИЙКФХЦЧШЩЬЫ34уфхцчшщьыъэюяабвгдёежзийкЪЭЮЯАБВ56789_<>+ЛМНОПРСТ12лмнопрст'
    ]
]


def translate(alphabet, arrCode, text, encode, inputs):
    result = []
    z, x = 0, 0
    n, m = 0, 0
    c, c1 = 1, 1

    idx = 0
    input_value = inputs[idx]

    for char in text:
        print(f'Символ {char} заменяем на ', end='')
        try:
            if encode:
                index = alphabet[x][m].index(char)
                result_char = arrCode[z][n][index]
                print(result_char)
                result.append(result_char)
                if n + 1 < len(arrCode[z]) and c != input_value:
                    n += 1
                    c += 1
                elif c != input_value:
                    n = 0
                    c += 1
                else:
                    n = 0
                    c = 1
                    idx = (idx + 1) % len(inputs)
                    input_value = inputs[idx]
                    z = (z + 1) % len(arrCode)
            else:
                index = arrCode[z][n].index(char)
                result_char = alphabet[x][m][index]
                print(result_char)
                result.append(result_char)
                if n + 1 < len(arrCode[z]) and c1 != input_value:
                    n += 1
                    c1 += 1
                elif c1 != input_value:
                    n = 0
                    c1 += 1
                else:
                    n = 0
                    c1 = 1
                    idx = (idx + 1) % len(inputs)
                    input_value = inputs[idx]
                    z = (z + 1) % len(arrCode)
        except ValueError:
            result.append(char)
            print(char)

    print("Полученный результат: ")
    return "".join(result)


flag = False
while flag == False:
    print("Введите текст: ")
    text = input()
    print("Введите ключи контура")
    inputs = [int(input()), int(input()), int(input())]
    print("1-зашифровать 2-расшифровать")
    a = input()
    if a == "1":
        print(alphabet[0][0])
        print("----------------------")
        print(arrCode[0][0])
        print(arrCode[0][1])
        print(arrCode[0][2])
        print("----------------------")
        print(arrCode[1][0])
        print(arrCode[1][1])
        print(arrCode[1][2])
        print("----------------------")
        print(arrCode[2][0])
        print(arrCode[2][1])
        print(arrCode[2][2])
        print(translate(alphabet, arrCode, text, True, inputs))
    elif a == "2":
        print(alphabet[0][0])
        print("----------------------")
        print(arrCode[0][0])
        print(arrCode[0][1])
        print(arrCode[0][2])
        print("----------------------")
        print(arrCode[1][0])
        print(arrCode[1][1])
        print(arrCode[1][2])
        print("----------------------")
        print(arrCode[2][0])
        print(arrCode[2][1])
        print(arrCode[2][2])
        print(translate(alphabet, arrCode, text, False, inputs))
    else:
        flag = True