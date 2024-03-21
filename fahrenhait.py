def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

# Meminta input dari pengguna untuk suhu dalam Celcius
celsius = float(input("Masukkan suhu dalam Celcius: "))

# Mengkonversi suhu dari Celcius ke Fahrenheit
fahrenheit = celsius_to_fahrenheit(celsius)

# Mencetak hasil konversi
print("{} derajat Celsius sama dengan {} derajat Fahrenheit.".format(celsius, fahrenheit))
