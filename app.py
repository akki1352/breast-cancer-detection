from flask import Flask,render_template,request
import pickle
import numpy as np
app = Flask('__name__')
model=pickle.load(open('breast_cancer.pkl','rb'))

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict',methods=["POST"])
def predict():
    feature=[int(x) for x in request.form.values()]
    feature_final=np.array(feature).reshape(-1,1)
    input_data = (13.54,14.36,87.46,566.3,0.09779,0.08129,0.06664,0.04781,0.1885,0.05766,0.2699,0.7886,2.058,23.56,0.008462,0.0146,0.02387,0.01315,0.0198,0.0023,15.11,19.26,99.7,711.2,0.144,0.1773,0.239,0.1288,0.2977,0.07259, 0, 0)
    input_data_as_numpy_array = np.asarray(input_data)
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)
    prediction=model.predict(input_data_reshaped)
    
    print(input_data)
    print(input_data_as_numpy_array)
    print(prediction)

    if (prediction[0] == 0):
        print('The Breast cancer is Malignant')
        return render_template('index.html',prediction_text='The Breast Cancer is Malignant')
    else:
        print('The Breast Cancer is Benign')
        return render_template('index.html',prediction_text='The Breast Cancer is Benign')


@app.route('/predict_test',methods=["POST"])
def login_user():
	# data_points = list()
	# data = []
	# string = 'value'
	# for i in range(1,31):
	# 	data.append(float(request.form['value'+str(i)]))

	# for i in range(30):
	# 	data_points.append(data[i])
		
	# print(data_points)

    input_data = (13.54,14.36,87.46,566.3,0.09779,0.08129,0.06664,0.04781,0.1885,0.05766,0.2699,0.7886,2.058,23.56,0.008462,0.0146,0.02387,0.01315,0.0198,0.0023,15.11,19.26,99.7,711.2,0.144,0.1773,0.239,0.1288,0.2977,0.07259, 0, 0)
    input_data_as_numpy_array = np.asarray(input_data)
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)
    out, acc, t  = model.predict(input_data_reshaped)
    
    if(out==1):
        output = 'Malignant'
    else:
        output = 'Benign'
    acc_x = acc[0][0]
    acc_y = acc[0][1]
    if(acc_x>acc_y):
        acc1 = acc_x
    else:
        acc1=acc_y
        
    return render_template('result.html', output=output, time=t)

if(__name__=='__main__'):
    app.run(debug=True)

