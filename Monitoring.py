import serial
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import csv
import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Konfigurasi koneksi serial
port = 'COM10'
baud_rate = 9600
ser = serial.Serial(port, baud_rate)

# Inisialisasi data yang akan diplot
waktu = []
suhu1 = []
suhu2 = []
suhu3 = []
suhu4 = []
time = []
recording = False

# Fungsi untuk memproses data dari serial
def proses_data():
    if recording:
        data = ser.readline().decode('utf-8').strip()
        if data:
            hasil = data.split(',')
            suhu1.append(float(hasil[0]))
            suhu2.append(float(hasil[1]))
            suhu3.append(float(hasil[2]))
            suhu4.append(float(hasil[3]))
            time.append(len(suhu1))

            # Update nilai sensor di label GUI
            label_suhu1_value.config(text=f'{suhu1[-1]:.2f}')
            label_suhu2_value.config(text=f'{suhu2[-1]:.2f}')
            label_suhu3_value.config(text=f'{suhu3[-1]:.2f}')
            label_suhu4_value.config(text=f'{suhu4[-1]:.2f}')

# Fungsi untuk memperbarui plot
def update_plot(frame):
    if recording:
        proses_data()
        plt.cla()
        plt.plot(time, suhu1, label='Sensor 1')
        plt.plot(time, suhu2, label='Sensor 2')
        plt.plot(time, suhu3, label='Sensor 3')
        plt.plot(time, suhu4, label='Sensor 4')
        plt.xlabel('Waktu (s)')
        plt.ylabel('Suhu (*C)')
        plt.title('Grafik Suhu dari Sensor MAX6675')
        plt.legend()

# Fungsi untuk menyimpan data ke dalam file CSV saat jendela ditutup
def simpan_data():
    entry_nama_file.config(state='disabled')
    button_simpan.config(state='disabled')
    global nama_file
    nama_file = entry_nama_file.get()

def simpan_gambar():
    filee = str(nama_file + '.png')
    fig.savefig(filee)
    print(f"Gambar disimpan sebagai {filee}")

def start_recording():
    global recording
    recording = True

def stop_recording():
    global recording
    recording = False

def on_close():
    ser.close()  # Menutup koneksi serial saat aplikasi ditutup
    plt.close()  # Menutup plot secara eksplisit

    # Menyimpan data ke dalam file CSV
    filee = str(nama_file + '.csv')
    with open(filee, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Time', 'Sensor 1', 'Sensor 2', 'Sensor 3', 'Sensor 4', 'Sensor 5'])
        for i in range(len(time)):
            writer.writerow([time[i], suhu1[i], suhu2[i], suhu3[i], suhu4[i]])
    root.quit()

# Inisialisasi GUI
root = tk.Tk()
root.title("Monitoring Suhu Sensor")

# Variabel untuk nama file
nama_file = tk.StringVar()

# Layout untuk input nama file
frame_input = ttk.Frame(root)
frame_input.grid(row=0, column=0, padx=10, pady=10, sticky="ew")
label_nama_file = ttk.Label(frame_input, text="Simpan sebagai (nama file):")
label_nama_file.grid(row=0, column=0, sticky="w")
entry_nama_file = ttk.Entry(frame_input, textvariable=nama_file)
entry_nama_file.grid(row=0, column=1, sticky="ew")
frame_input.columnconfigure(1, weight=1)
button_simpan = ttk.Button(frame_input, text="Simpan", command=simpan_data)
button_simpan.grid(row=0, column=2, padx=5)

# Layout untuk menampilkan nilai masing-masing sensor dalam satu baris
frame_data = ttk.Frame(root)
frame_data.grid(row=1, column=0, padx=10, pady=10, sticky="ew")
labels = ["Sensor 1", "Sensor 2", "Sensor 3", "Sensor 4", "Sensor 5"]
label_suhu1_value = ttk.Label(frame_data, text="0.00")
label_suhu2_value = ttk.Label(frame_data, text="0.00")
label_suhu3_value = ttk.Label(frame_data, text="0.00")
label_suhu4_value = ttk.Label(frame_data, text="0.00")
label_values = [label_suhu1_value, label_suhu2_value, label_suhu3_value, label_suhu4_value]

for i, (label, value_label) in enumerate(zip(labels, label_values)):
    ttk.Label(frame_data, text=label).grid(row=0, column=i * 2, sticky="w", padx=5)
    value_label.grid(row=0, column=i * 2 + 1, sticky="e", padx=5)

# Layout untuk tombol kontrol
frame_controls = ttk.Frame(root)
frame_controls.grid(row=2, column=0, padx=10, pady=10, sticky="ew")
button_start = ttk.Button(frame_controls, text="Start", command=start_recording)
button_start.grid(row=0, column=0, padx=5)
button_stop = ttk.Button(frame_controls, text="Stop", command=stop_recording)
button_stop.grid(row=0, column=1, padx=5)
button_save_img = ttk.Button(frame_controls, text="Simpan Gambar", command=simpan_gambar)
button_save_img.grid(row=0, column=2, padx=5)

# Layout untuk plotting
frame_plot = ttk.Frame(root)
frame_plot.grid(row=3, column=0, padx=10, pady=10, sticky="nsew")
root.rowconfigure(3, weight=1)
root.columnconfigure(0, weight=1)

# Inisialisasi plot
fig, ax = plt.subplots()
canvas = FigureCanvasTkAgg(fig, master=frame_plot)
canvas.draw()
canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

# Animasi plot dengan interval 100 ms (untuk memastikan plot real-time)
ani = FuncAnimation(fig, update_plot, interval=100)

# Menutup aplikasi dengan menyimpan data
root.protocol("WM_DELETE_WINDOW", on_close)

# Tampilkan GUI
root.mainloop()
