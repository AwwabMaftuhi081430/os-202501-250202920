import time
import os

def cpu_stress():
    print("--- Memulai Komputasi Berat (CPU Stress) ---")
    start_time = time.time()
    while time.time() - start_time < 15:
        _ = 12345 * 67890
    print("--- Selesai Tes CPU ---")

def memory_stress():
    print("--- Memulai Alokasi Memori Bertahap ---")
    data = []
    try:
        for i in range(1, 11):
            chunk = ' ' * (50 * 1024 * 1024)
            data.append(chunk)
            print(f"Iterasi {i}: Mengalokasikan ~{i * 50} MB")
            time.sleep(2) 
    except MemoryError:
        print("Error: Batas memori tercapai!")

if __name__ == "__main__":
    print(f"PID Program: {os.getpid()}")
    cpu_stress()
    memory_stress()
    print("Program selesai.")
