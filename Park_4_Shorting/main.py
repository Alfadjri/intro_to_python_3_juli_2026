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



if __name__ == "__main__":
    jumlah_data = input_data()
    data = generate_data(jumlah_data)
    print("Data sebelum di shorting: ")
    print(data)
    input("Tekan Enter untuk melakukan shorting data...")
    shorting_bobble(data)
    print("Data setelah di shorting: ")
    print(data)