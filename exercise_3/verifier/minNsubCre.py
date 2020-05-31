def minimoNumSubCRE(seq, studseq, n):
    seq = list(map(int, seq))
    studseqint = []
    for elem in studseq:
        aux = []
        for num in elem:
            if num != '0':
                aux.append(int(num))
        studseqint.append(aux)

    check = [0 for i in range(len(seq))]
    for elem in studseqint:
        if len(elem) == 1:
            trovato = 0
            j = 0
            while j < len(seq) and trovato != 1:
                if elem[0] == seq[j]:
                    check[j] = 1
                    trovato = 1
                j += 1
        else:
            for i in range(1, len(elem)):
                j = 0
                if elem[i - 1] > elem[i]:
                    print("Hai inserito una sequenza non crescente")
                    return
                else:
                    trovato = 0
                    while j < len(seq) and trovato != 2:
                        if elem[i - 1] == seq[j]:
                            check[j] = 1
                            trovato += 1
                        if elem[i] == seq[j]:
                            check[j] = 1
                            trovato += 1
                        j += 1

    for x in check:
        if x == 0:
            print("Soluzione sbagliata non hai inserito tutti i numeri\n")
            return

    print("Bravo/a hai trovato queste " + str(n) + " sottosequenze: " + str(studseqint))

