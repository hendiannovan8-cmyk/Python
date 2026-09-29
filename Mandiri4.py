print("=== Mini FAQ Chatbot ===")
kode = input("Tanyakan apa saja: ").lower()

if "peminjaman" in kode:
    print ("Syarat Utama: Mahasiswa wajib menunjukkan Kartu Tanda Mahasiswa (KTM) yang masih aktif kepada petugas perpustakaan." \
    "Batas Waktu Peminjaman: buku umumnya dapat dipinjam dalam jangka waktu tertentu (biasanya maksimal 1 hingga 2 minggu) ")
elif "operasional" in kode:
    print ("Proses peminjaman dapat dilakukan pada jam operasional perpustakaan, yaitu Senin - Jumat pukul 08.00 - 16.00.")
else :
    print ("Maaf, pertanyaan tidak dikenali. Silakan hubungi petugas perpustakaan")
