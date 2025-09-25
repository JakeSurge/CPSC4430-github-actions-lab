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
        <a href="/divide">Divide</a>
    </div>
    """

# Get request for adding
@app.route("/add")
def add():
    page = """
    <h1>Add</h1>
    <form action=/add method=get>
        <input name=a />
        <input name=b />
        <input type=submit />
    </form>
    <a href="/">Home</a>
    """

    try:
        a = int(request.args["a"])
        b = int(request.args["b"])
        page += f"<p>The sum is {a+b}</p>"
    except:
        pass

    return page

# Get request for subtracting
@app.route("/subtract")
def subtract():
    page = """
    <h1>Subtract</h1>
    <form action=/subtract method=get>
        <input name=a />
        <input name=b />
        <input type=submit />
    </form>
    <a href="/">Home</a>
    """

    try:
        a = int(request.args["a"])
        b = int(request.args["b"])
        page += f"<p>The difference is {a-b}</p>"
    except:
        pass

    return page

# Get request for multiplying
@app.route("/multiply")
def multiply():
    page = """
    <h1>Multiply</h1>
    <form action=/multiply method=get>
        <input name=a />
        <input name=b />
        <input type=submit />
    </form>
    <a href="/">Home</a>
    """

    try:
        a = int(request.args["a"])
        b = int(request.args["b"])
        page += f"<p>The product is {a*b}</p>"
    except:
        pass

    return page


# Get request for dividing
@app.route("/divide")
def divide():
    page = """
    <h1>Divide</h1>
    <form action=/divide method=get>
        <input name=a />
        <input name=b />
        <input type=submit />
    </form>
    <a href="/">Home</a>
    """

    try:
        a = int(request.args["a"])
        b = int(request.args["b"])
        page += f"<p>The quotient is {a/b}</p>"
    except:
        pass

    return page


if __name__ == "__main__":
    app.run()