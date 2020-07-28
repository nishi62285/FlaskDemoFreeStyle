from flask_wtf import FlaskForm,Form,CSRFProtect
from flask import app,Blueprint,request,make_response,render_template,redirect,url_for,session
from Forms.DealForm import DealForm
deal=Blueprint(name='deal',import_name=__name__,template_folder='templates',url_prefix='/deal')

# @deal.before_request
# def be():
#     pass

@deal.after_request
def tear_request(response):
    response.headers.add('Cache-Control', 'no-store, no-cache, must-revalidate, post-check=0, pre-check=0')
    return response


@deal.errorhandler(Exception)
def handle_error(error):
    return render_template('error.html',error=error)

@deal.route('/deal',methods=['GET','POST'])
def deal_form():
    session['current']='deal'
    form = DealForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            return redirect(url_for('deal.show_deals'))
    return render_template('deal_create.html',form=form)


    # form=Deal()
    # return render_template('deal_create.html',form=form)

# @deal.route('/create',methods=['POST'])
# def create_deal():
#     form = Deal()
#     if form.validate_on_submit():
#         return redirect(url_for('show_deals'))
#     else:
#         return render_template('deal_create.html',form=form)#redirect(url_for('deal.deal_form',form=form))

@deal.route('/error')
def error_deal():
    response= make_response(render_template('error.html'))
    return response

@deal.route('/deals',methods=['GET'])
def show_deals():
    from Repository.DealRepository import get_deals
    deals=get_deals(_id=0)
    return render_template('show_deals.html',deals=deals)


