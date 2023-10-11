def input_matematika():
    print("=" * 25)
    print("operasi matematika")
    print(" 1. jumlah \t [+]")
    print(" 2. jumlah \t [-]")
    print(" 3. jumlah \t [*]")
    print(" 4. jumlah \t [/]")
    print("=" * 25)
    operasi_matematika()

def operasi_matematika():
    operasi = input("pilih operasi (1/2/3/4): ")
    bil_1 = eval(input("masukkan bilangan pertama: "))
    bil_2 = eval(input("masukkan bilangan kedua: "))

    print("=" * 25)

    if operasi == "1":
        hasil = bil_1 + bil_2
        print(f"hasil operasi dari {bil_1} + {bil_2} = {hasil}")
        return hasil

    elif operasi == "2":
        hasil = bil_1 - bil_2
        print(f"hasil operasi dari {bil_1} - {bil_2} = {hasil}")
        return hasil

    elif operasi == "3":
        hasil = bil_1 * bil_2
        print(f"hasil operasi dari {bil_1} * {bil_2} = {hasil}")
        return hasil

    elif operasi == "4":
        hasil = bil_1 / bil_2
        print(f"hasil operasi dari {bil_1} / {bil_2} = {hasil}")
        return hasil

    else:
        print("operasi tidak valid")
        return False

# input_matematika()