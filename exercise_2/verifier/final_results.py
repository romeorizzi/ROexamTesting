import fnmatch
import os

def save_results(path):
    #path = '../data/tmp/'
    n_file=len(fnmatch.filter(os.listdir(path), 'es*.txt'))
    res = open(path + 'soluzione.txt', 'w')
    for i in range(1,n_file+1):
        file = open(path+'es'+str(i)+'.txt', 'r')
        line=file.readlines()
        if len(line)==1:
            n=line[0].split(',')
            res.write(str(i)+".\tSequenza: "+str(line[0])+"\t Lunghezza: "+str(len(n))+'\n')
        else:
            res.write(str(i)+".\tSequenze:\n")
            for elem in line:
                elem=elem[1:-2]
                elem=elem.replace(" ", "")
                aux=[]
                num=elem.split(",")
                for n in num:
                    if int(n)!=0:
                        aux.append(int(n))
                res.write('\t\t'+str(aux)+'\n')
            res.write('\tNumero di sottosequenze: '+str(len(line)))

        file.close()


    res.close()




# if __name__ == '__main__':
#     save_results()