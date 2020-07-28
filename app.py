from flask import Flask,redirect,url_for,request,render_template,abort,g,make_response
from jinja2 import TemplateNotFound
from flask_swagger_ui import get_swaggerui_blueprint
app=Flask(__name__)
from Product.product import product_bp
from Inventory.inventory import inventory_bp
from flask_cors import CORS,cross_origin
cors=CORS(app,resources={'*':{'origins':'*'}})
from simple_guid import UIDGenerator
from flask_debugtoolbar import DebugToolbarExtension
from Deal.deal_process import deal

SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.json'
SWAGGERUI_BLUEPRINT = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "Seans-Python-Flask-REST-Boilerplate"
    }
)


def home():
    return render_template('index.html',a=1,b=2)

# @app.teardown_appcontext
# def tear_app(data):
#     a=data
#
# @app.teardown_request
# def tear_request(data):
#     a=data


@app.errorhandler(Exception)
def handle_error(error):
    data=error
    return render_template('error.html',error=error)


@cross_origin()
@app.route('/test',defaults={'id':1})
@app.route('/test123/<int:id>')
def test(id):
    try:
        import time
        time.sleep(20)
        g.owner='Me'
        body=render_template('index.html',a=id)
        response=make_response(body)
        #return render_template('index.html',a=id)
        return response
    except TemplateNotFound as t:
        abort(404)


@app.route('/foo/<string:id>/<int:id1>')
def foo(id,id1):
    return str(id)

@app.route('/bar/')
def bar():
    a=request.args.get('name')
    return redirect(url_for('foo',**{'id':int(a),'id1':2}))

if __name__ == '__main__':
    app.register_blueprint(product_bp)
    app.register_blueprint(inventory_bp)
    app.add_url_rule('/home','home',home)
    app.register_blueprint(deal)
    app.register_blueprint(SWAGGERUI_BLUEPRINT, url_prefix=SWAGGER_URL)
    from flask import current_app
    uid=UIDGenerator(app)
    app.config['SECRET_KEY']=str(uid.get_uid())
    app.config['DB_URL'] = 'Driver={SQL Server};''Server=LAPTOP-26CR59NM\SQLEXPRESS;''Database=ORG;''Trusted_Connection=yes;'
    toolbar = DebugToolbarExtension(app)
    print("***************************** {0}".format(uid.get_uid()))
    with app.app_context():
        a = current_app.name
    app.run(debug=True,threaded=True,use_reloader=False)


