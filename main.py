from flask import Flask, request,render_template

app = Flask(__name__)


@app.route('/url_name/', methods=['GET'])
def print_hello():
    name = request.args.get('name')
    message = request.args.get('message')
    if name and name != '' and message and message != '':
        return f"Hello {name} <br> " \
           f"{message} <br>"
    return 'введите верный урл [ url_name/?name=Rekruto&message=Давай дружить! ] '


if __name__ == '__main__':
    app.run(debug=False, port=8000)
