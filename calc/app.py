from flask import Flask, Response
from model.config import Config
from  generator import Generator
import  json
app = Flask(__name__)

@app.route("/")
def index():
    mygen = Generator()
    myconf = Config(hasfraction=True, hasmulanddiv=True, numofexp=10, myrange=5)
    set_expression = mygen.generate(myconf)

    ret = mygen.format_expression(set_expression)
    t = {}
    t['data'] =ret
    # return Response("<h2>welcome flask</h2>")
    return json.dumps(t,ensure_ascii=False)

if __name__ == '__main__':
    app.run(debug=True)