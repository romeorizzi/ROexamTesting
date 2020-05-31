def lisWithNumber(seq, studseq, n, numToCheck):
    seq = list(map(int, seq))
    studseq = list(map(int, studseq))

    check = 0
    for i in range(0, n - 1):
        if studseq[i] == numToCheck:
            check = 1
    if check == 0:
        print("Non hai inserito una sequenza contenente il numero: " + str(numToCheck))
        return
    for i in range(1, n):
        if studseq[i - 1] > studseq[i]:
            print("Non hai inserito una sequenza crescente")
            return

    i = 0
    j = 0
    while i != n and j != len(seq):
        if studseq[i] == seq[j]:
            i += 1
            j += 1
        else:
            j += 1
    if i == n:
        print("Sottosequenza fornita ammissibile: " + str(studseq))
        print("Bravo/a hai fornito una sottosequenza ammissibile lunga: " + str(n))
    else:
        print("Sottosequenza fornita non ammissibile\n")


if __name__ == "__main__":
    seq = [34, 42, 44, 49, 41, 52, 63, 69, 40, 60, 86, 45, 66, 54, 79, 81, 43, 46, 38, 61, 80, 48, 64, 73, 47]
    studseq = [34, 40, 45, 54, 61, 64, 73]
    n = 7
    lisWithNumber(seq, studseq, n, 40)
