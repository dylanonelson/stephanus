from app import app

app.run(port=app.config['PORT'], host=app.config['HOST'])
