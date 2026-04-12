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
    
    def getday(self):
        elapsed_time = time.time() - self.start_time
        self.day = int(elapsed_time // self.durasi) + 1
        return self.day