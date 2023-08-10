import os
import shutil
from ultralytics import YOLO
from flask import Flask, render_template, request, redirect, url_for, session


app = Flask(__name__, template_folder="templates", static_folder="static")

UPLOAD_FOLDER = os.path.join("static", "uploads")
PRED_IMG_FOLDER = r"runs\detect\predict"
RESULT_IMG_FOLDER = os.path.join("static", "result")

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
app.config["PRED_IMG_FOLDER"] = PRED_IMG_FOLDER
app.config["RESULT_IMG_FOLDER"] = RESULT_IMG_FOLDER
app.secret_key = "6RD2002"

model = YOLO(r"models\trained_models\best.pt")


@app.route('/detector')
def tumor_detector():

    result = os.path.join('runs\detect\predict', session['filename'])
    image_filename = session['filename']

    if os.path.exists(app.config['RESULT_IMG_FOLDER']):
        shutil.rmtree(app.config['RESULT_IMG_FOLDER']) 
    os.mkdir(app.config['RESULT_IMG_FOLDER'])

    shutil.copy(result, app.config['RESULT_IMG_FOLDER'])

    path = 'result/'+session['filename']

    return render_template('detector.html', path=path) 


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":

        if os.path.exists(r"runs\detect\predict"):
            shutil.rmtree(r"runs\detect\predict")

        if not os.path.exists(app.config["UPLOAD_FOLDER"]):
            os.mkdir(app.config["UPLOAD_FOLDER"])

        _img = request.files["myPhoto"]
        session["filename"] = _img.filename
        _img.save(os.path.join(app.config["UPLOAD_FOLDER"], session["filename"]))

        model.predict(os.path.join(app.config["UPLOAD_FOLDER"], session["filename"]), save = True)

        shutil.rmtree(r"static\uploads")

        return redirect(url_for("tumor_detector"))

    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
