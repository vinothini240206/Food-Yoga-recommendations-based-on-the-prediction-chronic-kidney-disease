import pickle
import numpy as np
import pandas as pd
loaded_class = pickle. load(open('randomclass_chronic', 'rb'))
loaded_reg = pickle. load(open('randomreg_chronic', 'rb'))

from flask import Flask, request, redirect, render_template
app = Flask(__name__)
@app.route("/",methods=['GET'])
def index():
    return render_template('index.html')

@app.route("/val",methods=['POST'])
def val():
    test=[]
    if request.method == 'POST':
        test.append(request.form.get("age"))
        test.append(request.form.get("bp"))
        test.append(request.form.get("sg"))
        test.append(request.form.get("al"))
        test.append(request.form.get("su"))
        test.append(request.form.get("rbc"))
        test.append(request.form.get("pc"))
        test.append(request.form.get("pcc"))
        test.append(request.form.get("ba"))
        test.append(request.form.get("bgr"))
        test.append(request.form.get("bu"))
        test.append(request.form.get("sc"))
        test.append(request.form.get("sod"))
        test.append(request.form.get("pot"))
        test.append(request.form.get("hemo"))
        test.append(request.form.get("pcv"))
        test.append(request.form.get("wc"))
        test.append(request.form.get("rc"))
        test.append(request.form.get("htn"))
        test.append(request.form.get("dm"))
        test.append(request.form.get("cad"))
        test.append(request.form.get("appet"))
        test.append(request.form.get("pe"))
        test.append(request.form.get("ane"))
    print(test)
    # test = ['5', '50', '1', '1', '1', '1', '1', '1', '1', '75', '15', '1', '100', '1', '15', '1', '6000', '0', '1', '1', '1', '1', '1', '1']
    test_df=pd.DataFrame(test)
    test_df=np.array(test_df).reshape(1, -1)
    ans1=loaded_class.predict(test_df)
    ans2=loaded_reg.predict(test_df)
    print(ans1)
    print(ans2)
    prediction = (ans2*100)
   
    return render_template('result.html',prediction=prediction)
    
if __name__ == "__main__":
    app.debug=True
    app.run(debug=False)