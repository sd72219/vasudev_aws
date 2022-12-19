from flask import Flask, redirect, url_for, render_template, request
import units

app = Flask(__name__)

@app.route('/')
def welcom():
    return render_template('index2.html') 

@app.route('/win/<int:score>')
def win(score):
    return render_template('result.html',result=score)

@app.route('/submit', methods = ['POST', 'GET'])
def submit():
    data = request.form
    if request.method == 'POST':
        print(f"The Linear model Yearly Charges: {data}")

        x1 = float(data['Avg_Session_Length'])
        x2 = float(data['Time_on_App'])
        x3 = float(data['Length_of_Membership'])

        pred1 = units.get_charges(x1,x2,x3)

        return redirect(url_for('win', score=pred1))
    else:
        return "Model Failed"

    
if __name__ == "__main__":
    app.run(debug=True)