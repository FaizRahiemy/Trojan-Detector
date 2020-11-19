import csv
import numpy as np

data = []
hasilData = []
dataTrojan = []
hasil = []
hasilTrojan = []
with open('parameter.csv', "rt", encoding="utf8") as csvfile:
    resultreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    index = 0;
    for row in resultreader:
        if (index >= 1):
            data.insert(len(data),row)
            hasilData.insert(len(hasilData),float(row[42]))
            if (float(row[42]) != 8 and float(row[42]) != 2):
                dataTrojan.insert(len(dataTrojan),index)
            trojan = 0
            indexy = 0
            for number in row:
                if (number != ';'):
                    content = number
                    if (indexy < 42):
                        if (indexy != 0 and indexy != 1 and indexy != 2 and indexy != 6 and indexy != 7 and indexy != 11 and indexy != 13 and indexy != 15 and indexy != 16 and indexy != 17 and  indexy != 18 and indexy != 19 and indexy != 22 and indexy != 23 and indexy != 27 and indexy != 28 and indexy != 29 and indexy != 30 and indexy != 32 and indexy != 36 and indexy != 38 and indexy != 39 and indexy != 40 and indexy != 41):
                            if (int(number) >= 1):
                                trojan = trojan + 1
                    indexy = indexy + 1
            if (trojan >= 1):
                hasil.insert(len(hasil),float(1))
                hasilTrojan.insert(len(hasilTrojan),index)
            else:
                hasil.insert(len(hasil),float(0))
        index = index + 1
       
tp=0
tn=0
fp=0
fn=0
p=0
n=0
i=0

while i < len(data):
    if (hasilData[i] == 8 or hasilData[i] == 2):
        if (hasil[i] == 1):
            fp += 1
        else:
            tn += 1
    else:
        if (hasil[i] == 1):
            tp += 1
        else:
            fn += 1
    i += 1

presisi = tp/(tp+fp)    
akurasi = (tp+tn)/len(data)
recall = tp/(tp+fn)


print ("Static/Dynamic")
print ("========================")
print ("Jumlah Data : " + str(len(data)))
print ("Jumlah Trojan Menurut Aplikasi : " + str(len(hasilTrojan)))
print ("Jumlah Bukan Trojan Menurut Aplikasi : " + str(len(data) - len(hasilTrojan)))
print ("Jumlah Trojan Menurut Dataset : " + str(len(dataTrojan)))
print ("Jumlah Bukan Trojan Menurut Dataset : " + str(len(data) - len(dataTrojan)))
print ("========================")
print ("TP : " + str(tp))
print ("FP : " + str(fp))
print ("TN : " + str(tn))
print ("FN : " + str(fn))
print ("========================")
print ("Akurasi " + "{0:.2f}".format(round(akurasi*100,2)) + "%")
print ("Presisi " + "{0:.2f}".format(round(presisi*100)) + "%")
print ("Recall " + "{0:.2f}".format(round(recall*100)) + "%")
