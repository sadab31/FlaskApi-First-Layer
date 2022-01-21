from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

buttonInfo = {}

class Fitness(Resource):
    def get(self, btn_id):
        if btn_id=="all":
            return buttonInfo
        return {btn_id: buttonInfo[btn_id]}

    def post(self, btn_id):
        buttonInfo[btn_id] = request.form['data']
        return {btn_id: buttonInfo[btn_id]}

api.add_resource(Fitness, '/<string:btn_id>')

if __name__ == '__main__':
    app.run(debug=True)



#curl http://localhost:5000/todo1 -d "data=Remember the milk" -X POST