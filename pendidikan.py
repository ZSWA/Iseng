#identitas dosen
nama = input ('Nama Dosen : ')
prodi = input ('Prodi : ')
fakultas = input ('Fakultas : ')
perguruan_tinggi = input ('Perguruan Tinggi : ')
ta = input ('Tahun Ajaran : ')
#1 pelaksanaan pendidikan
print('1. Pelaksanaan Pendidikan')
print()
#a. melaksanakan perkuliahan
print('Melaksanakan perkuliahan')
sks = int(input ("Masukan Jumlah SKS : "))
if sks > 10 :
  sksA = 0.5 #sks 10 pertama
  sks2 = sks - 10 # sks 2 berikutnya
  sksB = sks2 / 2 * 0.25

  status1_1a = input("Status sks awal (S/BL) : ")
  if status1_1a.upper() == "S" :
    nilai1_1a = sksA
  else :
    nilai1_1a = 0

  status1_1b = input("Status sks awal (S/BL) : ")
  if status1_1b.upper() == "S" :
    nilai1_1b = sksB
  else :
    nilai1_1b = 0

elif sks <= 10 :
  sksA = sks / 10 * 0.5
  status1_1a = input("Status sks akhir (S/BL) : ")
  
  if status1_1a.upper() == "S" :
    nilai1_1a = sksA
  else :
    nilai1_1a = 0
  nilai1_1b = 0

print("Nilai 1-1a = ", nilai1_1a)
print("Nilai 1-1b = ", nilai1_1b)
print()
#b membimbing mahasiswa seminar
print('Membimbing mahasiswa seminar')
seminar = input ('ada / tidak ada : ')
if seminar.upper() == "ADA" :
  status1_2 = input("Status kegiatan (S/BL) : ")
  if status1_2.upper() == "S" :
    nilai1_2 = 1
  else :
    nilai1_2 = 0
else :
  nilai1_2 = 0

print("Nilai 1-2 = ", nilai1_2)
print()
#c membimbing KP dan KKN
print('Membimbing KP dan KKN')
KP_dan_KKN = input ('ada / tidak ada :')
if KP_dan_KKN.upper() == "ADA" :
  status1_3 = input("Status kegiatan (S/BL) : ")
  if status1_3.upper() == "S" :
    nilai1_3 = 1
  else :
    nilai1_3 = 0
else :
  nilai1_3 = 0

print("Nilai 1-3 = ", nilai1_3)
print()
#d membimbing skripsi pembimbing utama
print('Membimbing Skripsi Pembimbing Utama')
skripsi_pembimbing_utama = input ('ada/tidak ada :')
if skripsi_pembimbing_utama.upper() == "ADA" :
  status1_4 = input("Status kegiatan (S/BL) : ")
  if status1_4.upper() == "S" :
    nilai1_4 = 2
  else :
    nilai1_4 = 0
else :
  nilai1_4 = 0

print("Nilai 1-4 = ", nilai1_4)
print()
#e membimbing skripsi pembimbing pendamping
print('Skripsi Pembimbing Pendamping')
Skripsi_Pembimbing_Pendamping = input ('ada/tidak ada :')
if Skripsi_Pembimbing_Pendamping.upper() == "ADA" :
  status1_5 = input("Status kegiatan (S/BL) : ")
  if status1_5.upper() == "S" :
    nilai1_5 = 1
  else :
    nilai1_5 = 0
else :
  nilai1_5 = 0

print("Nilai 1-5 = ", nilai1_5)
print()
#f Ketua Penguji Skripsi
print('Ketua Penguji Skripsi')
Ketua_Penguji_Skripsi = input ('ada/tidak ada :')
if Ketua_Penguji_Skripsi.upper() == "ADA" :
  status1_6 = input("Status kegiatan (S/BL) : ")
  if status1_6.upper() == "S" :
    nilai1_6 = 1
  else :
    nilai1_6 = 0
else :
  nilai1_6 = 0

print("Nilai 1-6 = ", nilai1_6)
print()
#g Anggota Penguji Skripsi
print('Anggota Penguji Skripsi')
Anggota_Penguji_Skripsi = input ('ada/tidak :')
if Anggota_Penguji_Skripsi.upper() == "ADA" :
  status1_7 = input("Status kegiatan (S/BL) : ")
  if status1_7.upper() == "S" :
    nilai1_7 = 0.5
  else :
    nilai1_7 = 0
else :
  nilai1_7 = 0

print("Nilai 1-7 = ", nilai1_7)
print()
#h Melakukan Bimbingan Akademik (DPA)
print('DPA')
DPA = input ('ada/tidak :')
if DPA.upper() == "ADA" :
  status1_8 = input("Status kegiatan (S/BL) : ")
  if status1_8.upper() == "S" :
    nilai1_8 = 2
  else :
    nilai1_8 = 0
else :
  nilai1_8 = 0

print("Nilai 1-8 = ", nilai1_8)
print()
#i Membuat Buka Ajar
print('Membuat Buku Ajar')
Buku_Ajar = int(input ('Jumlah buku : '))
if Buku_Ajar >= 1:
  status1_9 = input("Status kegiatan (S/BL) : ")
  if status1_9.upper() == "S" :
    nilai1_9 = Buku_Ajar*5
  else :
    nilai1_9 = 0
else :
  nilai1_9 = 0

print("Nilai 1-9 = ", nilai1_9)
print()
#j Membuat Modul Praktikum
print('Modul Praktikum')
Modul_Praktikum = int(input ('jumlah modul : '))
if Modul_Praktikum >= 1:
  status1_10 = input("Status kegiatan (S/BL) : ")
  if status1_10.upper() == "S" :
    nilai1_10 = Modul_Praktikum*3
  else :
    nilai1_10 = 0
else :
  nilai1_10 = 0

print("Nilai 1-10 = ", nilai1_10)
print()
print()
#2 Pelaksanaan Penelitian
print('2. Pelaksanaan Penelitian')
print()
#a Publikasi Jurnal Internasional Bereputasi
print('Publikasi Jurnal Internasional Bereputasi')
Publikasi_Jurnal_Internasional_Bereputasi = int(input ('Jumlah Jurnal :'))
if Publikasi_Jurnal_Internasional_Bereputasi >= 1:
  status2_1 = input("Status kegiatan (S/BL) : ")
  if status2_1.upper() == "S" :
    nilai2_1 = Publikasi_Jurnal_Internasional_Bereputasi*12
  else :
    nilai2_1 = 0
else :
  nilai2_1 = 0

print("Nilai 2-1 = ", nilai2_1)
print()
#b Publikasi Jurnal Internasional Tidak Bereputasi
print('Publikasi Jurnal Internasional Tidak Bereputasi')
Publikasi_Jurnal_Internasional_Tidak_Bereputasi = int(input ('Jumlah Jurnal :'))
if Publikasi_Jurnal_Internasional_Tidak_Bereputasi >= 1:
  status2_2 = input("Status kegiatan (S/BL) : ")
  if status2_2.upper() == "S" :
    nilai2_2 = Publikasi_Jurnal_Internasional_Tidak_Bereputasi*10
  else :
    nilai2_2 = 0
else :
  nilai2_2 = 0

print("Nilai 2-2 = ", nilai2_2)
print()
#c Publikasi Jurnal Nasional Terakreditasi
print('Publikasi Jurnal Nasional Terakreditasi')
Publikasi_Jurnal_Nasional_Terakreditasi = int(input ('Jumlah Jurnal :'))
if Publikasi_Jurnal_Nasional_Terakreditasi >= 1:
  status2_3 = input("Status kegiatan (S/BL) : ")
  if status2_3.upper() == "S" :
    nilai2_3 = Publikasi_Jurnal_Nasional_Terakreditasi*6
  else :
    nilai2_3 = 0
else :
  nilai2_3 = 0

print("Nilai 2-3 = ", nilai2_3)
print()
#d Publikasi Jurnal Nasional Tidak Terakreditasi
print('Publikasi Jurnal Nasional Tidak Terakreditasi')
Publikasi_Jurnal_Nasional_Tidak_Berakreditasi = int(input ('Jumlah Jurnal :'))
if Publikasi_Jurnal_Nasional_Tidak_Berakreditasi >= 1:
  status2_4 = input("Status kegiatan (S/BL) : ")
  if status2_4.upper() == "S" :
    nilai2_4 = Publikasi_Jurnal_Nasional_Tidak_Berakreditasi*5
  else :
    nilai2_4 = 0
else :
  nilai2_4 = 0

print("Nilai 2-4 = ", nilai2_4)
print()
#e Publikasi Pada Seminar Internasional
print('Publikasi Pada Seminar Internasional')
Publikasi_Pada_Seminar_Internasional = int(input ('Jumlah Makalah :'))
if Publikasi_Pada_Seminar_Internasional >= 1:
  status2_5 = input("Status kegiatan (S/BL) : ")
  if status2_5.upper() == "S" :
    nilai2_5 = Publikasi_Pada_Seminar_Internasional*8
  else :
    nilai2_5 = 0
else :
  nilai2_5 = 0

print("Nilai 2-5 = ", nilai2_5)
print()
#f Publikasi Pada Seminar Nasional
print('Publikasi Pada Seminar Nasional')
Publikasi_Pada_Seminar_Nasional = int(input ('Jumlah Makalah : '))
if Publikasi_Pada_Seminar_Nasional >= 1:
  status2_6 = input("Status kegiatan (S/BL) : ")
  if status2_6.upper() == "S" :
    nilai2_6 = Publikasi_Pada_Seminar_Nasional*6
  else :
    nilai2_6 = 0
else :
  nilai2_6 = 0

print("Nilai 2-6 = ", nilai2_6)
print()
print()
#3 Pelaksanaan Pengabdian
print('3. Pelaksanaan Pengabdian')
print()
#a Mengembangkan Hasil Pendidikan dan Penelitian 
print('Mengembangkan Hasil Pendidikan dan Penelitian')
Mengembangkan_Hasil_Pendidikan_dan_Penelitian = int(input('Jumlah Program : '))
if Mengembangkan_Hasil_Pendidikan_dan_Penelitian >= 1:
  status3_1 = input("Status kegiatan (S/BL) : ")
  if status3_1.upper() == "S" :
    nilai3_1 = Mengembangkan_Hasil_Pendidikan_dan_Penelitian*2
  else :
    nilai3_1 = 0
else :
  nilai3_1 = 0

print("Nilai 3-1 = ", nilai3_1)
print()
#b Memberikan pelatihan/penyuluhan/penataran/ceramah pada masyarakat (internasional)
print('Memberikan pelatihan/penyuluhan/penataran/ceramah pada masyarakat (internasional)')
Memberikan_pelatihan_penyuluhan_penataran_ceramah_pada_masyarakat_internasional = int(input ('Jumlah Program :'))
if Memberikan_pelatihan_penyuluhan_penataran_ceramah_pada_masyarakat_internasional >= 1:
  status3_2 = input("Status kegiatan (S/BL) : ")
  if status3_2.upper() == "S" :
    nilai3_2 = Memberikan_pelatihan_penyuluhan_penataran_ceramah_pada_masyarakat_internasional*3
  else :
    nilai3_2 = 0
else :
  nilai3_2 = 0

print("Nilai 3-2 = ", nilai3_2)
print()
#c Memberikan pelatihan/penyuluhan/penataran/ceramah pada masyarakat (nasional)
print('Memberikan pelatihan/penyuluhan/penataran/ceramah pada masyarakat (nasional)')
Memberikan_pelatihan_penyuluhan_penataran_ceramah_pada_masyarakat_nasional = int(input ('Jumlah Program :'))
if Memberikan_pelatihan_penyuluhan_penataran_ceramah_pada_masyarakat_nasional >= 1:
  status3_3 = input("Status kegiatan (S/BL) : ")
  if status3_3.upper() == "S" :
    nilai3_3 = Memberikan_pelatihan_penyuluhan_penataran_ceramah_pada_masyarakat_nasional*2
  else :
    nilai3_3 = 0
else :
  nilai3_3 = 0

print("Nilai 3-3 = ", nilai3_3)
print()
#d Memberikan pelatihan/penyuluhan/penataran/ceramah pada masyarakat (lokal)
print('Memberikan pelatihan/penyuluhan/penataran/ceramah pada masyarakat (lokal)')
Memberikan_pelatihan_penyuluhan_penataran_ceramah_pada_masyarakat_lokal = int(input ('Jumlah Program :'))
if Memberikan_pelatihan_penyuluhan_penataran_ceramah_pada_masyarakat_lokal >= 1:
  status3_4 = input("Status kegiatan (S/BL) : ")
  if status3_4.upper() == "S" :
    nilai3_4 = Memberikan_pelatihan_penyuluhan_penataran_ceramah_pada_masyarakat_lokal*1
  else :
    nilai3_4 = 0
else :
  nilai3_4 = 0

print("Nilai 3-4 = ", nilai3_4)
print()
#e Membuat/Menulis karya pengabdian
print('Membuat/Menulis karya pengabdian')
Membuat_Menulis_karya_pengabdian = int(input ('Jumlah Karya :'))
if Membuat_Menulis_karya_pengabdian >= 1:
  status3_5 = input("Status kegiatan (S/BL) : ")
  if status3_5.upper() == "S" :
    nilai3_5 = Membuat_Menulis_karya_pengabdian*2
  else :
    nilai3_5 = 0
else :
  nilai3_5 = 0

print("Nilai 3-5 = ", nilai3_5)
print()
print()
#4 Penunjang
print('4. Penunjang')
print()
#a Menjadi Anggota dalam Suatu Panitia/badan pada perguruan tinggi(sebagai ketua)
print('Menjadi Anggota dalam Suatu Panitia/badan pada perguruan tinggi(sebagai ketua)')
Menjadi_Anggota_dalam_Suatu_Panitia_badan_pada_perguruan_tinggi_sebagai_ketua = input ('ada / tidak ada :')
if Menjadi_Anggota_dalam_Suatu_Panitia_badan_pada_perguruan_tinggi_sebagai_ketua.upper() == "ADA" :
  status4_1 = input("Status kegiatan (S/BL) : ")
  if status4_1.upper() == "S" :
    nilai4_1 = 1.5
  else :
    nilai4_1 = 0
else :
  nilai4_1 = 0

print("Nilai 4-1 = ", nilai4_1)
print()
#b Menjadi Anggota dalam Suatu Panitia/badan pada perguruan tinggi(sebagai anggota)
print('Menjadi Anggota dalam Suatu Panitia/badan pada perguruan tinggi(sebagai anggota)')
Menjadi_Anggota_dalam_Suatu_Panitia_badan_pada_perguruan_tinggi_sebagai_anggota = input ('ada / tidak ada :')
if Menjadi_Anggota_dalam_Suatu_Panitia_badan_pada_perguruan_tinggi_sebagai_anggota.upper() == "ADA" :
  status4_2 = input("Status kegiatan (S/BL) : ")
  if status4_2.upper() == "S" :
    nilai4_2 = 1
  else :
    nilai4_2 = 0
else :
  nilai4_2 = 0

print("Nilai 4-2 = ", nilai4_2)
print()
#c Menjadi Anggota dalam suatu panitia/badan pada lembaga pemerintahan(sebagai ketua)
print('Menjadi Anggota dalam suatu panitia/badan pada lembaga pemerintahan(sebagai ketua)')
Menjadi_Anggota_dalam_suatu_panitia_badan_pada_lembaga_pemerintahan_sebagai_ketua = input ('ada / tidak ada :')
if Menjadi_Anggota_dalam_suatu_panitia_badan_pada_lembaga_pemerintahan_sebagai_ketua.upper() == "ADA" :
  status4_3 = input("Status kegiatan (S/BL) : ")
  if status4_3.upper() == "S" :
    nilai4_3 = 2
  else :
    nilai4_3 = 0
else :
  nilai4_3 = 0

print("Nilai 4-3 = ", nilai4_3)
print()
#d Menjadi Anggota dalam suatu panitia/badan pada lembaga pemerintahan(sebagai anggota)
print('Menjadi Anggota dalam suatu panitia/badan pada lembaga pemerintahan(sebagai anggota)')
Menjadi_Anggota_dalam_suatu_panitia_badan_pada_lembaga_pemerintahan_sebagai_anggota = input ('ada / tidak ada :')
if Menjadi_Anggota_dalam_suatu_panitia_badan_pada_lembaga_pemerintahan_sebagai_anggota.upper() == "ADA" :
  status4_4 = input("Status kegiatan (S/BL) : ")
  if status4_4.upper() == "S" :
    nilai4_4 = 1
  else :
    nilai4_4 = 0
else :
  nilai4_4 = 0

print("Nilai 4-4 = ", nilai4_4)
print()
#e Menjadi Anggota organisi profesi dosen tingkat internasioanl sebagai pengurus
print('Menjadi Anggota organisi profesi dosen tingkat internasional sebagai pengurus')
Menjadi_Anggota_organisi_profesi_dosen_tingkat_internasional_sebagai_pengurus = input ('ada / tidak ada :')
if Menjadi_Anggota_organisi_profesi_dosen_tingkat_internasional_sebagai_pengurus.upper() == "ADA" :
  status4_5 = input("Status kegiatan (S/BL) : ")
  if status4_5.upper() == "S" :
    nilai4_5 = 2
  else :
    nilai4_5 = 0
else :
  nilai4_5 = 0

print("Nilai 4-5 = ", nilai4_5)
print()
#f Menjadi Anggota organisasi profesi dosen tingkat internasional sebagai anggota
print('Menjadi Anggota organisasi profesi dosen tingkat internasional sebagai anggota')
Menjadi_Anggota_organisasi_profesi_dosen_tingkat_internasional_sebagai_anggota = input ('ada / tidak ada :')
if Menjadi_Anggota_organisasi_profesi_dosen_tingkat_internasional_sebagai_anggota.upper() == "ADA" :
  status4_6 = input("Status kegiatan (S/BL) : ")
  if status4_6.upper() == "S" :
    nilai4_6 = 0.5
  else :
    nilai4_6 = 0
else :
  nilai4_6 = 0

print("Nilai 4-6 = ", nilai4_6)
print()
#g Menjadi Anggota organisasi profesi dosen tingkat nasional sebagai pengurus
print('Menjadi Anggota organisasi profesi dosen tingkat nasional sebagai pengurus')
Menjadi_Anggota_organisasi_profesi_dosen_tingkat_nasional_sebagai_pengurus = input ('ada / tidak ada :')
if Menjadi_Anggota_organisasi_profesi_dosen_tingkat_nasional_sebagai_pengurus.upper() == "ADA" :
  status4_7 = input("Status kegiatan (S/BL) : ")
  if status4_7.upper() == "S" :
    nilai4_7 = 2
  else :
    nilai4_7 = 0
else :
  nilai4_7 = 0

print("Nilai 4-7 = ", nilai4_7)
print()
#h Menjadi Anggota organisasi profesi dosen tingkat nasional sebagai anggota
print('Menjadi Anggota organisasi profesi dosen tingkat nasional sebagai anggota')
Menjadi_Anggota_organisasi_profesi_dosen_tingkat_nasional_sebagai_anggota = input ('ada / tidak ada :')
if Menjadi_Anggota_organisasi_profesi_dosen_tingkat_nasional_sebagai_anggota.upper() == "ADA" :
  status4_8 = input("Status kegiatan (S/BL) : ")
  if status4_8.upper() == "S" :
    nilai4_8 = 0.5
  else :
    nilai4_8 = 0
else :
  nilai4_8 = 0

print("Nilai 4-8 = ", nilai4_8)
print()
print()
print("="*80)
#akumulasi
Pendidikan = nilai1_1a + nilai1_1b + nilai1_2 + nilai1_3 + nilai1_4 + nilai1_5 + nilai1_6 + nilai1_7 + nilai1_8 + nilai1_9 + nilai1_10
Penelitian = nilai2_1 + nilai2_2 + nilai2_3 + nilai2_4 + nilai2_5 + nilai2_6
Pengabdian = nilai3_1 + nilai3_2 + nilai3_3 + nilai3_4 + nilai3_5
Penunjang = nilai4_1 + nilai4_2 + nilai4_3 + nilai4_5 + nilai4_6 + nilai4_7 + nilai4_8
Pendidikan_Penelitian = Pendidikan + Penelitian
Pengabdian_Penunjang = Pengabdian + Penunjang
Total_Kinerja = Pendidikan+Penelitian+Pengabdian+Penunjang

#kesimpulan
if Pendidikan > 0 :
  Kesimpulan_Pendidikan = "Memenuhi"
else:
  Kesimpulan_Pendidikan = "Tidak Memenuhi"

if Penelitian > 0 :
  Kesimpulan_Penelitian = "Memenuhi"
else:
  Kesimpulan_Penelitian = "Tidak Memenuhi"

if Pengabdian > 0 :
  Kesimpulan_Pengabdian = "Memenuhi"
else:
  Kesimpulan_Pengabdian = "Tidak Memenuhi"

if Pendidikan_Penelitian >= 9 :
  Kesimpulan_Pendidikan_Penelitian = "Memenuhi"
else:
  Kesimpulan_Pendidikan_Penelitian = "Tidak Memenuhi"

if Pengabdian_Penunjang >= 3 :
  Kesimpulan_Pengabdian_Penunjang = "Memenuhi"
else:
  Kesimpulan_Pengabdian_Penunjang = "Tidak Memenuhi"

if 12<= Total_Kinerja <= 16 :
  Kesimpulan_Total = "Memenuhi"
else :
  Kesimpulan_Total = "Tidak Memenuhi"

if Kesimpulan_Pendidikan == "Memenuhi" and Kesimpulan_Penelitian == "Memenuhi" and Kesimpulan_Pengabdian == "Memenuhi" and Kesimpulan_Pendidikan_Penelitian == "Memenuhi" and Kesimpulan_Pengabdian_Penunjang == "Memenuhi" and Kesimpulan_Total == "Memenuhi" :
  Kesimpulan_Akhir = "Memenuhi Syarat UU"
else :
  Kesimpulan_Akhir = "Tidak Memenuhi Syarat UU"

#hasil
print("Nama dosen : ",nama)
print("Prodi : ",prodi)
print("Fakultas : ",fakultas)
print("Perguruan Tinggi : ",perguruan_tinggi)
print("Tahun Ajaran : ",ta)
print()
print("Pendidikan | Kinerja = ", Pendidikan, "SKS | Kesimpulan", Kesimpulan_Pendidikan,"|")
print("Penelitian | Kinerja = ", Penelitian, "SKS | Kesimpulan", Kesimpulan_Penelitian,"|")
print("Pengabdian | Kinerja = ", Pengabdian, "SKS | Kesimpulan", Kesimpulan_Pengabdian,"|")
print("Pendidikan + Penelitian | Kinerja = ", Pendidikan_Penelitian, "SKS | Kesimpulan", Kesimpulan_Pendidikan_Penelitian,"|")
print("Pengabdian + Penunjang | Kinerja = ", Pengabdian_Penunjang, "SKS | Kesimpulan", Kesimpulan_Pengabdian_Penunjang,"|")
print("Total Kinerja | Kinerja = ", Total_Kinerja, "SKS | Kesimpulan", Kesimpulan_Total,"|")
print()
print("Kesimpulan Akhir : ", Kesimpulan_Akhir)