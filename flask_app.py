from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/',methods=['POST','GET'])
def mainpage():
    prompt = ""
    if request.form.get('submit'):
        task = request.form.get('task')
        data = request.form.get('data')
        if data == "Deep Learning":
            deep_library = request.form.get("deep_library")
            prompt = f"Write python code using {deep_library} to train a model to do {task}."
        else:
            prompt = f"Write python code using scikit-learn to train a model to do {task}."

    return render_template('mainpage.html', prompt = prompt)

if __name__ == "__main__":
    app.run(debug=True)