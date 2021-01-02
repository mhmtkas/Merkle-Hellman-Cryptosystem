def encrypt():
    for i in range(len(w)):
        temp = (w[i] * r) % q
        b.append(temp)
    word = (input("enter the word:  "))
    word_asci = [ord(c) for c in word]
    word_binary = []

    for i in word_asci:
        s = bin(i).replace("0b", "0")
        word_binary.append(s)
    # print(word_binary)

    for i in word_binary:
        temp = 0
        count = 0
        for j in str(i):
            temp += (int(j) * b[count])
            count += 1
        word_last.append(temp)

    print(word_last)


def decrypt():
    count1 = 1
    while True:
        x = (r * count1) % q
        if x == 1:
            break
        count1 += 1

    inverseInt = count1

    lastBinary_list = []

    for i in word_last:
        a = (i * inverseInt) % q
        lastBinary = 0
        for index, j in enumerate(reverseW):

            if j <= a:
                a = a - j
                binary = pow(10, index)
                lastBinary += binary
            else:
                continue
        # print(lastBinary)
        lastBinary_list.append(lastBinary)
    # print(lastBinary_list)

    ascii_list = []

    for i in lastBinary_list:
        b_num = list(str(i))
        value = 0
        for j in range(len(b_num)):
            digit = b_num.pop()
            if digit == '1':
                value = value + pow(2, j)
        ascii_list.append(value)
    print(f"\nASCII numbers of decrypted characters: {ascii_list}\n")

    solvedList = []

    for i in ascii_list:
        solvedList.append(chr(i))

    print(f"Decrypted word: {solvedList}")


if __name__ == '__main__':
    w = [2, 5, 9, 17, 40, 75, 170, 320]
    q = 740
    r = 547
    b = []
    word_last = []
    reverseW = sorted(w, reverse=True)
    sum = 0
    for i in range(len(w)):  # for counting sum of s = 652
        sum += w[i - 1]

    encrypt()

    while True:
        choice = input("\nDo you want to do decrypt process? (Y\\N):  ")
        if choice.upper() == 'Y':
            decrypt()
            break
        elif choice.upper() == 'N':
            print("End.")
            break
        else:
            print("Invalid Input")
