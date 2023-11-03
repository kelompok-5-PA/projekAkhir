# projekAkhir
# Program Toko Custom Kain oleh Kelompok 5
Anggota :
1. Siti Annida Adzra (2309116013)
2. Dhea Amalia Putri (2309116037)
3. Noor Lintang Bhaskara (2309116030)

# Penjelasan Singkat Program
Berkain merupakan sebuah program sederhana yang menggunakan bahasa Python dan dapat memungkinkan penggunanya untuk membeli produk kain dengan pembayaran tunai maupun dengan e-Money. Berkain memiliki 2 mode yaitu mode admin dan customer, keduanya dapat melakukan registrasi dan login. Pada mode admin terdapat fitur CRUD untuk mengelola produk yang dijual di Berkain.

# Flowchart

**Menu Utama**

![image](https://github.com/kelompok-5-PA/projekAkhir/assets/143193920/55760fda-7f22-4920-9aff-85b08c06a190)



**Login**

![Login drawio](https://github.com/kelompok-5-PA/projekAkhir/assets/143193920/167e4123-8289-47ed-afcf-aa27c45c2c65)



**Register**

#![Regi drawio](https://github.com/kelompok-5-PA/projekAkhir/assets/143193920/08c498d7-81ba-4f6b-b4e9-9b89eeec3e6c)



**Menu Admin**

![Admin drawio](https://github.com/kelompok-5-PA/projekAkhir/assets/143193920/1daa312b-eab7-4507-81c9-ab15841fb211)


**Menu Customer**

![Customer drawio](https://github.com/kelompok-5-PA/projekAkhir/assets/143193920/39a8d7fb-1007-4fd1-8ec4-b11740e0fb32)


# Main Program

Yang akan muncul pertama pada menu awal adalah pesan selamat datang dan dapat memilih peran. Terdapat role admin dan customer, dan ada opsi leave.

<img width="378" alt="Screenshot 2023-11-03 225833" src="https://github.com/dheaamaliaptri/PA_1_Daspro/assets/144705099/541dfa2b-e749-4487-8227-79103f1c95b1">

Jika memilih opsi 1 (admin) akan muncul menu admin dengan opsi registrasi, login, dan leave. Saya akan mendemokan jika memilih opsi 2 atau login maka outputnya akan muncul seperti dibawah ini

<img width="282" alt="Screenshot 2023-11-03 234244" src="https://github.com/dheaamaliaptri/PA_1_Daspro/assets/144705099/9f714a4e-41ec-4e4b-8ad6-edacc9274598">

Perlu dipahami bahwa anda tidak bisa melakukan login jika belum melakukan registrasi, hal ini dikarenakan data anda belum tersimpan di database maka dari itu anda harus melakukan registrasi terlebih dahulu sebelum melakukan login

Setelah berhasil melakukan login akan muncul CRUD yang dapat dijalankan dengan bebas oleh admin

<img width="223" alt="Screenshot 2023-11-03 235020" src="https://github.com/kelompok-5-PA/projekAkhir/assets/144705099/2184f4cd-f89e-4009-853c-b7e8330ec07b">

Jika memilih opsi 2 (customer) akan muncul menu customer dengan opsi read menu, e-Money dan juga logout

<img width="221" alt="Screenshot 2023-11-03 235315" src="https://github.com/kelompok-5-PA/projekAkhir/assets/144705099/ccf19fbb-9989-45f8-9dfb-3f3e2c378ede">

Jika memilih opsi 1 yaitu read menu, pelanggan dapat melihat produk yang disediakan oleh Berkain

<img width="209" alt="Screenshot 2023-11-03 235413" src="https://github.com/kelompok-5-PA/projekAkhir/assets/144705099/29a9c6eb-39ca-49ef-9bb2-8b54212e25e5">

Jika pelanggan memilih untuk melanjutkan, program akan kembali ke awal di bagian menu customer. Jika memilih opsi 2 yaitu e-Money, pelanggan dapat melakukan topup saldo e-Money, pengecekan saldo, checkout, dan keluar.

<img width="190" alt="Screenshot 2023-11-03 235643" src="https://github.com/kelompok-5-PA/projekAkhir/assets/144705099/704e0602-ce75-4292-9e90-5b41732b021a">

Jika memilih opsi 1 pelanggan dapat melakukan topup dengan pilihan saldo yang telah disediakan oleh kami,

<img width="187" alt="Screenshot 2023-11-04 000202" src="https://github.com/kelompok-5-PA/projekAkhir/assets/144705099/f8d2ce30-2bfb-4e2e-b375-14b6efeb2c2d">

Setelah berhasil topup, maka saldo akan bertambah. Dan pelanggan bisa beralih ke opsi 3 yaitu checkout. Jika ingin membayar secara tunai pelanggan tidak perlu topup e-Money dan dapat langsung menuju ke opsi checkout

<img width="343" alt="Screenshot 2023-11-04 000602" src="https://github.com/kelompok-5-PA/projekAkhir/assets/144705099/739df729-e51a-47c3-b948-2d82cf337779">

Pelanggan dapat menambahkan produk yang diinginkan sebanyak-banyaknya selama persediaan stok mencukupi, jika sudah selesai memilih produk pelanggan dapat menekan 0 untuk lanjut ke pembayaran. Pelanggan dapat memilih ingin membayar secara tunai atau dengan e-Money, setelah selesai akan muncul invoice.

<img width="351" alt="Screenshot 2023-11-04 000804" src="https://github.com/kelompok-5-PA/projekAkhir/assets/144705099/251a0a79-7bae-43b7-9823-ae1b6edde23e">

Pengguna dapat memilih opsi 3 atau leave pada menu awal untuk keluar dari program

<img width="216" alt="Screenshot 2023-11-04 001129" src="https://github.com/kelompok-5-PA/projekAkhir/assets/144705099/5406cb24-8bd1-4f0e-9c30-648897b0c024">

Outputnya akan muncul terima kasih telah berkunjung di toko kami.
