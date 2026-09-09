Nama : Fadlan Fathul Islam

NPM : 2506601275

Kelas : PBP B 

### Tugas 1
1. Pada Tutorial dan Tugas 1, Anda diberi kebebasan untuk menentukan tampilan dari website portofolio Anda. Saat Anda merancang struktur HTML yang digunakan, apakah Anda menggunakan elemen semantik HTML5 seperti <section>, <article>, atau <aside>? Jika iya, bagaimana elemen tersebut membantu Anda dalam membuat static web? Jika tidak, mengapa tanpa elemen tersebut sudah memenuhi kebutuhan desain Anda?
Ya, saya menggunakan section sebagai pemisah antar-halaman yang saya buat. Tidak hanya pemisah secara harfiah, tapi dengan membagi website saya menjadi bagian yang berbeda-beda membuat saya lebih mudah untuk memvisualisasikan hasil akhirnya sehingga penggunaan CSS menjadi lebih terarah (karena sudah memiliki gambaran berdasarkan bagian)

2. Ketika Anda mengatur CSS Anda agar tetap responsive, tantangan tata letak apa yang Anda temukan? Bagaimana Anda mengevaluasi elemen mana yang harus diubah posisinya atau diprioritaskan ukurannya saat berpindah dari tampilan desktop ke mobile?
Untuk tugas individu 1 ini sebetulnya saya belum terlalu merasa kesulitan karena websitenya masih sederhana dan elemen-elemen yang saya gunakan juga masih sedikit. Tapi mungkin untuk kedepannya ketika elemen di layar semakin banyak saya harus mulai mempertimbangkan untuk menyesuaikan tampilan website ketika dibuka di mobile agar tampilan halaman tidak rusak. dan juga mungkin saya akan memindahkan navbar ke menu samping untuk mobile agar menghemat tempat serta memodifikasi tombol agar lebih mudah diklik menggunakan jari karena di website ini rata rata tombolnya diklik menggunakan kursor.

3. Website yang Anda buat saat ini adalah static web murni. Batasan apa yang Anda rasakan saat mencoba menyajikan informasi pada portofolio Anda secara optimal? Berdasarkan batasan tersebut, fungsionalitas dinamis apa yang paling ingin Anda persiapkan dan tambahkan pada iterasi proyek selanjutnya?
Salah satu yang saya rasakan adalah ketika kita ingin menambahkan sesuatu seperti skill, project, atau yang saya buat yaitu certificate baru. Tanpa database, kita harus selalu menulis ulang kode ketika menambahkan semua itu. Saya ingin tahu apakah dengan database saya masih harus menulis ulang atau copy paste kode kode saya atau prosesnya akan jadi lebih mudah?(karena saya belum pernah mempelajari database sebelumnya)

AI Disclosure:
Flow dalam pengembangan website di Tugas Individu 1 ini sebagian besar berjalan dengan bantuan AI lebih tepatnya Gemini AI 3.1 Pro. Awalnya saya berencana mengerjakan tugas ini di hari sabtu dan minggu karena sebelumnya saya memprioritaskan tugas yang deadlinenya paling dekat. Tapi ternyata dari hari jumat malam sampai minggu saya terkena demam dan drop sehingga tidak sempat membuka laptop. Dan tidak terasa waktu yang saya miliki hanya tinggal 12 jam sebelum deadline pengumpulan. Tapi karena sebelumnya saya sudah pernah membuat website serupa, saya tetap coba menyelesaikannya dengan bantuan AI. Bantuan AI tersebut kebanyakan tentang konfirmasi keputusanku dalam menulis kode misal "apakah kalau kutulis begini tampilannya akan seperti ini?", bantuan debug kode, dan tentang syntax syntax yang saya tidak hafal. Saya juga selalu meminta agar AI tidak langsung memberikan kode mentah melainkan menjelaskan apa yang harus kulakukan. Saya mengubah tema website dari terang ke gelap dan menambahkan section certificates yang menampilkan beberapa sertifikat yang saya miliki. berikut riwayat percakapan saya dengan gemini:
https://share.gemini.google/OuHS9eMl6f7g
Gaya prompting yang saya lakukan lebih seperti percakapan atau diskusi sehingga kadang saya merasa AI terlalu percaya diri. Jadi mungkin ada beberapa prompt yang seharusnya tidak diperlukan.
Untuk pemilihan warna sendiri jika ternyata kurang cocok sebenarnya bukan kesalahan dari AI melainkan dari diri saya sendiri yang pada dasarnya tidak pandai dalam hal desain dan komposisi warna.  

### Tugas 2
1. Jelaskan alur yang terjadi ketika pengguna membuka halaman portofolio baru, mulai dari permintaan yang diterima proyek hingga data ditampilkan pada browser. Dalam jawabanmu, jelaskan peran urls.py proyek, urls.py aplikasi, view, model, dan template.
Pertama browser melakukan request ke server django. Lalu request ini diterima oleh urls.py yang berada di portofolio. kalau pathnya admin akan diarahkan ke menu admin, kalau pathnya kosong akan diarahkan ke main. jika ke main, request akan diatur oleh urls.py untuk menampilkan halaman yang mana (show di views). Setelah memanggil show_..., views akan mencocokkan show yang dimaksud dan meminta data ke models terkait lalu dikirim lagi ke views. Ia "membungkus" data itu ke dalam context dan mengirimkannya ke template lalu dikirimkan ke browser

2. Mengapa data untuk bagian portofolio baru sebaiknya disimpan pada model dan tidak ditulis langsung di dalam template? Jelaskan dampaknya terhadap kemudahan pemeliharaan dan pengembangan aplikasi.
Karena kalau kita langsung melakukan HardCode di dalam template itu akan membuat kode menjadi tidak rapih dan jika kita ingin menambah sesuatu, kita harus menulis secara manual lagi di dalam template. Sedangkan kalau kita pakai model kita tinggal menulis di template secara general (misal {{nama}}) dan itu akan menyesuaikan apa yang ada di dalam model.

3. Apa perbedaan fungsi makemigrations dan migrate pada Django? Berikan contoh perubahan model yang mengharuskanmu menjalankan kedua perintah tersebut.
Menurut saya makemigrations itu semacam blueprintnya sedangkan migrate adalah yang benar benar mengeksekusi (seperti arsitek dan tukang). Seperti yang tertulis di tutorial 2, kita harus menggunakan keduanya ketika kita ingin mengubah atau mengganti apapun yang ada di models meskipun hanya memperbaiki typo.

AI Disclosure:
Pada tugas kedua ini saya hanya menggunakan AI (Gemini Pro 3.1) untuk memahami konsep alur request, meminta penjelasan tentang syntax baru (article, span), dan juga proses debug. Untuk alur pengerjaan dari awal sampai akhir kurang lebih sama seperti tutorial 2 sehingga saya tidak butuh bantuan AI untuk melakukannya. Saya lebih banyak me-"reuse" dan memodifikasi kode yang diberikan di tutorial 2 karena fitur yang saya buat sama-sama berfungsi untuk menampilkan sesuatu.