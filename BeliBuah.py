#Masukkan Uang
money = 16

#harga per buah
items = {'anggur': 5, 'pisang': 4, 'jeruk': 3}
for item_name in items:
    print('--------------------------------------------------')
    print('Anda memiliki ' + str(money) + ' Ribu Rupiah di dompet Anda')
    print('Harga setiap ' + item_name + ' ' + str(items[item_name]) + ' Ribu Rupiah')
    
    input_count = input('Mau berapa ' + item_name + '?:')
    print('Anda akan membeli ' + input_count + ' ' + item_name)
    
    count = int(input_count)
    total_price = items[item_name] * count
    print('Harga total adalah ' + str(total_price) + ' Ribu Rupiah')
    
    if money >= total_price:
        print('Anda telah membeli ' + input_count + ' ' + item_name)
        money -= total_price
        # Ketika money sama dengan 0, cetak 'Dompet Anda kosong' dan hentikan loop
        if money == 0:
            print('Dompet Anda kosong')
            break
        
        
    else:
        print('Uang Anda tidak mencukupi')
        print('Anda tidak dapat membeli ' + item_name + ' sebanyak itu')
# Menggunakan variable money dan tipe conversion, cetak 'Uang Anda tinggal ___ dolar'
print('Uang Anda tinggal ' + str(money) + ' Rupiah')