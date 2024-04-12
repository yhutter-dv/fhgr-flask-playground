from flask import Flask, render_template, request, redirect

app = Flask(__name__)

open_todos = []
closed_todos = []

@app.route("/")
def index():
    return render_template("index.html", open_todos=open_todos, closed_todos = closed_todos)

@app.route("/create_todo", methods=["POST"])
def create_todo():
    global open_todos
    new_todo = request.form.get("todo", "").strip()
    if new_todo != "" and new_todo not in open_todos:
        open_todos.append(new_todo)
    return redirect("/") 

@app.route("/complete_todo/<todo>")
def complete_todo(todo):
    global open_todos
    global closed_todos
    if todo in open_todos:
        open_todos.remove(todo)
        closed_todos.append(todo)
    return redirect("/") 

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
