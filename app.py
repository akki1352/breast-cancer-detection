from flask import Flask, render_template, url_for, request, session, redirect, flash, jsonify
import pickle
import numpy as np
import bcrypt
from pymongo import MongoClient
from time import sleep

app = Flask('__name__')
app.secret_key = 'icXjsFoQxp'
app.config['SESSION_TYPE'] = 'filesystem'
app.debug = True

client = MongoClient('localhost', 27017) #host uri
db = client.breast_cancer
model=pickle.load(open('breast_cancer.pkl','rb'))

### Authentication APIS ###

@app.route('/')
@app.route('/signin', methods=['GET', 'POST'])
def signin():
    try:
        if request.method == 'POST':
            users = db.users
            signin_user = users.find_one({'email': request.form['email']})
            if signin_user:
                if bcrypt.hashpw(request.form['pass'].encode('utf-8'), signin_user['password']) == \
                        signin_user['password']:
                    session['email'] = request.form['email']
                    return redirect(url_for('main'))
                else:
                    flash('Email or password is incorrect !')
            else:
                flash('User with this email does not exist !')
            
            # return render_template('login/index.html')

        return render_template('login/index.html')
    except Exception as e:
        print(e)
        return render_template('login/index.html')

@app.route("/signup", methods=['POST', 'GET'])
def signup():
    print(db.list_collection_names())
    if request.method == 'POST':
        users = db.users
        print(users)
        signup_user = users.find_one({'email': request.form['email']})

        if signup_user:
            flash(request.form['email'] + ' email is already exist')
            return redirect(url_for('signup'))

        hashed = bcrypt.hashpw(request.form['pass'].encode('utf-8'), bcrypt.gensalt(14))
        db.users.insert_one({
            'password': hashed, 
            'email': request.form['email'],
            'name': request.form['name'],
            'contact': request.form['contact']
            })
        return redirect(url_for('signin'))

    return render_template('signup/index.html')

### Authentication APIS ENDS HERE ###

@app.route("/index")
def main():
    return render_template('home.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/getArray', methods=['GET', 'POST'])
def getArray():
    feature_columns = [
        "radius_mean",
        "texture_mean",
        "perimeter_mean",
        "area_mean",
        "smoothness_mean",
        "compactness_mean",
        "concavity_mean",
        "concave points_mean",
        "symmetry_mean",
        "fractal_dimension_mean",
        "radius_se",
        "texture_se",
        "perimeter_se",
        "area_se",
        "smoothness_se",
        "compactness_se",
        "concavity_se",
        "concave points_se",
        "symmetry_se",
        "fractal_dimension_se",
        "radius_worst",
        "texture_worst",
        "perimeter_worst",
        "area_worst",
        "smoothness_worst",
        "compactness_worst",
        "concavity_worst",
        "concave points_worst",
        "symmetry_worst",
        "fractal_dimension_worst",
    ]

    print(request.get_json())
    data = request.get_json()
    data_arr = data['data']
    res = {}
    for i in range(0,30):
        res[feature_columns[i]] = data_arr[i]
    return jsonify(
        res
    )

@app.route('/predict',methods=["GET", "POST"])
def predict():

    if request.method == 'POST':

        feature_columns = ["radius_mean", "texture_mean", "perimeter_mean", "area_mean", "smoothness_mean", "compactness_mean", 
            "concavity_mean", "concave_points_mean", "symmetry_mean", "fractal_dimension_mean", "radius_se", "texture_se", 
            "perimeter_se", "area_se", "smoothness_se", "compactness_se", "concavity_se", "concave_points_se", "symmetry_se", 
            "fractal_dimension_se", "radius_worst", "texture_worst", "perimeter_worst", "area_worst", "smoothness_worst", 
            "compactness_worst", "concavity_worst", "concave_points_worst", "symmetry_worst", "fractal_dimension_worst", 
        ]
        feature = []
        for column in feature_columns:
            feature.append(float(request.form.get(column)))
        # return jsonify(data="1")

        feature_tuple = tuple(feature)
        
        # input_data = (13.54, 14.36, 87.46, 566.3, 0.09779, 0.08129, 0.06664, 0.04781, 0.1885, 0.05766, 0.2699, 0.7886, 2.058, 23.56, 0.008462, 0.0146, 0.02387, 0.01315, 0.0198, 0.0023, 15.11, 19.26, 99.7, 711.2, 0.144, 0.1773, 0.239, 0.1288, 0.2977, 0.07259)
        input_data_as_numpy_array = np.asarray(feature_tuple)
        input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)
        prediction=model.predict(input_data_reshaped)

        print(prediction)
        sleep(5)
        if (prediction[0] == "0"):
            print('The Breast cancer is Malignant')
            return render_template('result/index.html',result='The Breast Cancer is Malignant')
            return jsonify({
                "result": 'The Breast Cancer is Malignant'
            }) 
        else:
            print('The Breast Cancer is Benign')
            return render_template('result/index.html',result='The Breast Cancer is Benign')
            # return render_template('index.html',prediction_text='The Breast Cancer is Benign')
            return jsonify({
                "result": 'The Breast Cancer is Benign'
            }) 
    
    return render_template('predict-cancer/index.html')


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

    data = [
        "diagnosis",
        "radius_mean",
        "texture_mean",
        "perimeter_mean",
        "area_mean",
        "smoothness_mean",
        "compactness_mean",
        "concavity_mean",
        "concave points_mean",
        "symmetry_mean",
        "fractal_dimension_mean",
        "radius_se",
        "texture_se",
        "perimeter_se",
        "area_se",
        "smoothness_se",
        "compactness_se",
        "concavity_se",
        "concave points_se",
        "symmetry_se",
        "fractal_dimension_se",
        "radius_worst",
        "texture_worst",
        "perimeter_worst",
        "area_worst",
        "smoothness_worst",
        "compactness_worst",
        "concavity_worst",
        "concave points_worst",
        "symmetry_worst",
        "fractal_dimension_worst",
    ]

    print("request", request)

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

@app.route("/model-info")
def model_info():
    return render_template('model-information/index.html')

@app.route("/contact")
def contact():
    return render_template('contact-form-04/index.html')

if(__name__=='__main__'):
    app.run(debug=True, port=8000)

