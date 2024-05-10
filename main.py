import subprocess

def jalankan_program(nama_file):
    try:
        subprocess.run(["python", nama_file])
    except FileNotFoundError:
        print(f"File '{nama_file}' tidak ditemukan.")

def main():
    # Daftar nama file program-program yang ingin dijalankan
    daftar_program = ["speed.py", "ping.py", "traceroute.py"]

    # Jalankan setiap program dari daftar
    for nama_program in daftar_program:
        print(f"Menjalankan program '{nama_program}':")
        jalankan_program(nama_program)
        print()

if __name__ == "__main__":
    main()