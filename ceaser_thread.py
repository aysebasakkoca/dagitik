import threading

sonuc = []
def main():
    i=0
    metin2 =[]
    s = input('Şifreleme için kaydırma sayısı girin')
    n = input('Thread sayısını girin')
    l = input('Threadin çalışacağı karakter sayısını girin')
    metin1 = open('metin.txt','r')  
    length = find_length(metin1)    
    while i<length:
        for j in range(n):
            for k in range(l):
                ch = metin1.read(1)
                metin2.append(ch)       
            thread_func(metin2,s)
            metin2 = []
            i+=1
    metin1.close()
    return 0   
def thread_func(metin2,s):
    t1 =  threading.start_new_thread(ceaser,(metin2,s))
    t1.start()
    t1.join()
    return 0
    
def find_length(metin1):   
    j=0
    while True:
        ch=metin1.read(1)
        if not ch: break
        j+=1
    return j

def ceaser(metin2,s):
    array1 = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    array2 = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    result = []
    
    for x in metin2:
        if x in array1:
            result.append(array1[(array1.index(x)+s)%26])
        elif x in array2:
            result.append(array2[(array2.index(x)+s)%26])
    result = "".join(result)
    send(result)
    return 0
    
def send(result):
    sonuc.append(result)
    uzunluk = find_length(sonuc)
    metin = open('metin.txt','r') 
    length = metin.read()
    if(uzunluk == length):
        ends(sonuc)
    return 0
def ends(sonuc):
    file = open('sonuc.txt','w')
    file.write(sonuc)
    file.close()
    return 0