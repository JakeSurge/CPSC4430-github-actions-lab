from flask import Flask, request

app = Flask(__name__)

# Home route for linking pages
@app.route("/")
def home():
    return """
    <h1>Best Calculator Site Ever</h1>
    <div>
        <a href="/add">Add</a>
        <a href="/subtract">Subtract</a>
        <a href="/multiply">Multiply</a>
    </div>
    """

# Get request for adding
@app.route("/add")
def add():
    num1 = int(request.args.get("num1"))
    num2 = int(request.args.get("num2"))

    return f"<p>{num1 + num2}</p>"

# Get request for subtracting
@app.route("/subtract")
def subtract():
    num1 = int(request.args.get("num1"))
    num2 = int(request.args.get("num2"))

    return f"<p>{num1 - num2}</p>"

# Get request for multiplying
@app.route("/multiply")
def multiply():
    num1 = int(request.args.get("num1"))
    num2 = int(request.args.get("num2"))

    return f"<p>{num1 * num2}</p>"

if __name__ == "__main__":
    app.run()