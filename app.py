from flask import Flask, render_template, redirect, url_for, send_file

app = Flask(__name__)
app.secret_key = 'your_secret_key'

@app.route('/')
def home():
    # Render the home page
    return render_template('index.html')

@app.route('/play')
def play():
    # Redirect to an external URL for the game
    return redirect("https://mario-website-nu.vercel.app/") # Replace with the actual game URL

@app.route('/download')
def download():
    # Serve the game executable file for download
    file_path = 'game/main.exe'  
    return send_file(file_path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
