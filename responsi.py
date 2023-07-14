from flask import Flask, render_template
import pymysql

app = Flask(__name__)

# Fungsi untuk membuat koneksi ke database
def create_connection():
    conn = pymysql.connect(
        host='localhost',
        user='root',
        password='',
        database='dbresponsi.db'
    )
    return conn

# Fungsi untuk mengambil data dari tabel
def get_data():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT nama, nomor_urut FROM mahasiswa")
    data = cursor.fetchall()
    conn.close()
    return data

@app.route('/')
def home():
    data = get_data()
    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run()