def nSequenza(seq, studseq, n):
    seq = list(map(int, seq))
    studseq = list(map(int, studseq))

    i = 0
    j = 0
    ripensamento = 0
    while i != n and j != len(seq) and ripensamento <= 1:
        if i > 1:
            if studseq[i] < studseq[i-1]:
                ripensamento += 1
        if studseq[i] == seq[j]:
            i += 1
            j += 1
        else:
            j += 1
    if i == n:
        print("N-sottosequenza fornita ammissibile: " + str(studseq))
        print("Bravo/a hai fornito una N-sottosequenza ammissibile lunga: " + str(n))
    else:
        print("Sottosequenza fornita non ammissibile, controlla il numero di ripensamenti o i numeri inseriti")


# if __name__ == "__main__":
#     seq = ['34', '42', '44', '49', '41', '52', '63', '69', '40', '60', '86', '45', '66', '54', '79', '81', '43', '46',
#            '38', '61', '80', '48', '64', '73', '47']
#     studseq = ['34', '42', '44', '49', '52', '63', '69', '79', '81', '43', '46', '38', '48']
#     n = 13
#     nSequenza(seq, studseq, n)
