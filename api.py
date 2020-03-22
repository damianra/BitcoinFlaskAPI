from flask import Flask
from flask import render_template
from flask_restful import Api
from view.Resources import Price, AllData, Date, DateRange, RangeVariation

# Create flask application and API rest
app = Flask(__name__, static_folder='static', template_folder='template')
app.config['SECRET_KEY'] = 'Secret_Key'
api = Api(app, prefix="/api/v1")

# End points for the API
api.add_resource(Price, '/price')
api.add_resource(AllData, '/alldata')
api.add_resource(Date, '/date')
api.add_resource(DateRange, '/daterange')
api.add_resource(RangeVariation, '/rangevariation')


# Application route
@app.route('/')
def IndexApi():
    return render_template('index.html')


if __name__ == '__main__':
    # run application
    # debug=false only in production
    app.run(debug=False)