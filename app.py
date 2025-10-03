from flask import Flask
app = Flask(app)

@app.route("/")
def home():
  return "Hello from Docker + Github!"

if app == "__main__":
  app.run(host"0.0.0.0", port=5000)
