import time

class waktu:
    def __init__(self):
        self.durasi = 300  # Durasi dalam detik (5 menit)
        self.start_time = time.time()
        self.day = 1

    def sisa_waktu(self):
        elapsed_time = time.time() - self.start_time
        sisa = max(0, self.durasi - elapsed_time)
        return int(sisa)
    
    def get_day(self):
        elapsed_time = time.time() - self.start_time
        self.day = int(elapsed_time // self.durasi) + 1
        return self.day
    
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