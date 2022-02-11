from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', num_x=4, num_y=4)

@app.route('/<int:num_x>/<int:num_y>')
def x_y(num_x, num_y):
    print(num_x,num_y)
    return render_template('index.html', num_x=num_x, num_y=num_y)

if __name__=="__main__":
    app.run(debug=True)