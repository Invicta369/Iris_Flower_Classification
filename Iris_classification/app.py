# pip install flask

from flask import Flask,render_template,request
import pickle

# loading the label encoder 
#le=pickle.load(open('label_encoder.pkl','rb'))

# loading my mlr model
model= pickle.load(open('model.pkl', 'rb'))


# Flask is used for creating your application
# render template is use for rendering the html page


app= Flask(__name__)  # your application


@app.route('/')  # default route 
def home():
    return render_template('iris.html') # rendering if your home page.

@app.route('/pred',methods=['POST']) # prediction route
def predict1():
    '''
    For rendering results on HTML 
    '''
    
    sl = request.form["sepal_len"]
    sw = request.form["sepal_wd"]
    pl = request.form["petal_len"]
    pw = request.form["petal_wd"]
    t =  [[float(sl),float(sw),float(pl),float(pw)]] 
    output =model.predict(t)
    print(output)
    
    return render_template("iris.html", result = "The predicted species is "+str(output[0]))
        
    
    
    
# running your application
if __name__ == "__main__":
    app.run()

#http://localhost:5000/ or localhost:5000