from flask import Flask,url_for,render_template
app=Flask(__name__, template_folder='template')
@app.route('/')
def home():
    return render_template('predict.html')
if __name__ == "__main__":
    app.run(debug=True)