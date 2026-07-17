import random

def generate_data(jumlah_data):
    data = []
    for _ in range(jumlah_data):
        value = random.randint(1,100)
        data.append(value)
    return data

def input_data():
    jumlah_data = int(input("masukan jumlah data yang ingin di generate: "))
    return jumlah_data


def shorting_bobble(data):
    banyak_data = len(data)
    for index in range(banyak_data):
        for value in range(0,banyak_data - index - 1):
            if data[value] > data[value + 1]:
                temp = data[value]
                data[value] = data[value + 1]
                data[value + 1] = temp

def shorting_seletion(data):
    banyak_data = len(data)
    for index in range(banyak_data):
        min_index = index
        for value in range(index +1, banyak_data):
            if data[value] < data[min_index]:
                min_index = value

        data[index],data[min_index]=data[min_index],data[index]
    
def insertion_sort(data):
    for index in range(1,len(data)):
        min_value = data[index]
        value = index - 1
        while value >= 0 and min_value < data[value]:
            data[value + 1] = data[value]
            value -= 1
        data[value + 1] = min_value

def merge_sort(data):
    if len(data) > 1 :
        index_tengah = len(data) // 2
        data_kiri = data[:index_tengah]
        data_kanan = data[index_tengah:]

        merge_sort(data_kiri) #rekursif, ini bisa terjadi infinit loop
        merge_sort(data_kanan)
        # index = 0
        # value = 0 
        # data_real = 0
        index = value = data_real = 0

        while index < len(data_kiri) and value < len(data_kanan):
            if data_kiri[index] < data_kanan[value]:
                data[data_real] = data_kiri[index]
                index += 1
            else :
                data[data_real] = data_kanan[value]
                value += 1
            data_real += 1
        

        while index < len(data_kiri):
            data[data_real] = data_kiri[index]
            index += 1
            data_real +=1

        while value < len(data_kanan):
            data[data_real] = data_kanan[value]
            value += 1
            data_real +=1


if __name__ == "__main__":
    jumlah_data = input_data()
    data = generate_data(jumlah_data)
    print("Data sebelum di shorting: ")
    print(data)
    input("Tekan Enter untuk melakukan shorting data...")
    # shorting_bobble(data)
    # shorting_seletion(data)
    # insertion_sort(data)
    merge_sort(data)
    print("Data setelah di shorting: ")
    print(data)