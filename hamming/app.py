from flask import Flask, render_template, request

app = Flask(__name__)

def calcRedundantBits(m):
    # 2 ^ r >= m + r + 1 formulu kullanilarak knotrol bitlerinin sayisi hesaplanir.
	# 0 .. m arasında donecek bir dongu olusturulur ve esitsizligi saglayan deger dondurulur. 
    for i in range(m):
        if(2**i >= m + i + 1):
            return i

#kontrol bitlerinin konumlari bulunur
def posRedundantBits(data, r):
    #Check bitlerinin konum numaralari bulunur
    j = 0
    k = 1
    m = len(data)
    res = ''

    #konum 2'nin bir ussuyse  '0' eklenir, diger turlu sonuc eklenir
    for i in range(1, m + r + 1):
        if(i == 2**j):
            res = res + '0'
            j += 1
        else:
            res = res + data[-1 * k]
            k += 1

    #konumlar tersinden sayildigi icin sonuc tersine cevrilir (m + r+1 ... 1)
    return res[::-1]

#xor islemi sonucu olusan sendrom kelimesi hesaplanır
def checkBits(arr, r):
    n = len(arr)
    hamming = ""

    #r. parity bitini bulmak icin 0'dan r - 1'e bir dongu kurulur.
    for i in range(r):
        val = 0
        for j in range(1, n + 1):
            #msb 1 ise bitwise veya parity biti bulmak için dizideki değer kullanilir
            if(j & (2**i) == (2**i)):
                val = val ^ int(arr[-1 * j])
                #array tersten olduğu için degerleri -1 ile carpilir
        hamming += str(val)
    
    #gercek sendrom kelimesine ulasmak icin sonuc ters cevrilir
    hamming = hamming[::-1]
    return hamming

def errorCheckBits(r, arr_input):
    data_hamming = ""
    reversed_arr_input = arr_input[::-1]
    for i in range(r):
        data_hamming += reversed_arr_input[2**i - 1]
    return data_hamming[::-1]

#parity bitleri hesaplanir
def calcParityBits(arr, r):
    n = len(arr)
    for i in range(r):
        val = 0
        for j in range(1, n + 1):
            if(j & (2**i) == (2**i)):
                val = val ^ int(arr[-1 * j])

        # String birlestirme
		# (0 , n - 2^r) + parity bit + (n - 2^r + 1 , n)
        arr = arr[:n - (2**i)] + str(val) + arr[n - (2**i) + 1:]
    return arr

def detectError(arr, nr):
    n = len(arr)
    res = 0

    #parity bitlerin hesaplanmasi
    for i in range(nr):
        val = 0
        for j in range(1, n + 1):
            if(j & (2**i) == (2**i)):
                val = val ^ int(arr[-1 * j])

        #parity bitleri eklenerek bir binary numarasi elde edilir
        res = res + val * (10**i)
    
    #binary decimal'e çevrilir
    return int(str(res), 2)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        data = request.form['data']
        m = len(data)
        r = calcRedundantBits(m)
        arr = posRedundantBits(data, r)
        hamming = checkBits(arr, r)
        arr = calcParityBits(arr, r)
        if 'error_data' in request.form:
            arr_input = request.form['error_data']
            data_hamming = errorCheckBits(r, arr_input)
            correction = detectError(arr_input, r)
            if correction == 0:
                result = "There is no error in the received message."
            elif hamming != data_hamming:
                result = "The error is in check bits"
            else:
                result = f"The position of error is {len(arr_input) - correction + 1} from the left"
            return render_template('index.html', result=result, transferred_data=arr, input_data=data, error_data=arr_input)
        return render_template('index.html', transferred_data=arr, input_data=data)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
