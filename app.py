from flask import Flask, render_template, request, send_from_directory
import qrcode
import os

app = Flask(__name__)

# Directory to save QR code images
QR_CODE_DIR = 'static/qr_codes'
os.makedirs(QR_CODE_DIR, exist_ok=True)

# Home route: Shows the form for entering the URL
@app.route('/')
def home():
    return render_template('index.html')

# Route to generate QR code
@app.route('/generate_qr', methods=['POST'])
def generate_qr():
    url = request.form['url']
    if url:
        # Generate QR code for the URL
        qr = qrcode.make(url)
        file_name = f"{url.replace('http://', '').replace('https://', '').replace('/', '_')}.png"
        file_path = os.path.join(QR_CODE_DIR, file_name)
        qr.save(file_path)
        return render_template('show_qr.html', file_name=file_name)

# Route to download the QR code
@app.route('/download/<filename>')
def download_qr(filename):
    return send_from_directory(QR_CODE_DIR, filename)

if __name__ == "__main__":
    app.run(debug=True)
