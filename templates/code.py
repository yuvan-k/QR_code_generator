import qrcode
from flask import Flask, request, send_file
from io import BytesIO

# Create a Flask app instance
app = Flask(__name__)

# Define a route to generate a QR code
@app.route('/', methods=['GET', 'POST'])
def generate_qr():
    if request.method == 'POST':
        # Get the URL or text from the form
        data = request.form.get('data')
        
        if data:
            # Generate QR code from the given data
            qr = qrcode.make(data)
            
            # Save the QR code into a BytesIO object (in memory)
            img_io = BytesIO()
            qr.save(img_io, 'PNG')
            img_io.seek(0)
            
            # Return the image file to the user to download
            return send_file(img_io, mimetype='image/png', as_attachment=True, download_name='qrcode.png')
        else:
            return "Please provide some data to generate a QR code.", 400
    
    # Display the form to submit a URL or text
    return '''
        <form method="POST">
            <label for="data">Enter URL or Text for QR Code:</label>
            <input type="text" name="data" required>
            <button type="submit">Generate QR Code</button>
        </form>
    '''

# Run the app locally
if __name__ == '__main__':
    app.run(debug=True)
