import pythonping
import statistics
import time
import socket
import pandas as pd
from datetime import datetime
from openpyxl import load_workbook

def get_local_ip():
    try:
        # Mendapatkan alamat IP lokal
        local_ip = socket.gethostbyname(socket.gethostname())
        return local_ip
    except:
        return "Unknown"

def ping_and_save():
    source_host = get_local_ip()  # Mendapatkan alamat IP lokal
    all_results = []
    print("Pengukuran sedang berjalan")
    start_time = time.time()  # Waktu mulai pengukuran

    while (time.time() - start_time) < 30:  # waktu program berjalan
        target_host = 'google.com'  # Ganti dengan host yang ingin Anda uji ping-nya
        ping_result = pythonping.ping(target_host, count=10)  # Melakukan ping sebanyak 10 kali

        packet_loss = ping_result.packet_loss
        latency_values = [response.time_elapsed * 1000 for response in ping_result]

        latency_max = max(latency_values)
        latency_max = round(latency_max, 3)
        latency_min = min(latency_values)
        latency_min = round(latency_min, 3)
        latency_avg = statistics.mean(latency_values)
        latency_avg = round(latency_avg, 3)

        jitter_values = [abs(latency - latency_avg) * 1000 for latency in latency_values]
        jitter_avg = statistics.mean(jitter_values)
        jitter_avg = round(jitter_avg, 3)

        # Menyimpan hasil pengukuran dalam list
        all_results.append({
            "Source Host": source_host,
            "Target Host": target_host,
            "Packet Loss (%)": packet_loss,
            "Maximum Latency (ms)": latency_max,
            "Minimum Latency (ms)": latency_min,
            "Average Latency (ms)": latency_avg,
            "Average Jitter (ms)": jitter_avg,
            "Timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Format tanggal dan waktu yang lebih rapi
        })

        time.sleep(1)  # Menunggu selama 1 detik sebelum melakukan pengukuran berikutnya

    # Hitung rata-rata dari seluruh rata-rata latency
    avg_latency_overall = statistics.mean([result["Average Latency (ms)"] for result in all_results])

    # Tambahkan rata-rata seluruh avg latency ke dalam list
    for result in all_results:
        result["Avg Latency Overall"] = avg_latency_overall

    # Simpan hasil ke Excel
    save_to_excel(all_results)

def save_to_excel(all_results):
    # Membuat DataFrame dari hasil pengukuran
    df = pd.DataFrame(all_results)

    # Mendapatkan tanggal dan waktu saat ini
    now = datetime.now()
    timestamp_str = now.strftime("%Y%m%d_%H%M%S")

    # Menyimpan DataFrame ke dalam file Excel dengan nama yang mencerminkan tanggal dan waktu pengukuran
    file_name = f"ping_results_{timestamp_str}.xlsx"

    # Menyimpan DataFrame ke dalam file Excel dengan format yang lebih rapi
    df.to_excel(file_name, index=False)

    # Mengatur ukuran sel sesuai dengan isi yang didapat
    wb = load_workbook(file_name)
    ws = wb.active
    dims = {}
    for row in ws.rows:
        for cell in row:
            if cell.value:
                dims[cell.column_letter] = max((dims.get(cell.column_letter, 0), len(str(cell.value)) * 1.2))
    for col, value in dims.items():
        ws.column_dimensions[col].width = value
    wb.save(file_name)

    print(f"Pengukuran selesai. Hasil pengukuran ping telah disimpan dalam file: {file_name}")

# Mulai penjadwalan tugas
ping_and_save()
