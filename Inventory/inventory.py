from flask import Blueprint,app,render_template,request,url_for,g,current_app

inventory_bp=Blueprint('inventory_bp',__name__,template_folder='templates',url_prefix='/inventory')

def before():
    msg=request
    #raise Exception('bad')

def after(data):
    msg=data
    return data

@inventory_bp.errorhandler(Exception)
def handle_error(error):
    return {'error':'error1'}

inventory_bp.before_request(before)
inventory_bp.after_request(after)

@inventory_bp.route('/')
def index():
    g.id="swift"

    #return render_template('inventory.html')
    return render_template(url_for('product_bp.index'))
