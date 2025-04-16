import csv
from bottle import Bottle, redirect, template, static_file, request

app = Bottle()

@app.route('/resources/<filename:path>')
def send_static(filename):
    return static_file(filename, root='./resources/')

@app.route('/')
def index():
    with open("resources/library.csv", "r") as csvfile:
        library = list(csvfile)
    
    content = template('index_template', library=library)

    return content 

@app.route('/video/<name>')
def video(name):  
    content = template('video_template', name=name)

    return content

@app.post('/add') 
def add():
    value = request.forms.get('title')
    
    with open("resources/library.csv", "a") as csvfile:
            csvfile.write('\n' + value)

    redirect("/")

if __name__ == '__main__':
    app.run(host='localhost', port=8080, debug=True, reloader=True)
