from flask import Flask,render_template,request, jsonify
import pickle
import numpy as np
app = Flask('__name__')
model=pickle.load(open('breast_cancer.pkl','rb'))

@app.route('/')
def home():
    return render_template('home.html')

def create_json():
    a = [
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
        "label",
    ]

    input_data = [13.54,14.36,87.46,566.3,0.09779,0.08129,0.06664,0.04781,0.1885,0.05766,0.2699,0.7886,2.058,23.56,0.008462,0.0146,0.02387,0.01315,0.0198,0.0023,15.11,19.26,99.7,711.2,0.144,0.1773,0.239,0.1288,0.2977,0.07259, 0]
    print(len(input_data))
    print(len(a))
    json_obj = {}
    for i in range(0, 31):
        json_obj[a[i]] = str(input_data[i])
    return json_obj

@app.route('/predict',methods=["POST"])
def predict():

    # Sample Request Payload
    # {
    #     "radius_mean": "13.54",
    #     "texture_mean": "14.36",
    #     "perimeter_mean": "87.46",
    #     "area_mean": "566.3",
    #     "smoothness_mean": "0.09779",
    #     "compactness_mean": "0.08129",
    #     "concavity_mean": "0.06664",
    #     "concave points_mean": "0.04781",
    #     "symmetry_mean": "0.1885",
    #     "fractal_dimension_mean": "0.05766",
    #     "radius_se": "0.2699",
    #     "texture_se": "0.7886",
    #     "perimeter_se": "2.058",
    #     "area_se": "23.56",
    #     "smoothness_se": "0.008462",
    #     "compactness_se": "0.0146",
    #     "concavity_se": "0.02387",
    #     "concave points_se": "0.01315",
    #     "symmetry_se": "0.0198",
    #     "fractal_dimension_se": "0.0023",
    #     "radius_worst": "15.11",
    #     "texture_worst": "19.26",
    #     "perimeter_worst": "99.7",
    #     "area_worst": "711.2",
    #     "smoothness_worst": "0.144",
    #     "compactness_worst": "0.1773",
    #     "concavity_worst": "0.239",
    #     "concave points_worst": "0.1288",
    #     "symmetry_worst": "0.2977",
    #     "fractal_dimension_worst": "0.07259",
    #     "label": "0"
    # }

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
        "label",
    ]

    print("request", request.get_json())
    request_payload_json = request.get_json()
    feature = []
    for column in feature_columns:
        if column == "label":
            feature.append(int(request_payload_json[column]))    
        feature.append(float(request_payload_json[column]))
    
    feature_tuple = tuple(feature)
    print(feature_tuple)
    # input_data = (13.54,14.36,87.46,566.3,0.09779,0.08129,0.06664,0.04781,0.1885,0.05766,0.2699,0.7886,2.058,23.56,0.008462,0.0146,0.02387,0.01315,0.0198,0.0023,15.11,19.26,99.7,711.2,0.144,0.1773,0.239,0.1288,0.2977,0.07259, 0, 0)
    input_data_as_numpy_array = np.asarray(feature_tuple)
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)
    prediction=model.predict(input_data_reshaped)

    if (prediction[0] == 0):
        print('The Breast cancer is Malignant')
        # return render_template('index.html',prediction_text='The Breast Cancer is Malignant')
        return jsonify({
            "result": 'The Breast Cancer is Malignant'
        }) 
    else:
        print('The Breast Cancer is Benign')
        # return render_template('index.html',prediction_text='The Breast Cancer is Benign')
        return jsonify({
            "result": 'The Breast Cancer is Benign'
        }) 


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

if(__name__=='__main__'):
    app.run(debug=True)

