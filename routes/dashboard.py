from flask import render_template
from flask import Blueprint

dashboard_bp = Blueprint('dashboard', __name__, template_folder='templates', static_folder='static')

@dashboard_bp.route('/', endpoint='index')
def index():
    return render_template('dashboard/index.html',
        title='Dashboard',
        subtitle='AI',
        script='assets/js/homeChart/homeOneChart.js'
    )

@dashboard_bp.route('/index2', endpoint='index2')
def index2():
    return render_template('dashboard/index2.html',
        title='Dashboard',
        subtitle='CRM',
        script='assets/js/homeChart/homeTwoChart.js'
    )

@dashboard_bp.route('/index3', endpoint='index3')
def index3():
    return render_template('dashboard/index3.html',
        title='Dashboard',
        subtitle='eCommerce',
        script='assets/js/homeChart/homeThreeChart.js'
    )

@dashboard_bp.route('/index4', endpoint='index4')
def index4():
    return render_template('dashboard/index4.html',
        title='Dashboard',
        subtitle='Cryptocracy',
        script='assets/js/homeChart/homeFourChart.js'
    )

@dashboard_bp.route('/index5', endpoint='index5')
def index5():
    return render_template('dashboard/index5.html',
        title='Dashboard',
        subtitle='Investment',
        script='assets/js/homeChart/homeFiveChart.js'
    )

@dashboard_bp.route('/index6', endpoint='index6')
def index6():
    return render_template('dashboard/index6.html',
        title='Dashboard',
        subtitle='LMS / Learning System',
        script='assets/js/homeChart/homeSixChart.js'
    )

@dashboard_bp.route('/index7', endpoint='index7')
def index7():
    return render_template('dashboard/index7.html',
        title='Dashboard',
        subtitle='NFT & Gaming',
        script='assets/js/homeChart/homeSevenChart.js'
    )

@dashboard_bp.route('/index8', endpoint='index8')
def index8():
    return render_template('dashboard/index8.html',
        title='Dashboard',
        subtitle='Medical',
        script='assets/js/homeChart/HomeEightChart.js'
    )

@dashboard_bp.route('/index9', endpoint='index9')
def index9():
    return render_template('dashboard/index9.html',
        title='Dashboard',
        subtitle='Analytics',
        script='assets/js/homeChart/homeNineChart.js'
    )
