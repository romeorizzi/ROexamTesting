def minimoNumSubDESC(seq, studseq, n):
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
                if elem[i - 1] < elem[i]:
                    print("Hai inserito una sequenza non decrescente")
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

# if __name__ == "__main__":
#     seq=['34','42','44','49','41','52','63','69','40','60','86','45','66','54','79','81','43','46','38','61','80','48','64','73','47']
#     studseq=[['34','0','0','0'],['42','41','40','38'],['44','43','0','0'],['49','45','0','0'], ['52','46','0','0'], ['63','60','54','48'], ['69','66','61','47'], ['86','79','64','0'], ['81','80','73','0']]
#     n=9
#     minimoNumSubDESC(seq,studseq,n)
