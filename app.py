from flask import Flask,render_template,request,url_for
import pickle
import numpy as np
mlmodel=pickle.load(open('lg.pkl','rb'))
app=Flask(__name__)
@app.route('/')
def fun():
    return render_template('predict.html')
@app.route('/predict', methods=['POST','GET'])
def predict():
  if request.method == 'POST':
    data1=request.form['b']
    data2=request.form['c']
    data3=request.form['d']
    data4=request.form['e']
    data5=request.form['f']
    data6=request.form['g']
    data7=request.form['h']
    data8=request.form['i']
    data9=request.form['j']
    data10=request.form['k']
    data11=request.form['l']
    data12=request.form['m']
    data13=request.form['n']
    data14=request.form['o']
    data15=request.form['p']
    data16=request.form['q']
    data17=request.form['r']
    data18=request.form['s']
    arr=np.array([[data1,data2,data3,data4,data5,data6,data7,data8,data9,data10,data11,data12,data13,data14,data15,data16,data17,data18]])
    predict=mlmodel.predict(arr)
    return  render_template(output='predicted life expectancy is:{}'.format(predict))
    
    
if __name__  == "__main__":
    app.run(debug=True)