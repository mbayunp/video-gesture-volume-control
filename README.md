# video-gesture-volume-control
Program untuk mengendalikan volume suara menggunakan gerakan tangan. Berikut adalah penjelasan dan tahapan proses dalam kode tersebut:

1. Import Library: Pertama, kita mengimpor beberapa library yang diperlukan yaitu `cv2` untuk pengolahan citra dan tampilan video, `mediapipe` untuk mendeteksi tangan dan landmark, `math` untuk perhitungan matematika, `numpy` untuk operasi pada array, dan `pyautogui` untuk mengendalikan volume suara pada sistem.

2. Menginisialisasi OpenCV VideoCapture: Kode menginisialisasi objek `VideoCapture` dari OpenCV untuk mendapatkan video dari sumber. Dalam contoh ini, sumber video yang digunakan adalah webcam dengan menggunakan `cap = cv2.VideoCapture(0)`.

3. Mengatur Ukuran Jendela Tampilan: Kode mengatur ukuran jendela tampilan video menggunakan `cv2.namedWindow()` dan `cv2.resizeWindow()` untuk memberikan nama dan mengubah ukuran jendela menjadi 800x600 piksel.

4. Mendeteksi Tangan: Kode menggunakan objek `Hands` dari `mediapipe` untuk mendeteksi tangan dalam video. Pengaturan seperti `static_image_mode`, `max_num_hands`, `min_detection_confidence`, dan `min_tracking_confidence` digunakan untuk mengatur deteksi tangan.

5. Loop Utama: Kode memasuki loop utama untuk membaca setiap frame video dari webcam.

6. Membalikkan Citra: Citra yang diterima dari webcam kemudian dibalikkan menggunakan `cv2.flip()` agar gerakan tangan terlihat seperti di cermin.

7. Konversi Citra BGR ke RGB: Citra yang dibaca dalam format BGR kemudian dikonversi menjadi RGB menggunakan `cv2.cvtColor()` untuk mengikuti format yang digunakan oleh `mediapipe`.

8. Mendeteksi Tangan pada Citra: Kode menggunakan objek `hands` untuk memproses citra dan mendeteksi tangan dalam citra.

9. Menggambar Landmark dan Garis Tangan: Jika tangan terdeteksi dalam citra, maka kode akan menggambar landmark tangan dan garis tangan yang menghubungkan landmark tersebut menggunakan `mp_drawing.draw_landmarks()`.

10. Mendapatkan Posisi Landmark Ibu Jari dan Telunjuk: Kode mendapatkan posisi landmark untuk ibu jari dan telunjuk menggunakan `hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]` dan `hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]`.

11. Mengubah Posisi Landmark menjadi Koordinat Piksel: Posisi landmark yang didapatkan dalam bentuk pecahan antara 0 hingga 1, kemudian dikalikan dengan lebar dan tinggi citra untuk mengubahnya menjadi koordinat piksel dalam citra.

12. Menggambar Garis Antara Ibu Jari dan Telunjuk: Kode menggambar garis antara posisi ibu jari dan telunjuk menggunakan `cv2.line()`.

13. Menghitung Jarak Antara Ibu Jari dan Telunjuk: Kode menghitung jarak antara posisi ibu jari dan telunjuk menggunakan formula Euclidean distance pada koordinat piksel.

14. Mengontrol Volume Berdasarkan Jarak: Kode mengontrol volume suara pada sistem berdasarkan jarak antara ibu jari dan telunjuk. Jarak dikonversi menjadi rentang nilai volume menggunakan `np.interp()`, kemudian volume suara ditingkatkan atau diturunkan menggunakan `pyautogui.press()` berdasarkan rentang nilai volume yang ditentukan.

15. Menampilkan Citra dengan Landmark dan Garis Tangan: Citra yang telah diolah dan ditambahkan landmark dan garis tangan akan ditampilkan menggunakan `cv2.imshow()`.

16. Menghentikan Program: Program akan berhenti dan keluar dari loop utama jika tombol 'q' pada keyboard ditekan menggunakan `cv2.waitKey()`.

17. Membersihkan: Setelah selesai, objek `VideoCapture` akan dilepas dan semua jendela tampilan ditutup menggunakan `cap.release()` dan `cv2.destroyAllWindows()`.

Demikian penjelasan tentang kode program yang diberikan. Kode tersebut membantu dalam mendeteksi gerakan tangan menggunakan `mediapipe` dan mengontrol volume suara pada sistem menggunakan `pyautogui`.
