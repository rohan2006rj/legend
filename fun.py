from flask import Flask,render_template,request

app=Flask(__name__)
@app.route("/",methods=["GET","POST"])
def hello():
    img=""
    if request.method=="POST":
        if request.form["user"]=="rohan" and request.form["doom"]=="12345":
            return render_template ("ro.html",name=request.form["user"])
        # return render_template("new.html")
        else:
            img="image"
    return render_template("new.html",fight=img)
    

if __name__=="__main__":
    app.run(debug=True)