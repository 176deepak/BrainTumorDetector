import os
import shutil
from flask import Flask, render_template, request, redirect, url_for, session


app = Flask(__name__, template_folder="templates", static_folder="static")

UPLOAD_FOLDER = os.path.join("static", "uploads")
PRED_IMG_FOLDER = r"runs\detect\predict"
RESULT_IMG_FOLDER = os.path.join("static", "result")

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
app.config["PRED_IMG_FOLDER"] = PRED_IMG_FOLDER
app.config["RESULT_IMG_FOLDER"] = RESULT_IMG_FOLDER
app.secret_key = "6RD2002"


# @app.route('/detector')
# def img_vid_detector():

#     result = os.path.join('runs\detect\predict', session['filename'])
#     image_filename = session['filename']

#     if os.path.exists(app.config['PRED_IMG_FOLDER']):
#         shutil.rmtree(app.config['PRED_IMG_FOLDER']) 
#     os.mkdir(app.config['PRED_IMG_FOLDER'])

#     shutil.copy(result, app.config['PRED_IMG_FOLDER'])

#     path = 'pred/'+session['filename']

#     return render_template('img_vid_detector.html', path=path) 


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        if not os.path.exists(app.config["UPLOAD_FOLDER"]):
            os.mkdir(app.config["UPLOAD_FOLDER"])

        _img = request.files["myPhoto"]
        session["filename"] = _img.filename
        _img.save(os.path.join(app.config["UPLOAD_FOLDER"], session["filename"]))

        # if os.path.exists("runs"):
        #     shutil.rmtree(r"runs")

        shutil.rmtree(r"static\uploads")

        # return redirect(url_for("tumor_detector"))

    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
