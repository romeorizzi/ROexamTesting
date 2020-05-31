def ldsWithNumber(seq, studseq, n, numToCheck):
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
        if studseq[i - 1] < studseq[i]:
            print("Non hai inserito una sequenza decrescente")
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

