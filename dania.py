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
            if (float(row[42]) >= 5):
                dataTrojan.insert(len(dataTrojan),index)
            trojan = 0
            indexy = 0
            for number in row:
                if (number != ';'):
                    content = number
                    if (indexy < 42):
                        if (int(number) >= 4):
                            trojan = trojan + 1
                    indexy = indexy + 1
            if (trojan >= 4):
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
    if (hasilData[i] < 5 and hasil[i] == 0):
        tp += 1
    elif (hasilData[i] >= 5 and hasil[i] == 0):
        fp += 1
    elif (hasilData[i] < 5 and hasil[i] == 1):
        fn += 1
    elif (hasilData[i] >= 5 and hasil[i] == 1):
        tn += 1
    if (hasilData[i] < 5):
        p += 1
    elif (hasilData[i] >= 5):
        n += 1
    i += 1
    
akurasi = (tp+tn)/len(data)
presisi = tp/(tp+fp)
recall = tp/(tp+fn)
errorrate = (fp+fn)/len(data)
fprate = fp/len(data)

print ("Pendeteksi Trojan")
print ("========================")
print ("Jumlah Data : " + str(len(data)))
print ("Jumlah Trojan Menurut Aplikasi : " + str(len(hasilTrojan)))
print ("Jumlah Trojan Menurut Dataset : " + str(len(dataTrojan)))
print ("========================")
print ("TP : " + str(tp))
print ("FP : " + str(fp))
print ("TN : " + str(tn))
print ("FN : " + str(fn))
print ("========================")
print ("Akurasi " + "{0:.2f}".format(round(akurasi*100,2)) + "%")
print ("Presisi " + "{0:.2f}".format(round(presisi*100)) + "%")
print ("Recall " + "{0:.2f}".format(round(recall*100)) + "%")
print ("Error Rate " + "{0:.2f}".format(round(errorrate*100)) + "%")
print ("False Positive Rate " + "{0:.2f}".format(round(fprate*100)) + "%")
