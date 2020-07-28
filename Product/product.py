from flask import Blueprint,render_template

product_bp=Blueprint('product_bp',__name__,template_folder='templates',url_prefix='/product')

@product_bp.route('/')
def index():
    return render_template('product.html')

@product_bp.route('/show')
def show_product():
    return render_template('product.html')
