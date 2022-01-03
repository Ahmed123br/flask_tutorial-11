from flask import Flask,render_template,request,flash

app = Flask(__name__)

@app.route("/")
def home():
    home = "this is my home page"
    return render_template('index.html', home1= home)
@app.route("/textanalyzer",methods=['GET','POST'])
def textAnalyze():
    text = request.args.get('text')
    wordcount = request.args.get('wordcount',default="off")
    removepunch =  request.args.get('removepunc',default="off")
    uppercase =  request.args.get('upper',default="off")
    spaceremove =  request.args.get('spaceremov',default="off")
    newlineremove =  request.args.get('newlineremov',default="off")

    if wordcount == "on":
        text = text.split()
        analyzed = len(text)
        params = {'task':'Word Counting','analyzed_text':analyzed}
        return render_template('analyze.html',params=params)

    elif  removepunch== "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

        for char in text:
            if char in punctuations:
                text = text.replace(char,"")
        analyzed = text
        params = {'task':'Remove punctuations','analyzed_text':analyzed}
        return render_template('analyze.html',params=params)

    elif uppercase == "on":
        analyzed = "".join(char.upper() for char in text)
        params = {'task':'Uppercase','analyzed_text':analyzed}
        return render_template('analyze.html',params=params)

    elif spaceremove == "on":
        analyzed = "".join(
            char
            for i, char in enumerate(text)
            if text[i] != " " or text[i + 1] != " "
        )

        params = {'task':'Unwanted Space Remove','analyzed_text':analyzed}
        return render_template('analyze.html',params=params)

    elif newlineremove == "on":
        analyzed = "".join(char for char in text if char != "\n")
        params = {'task':'Newline Remove','analyzed_text':analyzed}
        return render_template('analyze.html',params=params)

    else:
        flash("Error!! Please Select one item")
        return render_template("msg.html")
  
  



if __name__ == "__main__":
    app.secret_key = 'super secret key'
    app.config['SESSION_TYPE'] = 'filesystem'
    app.run(debug=True)