from flask import Flask, render_template, request
from numpy.core.records import array
from sklearn import tree
app = Flask('massage')



features = [[21,1,1,0,1,0,0,0,0,1,1,0,1,0,1,0,1,0,1],
            [60,1,1,1,1,1,1,0,1,0,1,1,1,1,1,1,1,1,0],
            [59,1,1,1,1,1,1,0,1,0,1,1,1,1,1,1,1,1,0],
            [45,0,0,1,1,1,0,0,0,0,0,1,0,0,1,1,1,0,0],
            [24,0,0,1,1,1,1,1,1,1,1,0,0,0,1,1,1,0,0],
            [38,0,0,1,1,1,0,0,0,0,0,1,0,1,1,1,1,1,0],
            [32,1,0,1,0,1,1,0,1,0,1,1,1,1,1,1,1,1,0],
            [53,0,0,1,1,1,0,0,0,0,0,1,0,1,1,1,1,1,0],
            [48,0,0,1,1,1,0,0,0,0,0,1,1,1,1,1,1,1,0],
            [47,1,1,1,1,1,1,0,1,0,1,1,1,1,1,1,1,1,0],
            [55,0,0,1,1,1,1,1,1,1,1,0,0,0,1,1,1,0,0],
            [23,0,0,1,1,1,0,0,0,0,0,1,0,0,1,1,1,0,0],
            [39,0,0,1,1,1,0,0,0,0,0,1,1,1,1,1,1,1,0],
            [51,0,0,1,1,1,0,0,0,0,0,1,0,1,1,1,1,1,0],
            [19,1,1,1,1,1,1,0,1,0,1,1,1,1,1,1,1,1,0],
            [22,0,0,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0],
            [62,1,1,0,1,0,0,0,0,1,1,0,1,0,1,0,1,0,1],
            [40,0,0,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0],
            [25,1,1,1,1,0,1,0,1,0,1,1,1,1,0,1,1,1,0],
            [24,0,0,1,0,1,1,1,1,1,1,0,0,0,1,1,1,0,0],
            [31,0,0,1,1,1,0,1,1,0,1,0,0,0,1,1,1,0,0]]

labels=["Reflexology","Medical Massage","Thai Massage","Swedish Massage Theraphy","Hot stone massage",
        "Deep Tissue Massage Therapy","Thai Massage","Deep Tissue Massage Therapy","Medical Massage",
        "Thai Massage","Hot stone massage","Swedish Massage Theraphy","Medical Massage","Deep Tissue Massage Therapy",
        "Thai Massage","Aromatherapy","Reflexology","Aromatherapy","Thai Massage","Hot stone massage","Hot stone massage"]

classifier = tree.DecisionTreeClassifier()
classifier = classifier.fit(features, labels)
result = classifier.predict([[36,0,0,1,1,1,0,1,1,0,1,0,0,0,1,1,1,0,0]])
print(result)


@app.route('/')
def show_predict_stock_form():
    return render_template('index.html')
@app.route('/home')
def predictor():
    return render_template('predictor.html')
@app.route('/results', methods=['POST'])
def results():
    form = request.form
    if request.method == 'POST':
      #write your function that loads the model
       #you can use pickle to load the trained model
       year = request.form['year']
       ye =[[int(s) for s in year.split(',')]]
       print(ye)
       
       predicted_stock_price = classifier.predict(ye)
       return render_template('result.html', year=year,   predicted_price=predicted_stock_price )

app.run("localhost", "9999", debug=True)