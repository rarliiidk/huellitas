from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('inicio.html')

if __name__ == "__main__":
    app.run(debug=True)
    
app.static_folder = 'static'  # Establece la carpeta estática

