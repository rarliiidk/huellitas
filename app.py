from routes import app 

if __name__ == '__main__':
    # Ejecutamos la aplicación en modo debug
    app.run(debug=True)
    
app.static_folder = 'static'
