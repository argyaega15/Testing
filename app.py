import subprocess
from flask import Flask, render_template, jsonify, redirect, url_for, send_file

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/test')
def test():
    return render_template('test.html')

@app.route('/speed')
def jalankan_pengukuran_speed():
    try:
        # Menjalankan speed.py menggunakan subprocess
        subprocess.run(['python', 'speed.py'], check=True)
        # Arahkan ke halaman speed.html setelah pengukuran speed selesai
        return redirect(url_for('hasil_pengukuran_speed'))
    except subprocess.CalledProcessError:
        return jsonify({'status': 'error', 'message': 'Gagal menjalankan pengukuran speed'})

@app.route('/hasil_pengukuran_speed')
def hasil_pengukuran_speed():
    return render_template('speed.html')

@app.route('/ping')
def pengujian_ping():
    try:
        subprocess.run(['python', 'ping.py'], check=True)
        return redirect(url_for('hasil_pengukuran_ping'))
    except subprocess.CalledProcessError:
        return jsonify({'status': 'error', 'message': 'Gagal menjalankan pengukuran ping'})

@app.route('/hasil_pengukuran_ping')
def hasil_pengukuran_ping():
    return render_template('ping.html')

@app.route('/traceroute')
def pengujian_traceroute():
    try:
        subprocess.run(['python', 'traceroute.py'], check=True)
        return redirect(url_for('hasil_pengukuran_traceroute'))
    except subprocess.CalledProcessError:
        return jsonify({'status': 'error', 'message':'Gagal menjalankan pengukuran traceroute'})

@app.route('/hasil_pengukuran_traceroute')
def hasil_pengukuran_traceroute():
    return render_template('traceroute.html')

@app.route('/test_all')
def pengujian_all():
    try:
        subprocess.run(['python', 'main.py'], check=True)
        return redirect(url_for('hasil_pengukuran_all'))
    except subprocess.CalledProcessError:
        return jsonify({'status': 'error', 'message':'Gagal Mengukur'})
    
@app.route('/hasil_pengukuran_all')
def hasil_pengukuran_all():
    return render_template('all.html')


if __name__ == '__main__':
    app.run(debug=True)
