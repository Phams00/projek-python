import time

class waktu:
    def __init__(self):
        self.durasi = 300  # Durasi dalam detik (5 menit)
        self.start_time = time.time()
        self.day = 1

    def sisa_waktu(self):                               #sistem loop sisa waktu dan sekali loop day nambah 1
        elapsed_time = time.time() - self.start_time 
        sisa = max(0, self.durasi - elapsed_time)
        if sisa == 0:
            self.day += 1
            self.start_time = time.time()
        return int(sisa)
    
    def format_time(self, sisa):
        menit = sisa // 60
        detik = sisa % 60
        return f"{menit:02d}:{detik:02d}"
    
    def jalankan_timer(self):
        while True:
            time.sleep(1)
            if self.sisa_waktu() <= 0:
                print("\nWaktu habis! lanjut ke hari berikutnya.")
                self.day += 1
                self.start_time = time.time()
                break