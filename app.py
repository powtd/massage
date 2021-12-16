import numpy as np
from flask import Flask, render_template, request
app = Flask('massage')

def jaccard_binary(x,y):
    
    intersection = np.logical_and(x, y)
    union = np.logical_or(x, y)
    similarity = intersection.sum() / float(union.sum())
    return similarity

Reflexology = [1,1,0,1,0,0,0,0,1,1,0,1,0,1,0,1,0,1]
MedicalMassage = [1,1,1,1,1,1,0,1,0,1,1,1,1,1,1,1,1,0]
ThaiMassage = [1,1,1,1,1,1,0,1,0,1,1,1,1,1,1,1,1,0]
SwedishMassageTheraphy = [0,0,1,1,1,0,0,0,0,0,1,0,0,1,1,1,0,0]
Hotstonemassage = [0,0,1,1,1,1,1,1,1,1,0,0,0,1,1,1,0,0]
DeepTissueMassageTherapy = [0,0,1,1,1,0,0,0,0,0,1,0,1,1,1,1,1,0]
Aromatherapy = [0,0,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0]



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
      
       year = request.form['year']
       ye =[[int(s) for s in year.split(',')]]
       print(ye)
       
       sim_Reflexology = jaccard_binary(Reflexology,ye)
       sim_MedicalMassage = jaccard_binary(MedicalMassage,ye)
       sim_ThaiMassage = jaccard_binary(ThaiMassage,ye)
       sim_SwedishMassageTheraphy = jaccard_binary(SwedishMassageTheraphy,ye)
       sim_Hotstonemassage = jaccard_binary(Hotstonemassage,ye)
       sim_DeepTissueMassageTherapy = jaccard_binary(DeepTissueMassageTherapy,ye)
       sim_Aromatherapy = jaccard_binary(Aromatherapy,ye)

       xx = [sim_Reflexology,sim_MedicalMassage,sim_ThaiMassage,sim_SwedishMassageTheraphy,sim_Hotstonemassage,sim_DeepTissueMassageTherapy,sim_Aromatherapy]
       xx.sort()
       p = xx[-1]

       if(p == sim_Reflexology):
        pp = "Reflexology"

       if(p == sim_MedicalMassage):
        pp = "Medical Massage"

       if(p == sim_ThaiMassage):
        pp = "Thai Massage"

       if(p == sim_SwedishMassageTheraphy):
        pp = "Swedish Massage Theraphy"

       if(p == sim_Hotstonemassage):
        pp = "Hotstone massage"

       if(p == sim_DeepTissueMassageTherapy):
        pp = "Deep TissueMassage Therapy"

       if(p == sim_Aromatherapy):
        pp = "Aromatherapy"
       


       return render_template('result.html', year=year,   predicted_price=pp)

app.run("localhost", "9999", debug=True)