import werkzeug.utils
from flask import Flask , jsonify,request

app=Flask (__name__)
@app.route('/upload',methods=["POST"])
def upload():
    if(request.method=="POST"):
        imagefile=request.files['images']
        filename=werkzeug.utils.secure_filename(imagefile.filename)
        imagefile. save("/uploadedimages/"+filename)
        return jsonify({
            "message":"Image Uploaded"
        })

if __name__ =="__main__":
    app.run()
