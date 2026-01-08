def hitung_penjadwalan(proses, burst_time, algoritma="FCFS"):
    n = len(proses)
    wt = [0] * n  # Waiting Time
    tat = [0] * n # Turnaround Time
    
    # Jika SJF, urutkan berdasarkan Burst Time
    if algoritma == "SJF":
        data = sorted(zip(burst_time, proses))
        burst_time, proses = zip(*data)
        burst_time = list(burst_time)
        proses = list(proses)

    # Menghitung Waiting Time (WT)
    wt[0] = 0
    for i in range(1, n):
        wt[i] = burst_time[i-1] + wt[i-1]

    # Menghitung Turnaround Time (TAT)
    for i in range(n):
        tat[i] = burst_time[i] + wt[i]

    # Menampilkan Hasil
    print(f"\n--- Algoritma {algoritma} ---")
    print("Proses\tBT\tWT\tTAT")
    for i in range(n):
        print(f"{proses[i]}\t{burst_time[i]}\t{wt[i]}\t{tat[i]}")
    
    print(f"Rata-rata Waiting Time: {sum(wt)/n:.2f}")
    print(f"Rata-rata Turnaround Time: {sum(tat)/n:.2f}")

# Dataset / Parameter Uji
nama_proses = ["P1", "P2", "P3", "P4"]
durasi_bt = [8, 4, 2, 1]

# Eksekusi
hitung_penjadwalan(nama_proses, durasi_bt, "FCFS")
hitung_penjadwalan(nama_proses, durasi_bt, "SJF")