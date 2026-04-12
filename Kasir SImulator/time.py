import time

class waktu:
    def __init__(self):
        self.durasi = 300  # Durasi dalam detik (5 menit)
        self.sisa_waktu = self.durasi
        self.start_time = time.time()

        def get_sisa_waktu(self):
            elapsed_time = time.time() - self.start_time
            self.sisa_waktu = max(0, self.durasi - elapsed_time)
            return self.sisa_waktu