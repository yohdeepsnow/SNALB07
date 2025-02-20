#tolong lengkapi fungsi python berikut untuk membuat kalkulator sederhana
#buat dengan format yang sama

def penambahan(a, b):
    total = a + b
    return total

def pengurangan(a, b):
    total = a - b
    return total

def perkalian(a, b):
    total = a * b
    return total

def pembagian(a, b):
    if b != 0:
        total = a / b
        return total
    else:
        return "Error: Pembagi tidak boleh 0"

def main():
    print("Penambahan: ", penambahan(10, 5))
    print("Pengurangan: ", pengurangan(10, 5))
    print("Perkalian: ", perkalian(10, 5))
    print("Pembagian: ", pembagian(10, 5))
    print("Pembagian dengan 0: ", pembagian(10, 0))

main()
