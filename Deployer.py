from flask import Flask, request, render_template
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def upload_predict():
    if request.method == 'POST':
        # Code to handle file upload and prediction
        pass
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
