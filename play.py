from flask import Flask, render_template
app = Flask(__name__)                     
    
@app.route('/play/')                           
def playground():
    return render_template('playGround3.html')
    # return render_template('playGround.html')  

@app.route('/play/<int:num>')
def playgroundNum(num):
    # comma / some word for html to use / equals to / "value"
    # ex. "render_template, someWord = "hello", times = 5, schedule = gameList"
    return render_template('playGround3.html', pgNum = num)
    # return render_template('playGround2.html', pgNum = num)

@app.route('/play/<int:num>/<color>')
def playgroundColor(num, color):
    return render_template('playGround3.html', pgNum = num, pgColor = color)
# @app.route('/play/<int:numboxes>/<color>')
# def pg_boxes(numboxes, color):
#     return render_template('playGround.html', pgBoxes=numboxes, pgBoxesColor=color)

# @app.route('/play/<int:numboxes1>/<color>')
# def pg_boxes_color(color):
#     return render_template('pgBoxColor.html', pgBoxesColor=color)




if __name__=="__main__":
    app.run(debug=True)