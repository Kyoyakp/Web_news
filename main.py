from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/news',methods=['GET','POST'])
def news():
    if request.method == 'POST':
        Headlines = request.form.get('Headlines')
        Description = request.form.get('Description')
        Author = request.form.get('Author Name')
        Category = request.form.get('News Category')
        return render_template('news.html',Category=Category,Author=Author,Headlines=Headlines,Description=Description)
    return render_template('news.html')

@app.route('/contacts')
def contacts():
    return render_template('contacts.html')

@app.route('/contribute')
def add_news():
    return render_template('add_news.html')

if __name__ == "__main__":
    app.run()
