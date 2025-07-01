import os
from flask import Flask, redirect, render_template, url_for
from routes.chart import chart_bp
from routes.aiapplication import aiapplication_bp
from routes.authentication import authentication_bp
from routes.componentspage import componentspage_bp
from routes.dashboard import dashboard_bp
from routes.forms import forms_bp
from routes.invoice import invoice_bp
from routes.settings import settings_bp
from routes.table import table_bp
from routes.user import user_bp


wowdash = Flask(__name__,
            template_folder='resource/views',
            static_folder=os.path.abspath('static'))


wowdash.register_blueprint(aiapplication_bp)  
wowdash.register_blueprint(authentication_bp)  
wowdash.register_blueprint(chart_bp)
wowdash.register_blueprint(componentspage_bp) 
wowdash.register_blueprint(dashboard_bp)  
wowdash.register_blueprint(forms_bp)  
wowdash.register_blueprint(invoice_bp)  
wowdash.register_blueprint(settings_bp)  
wowdash.register_blueprint(table_bp) 
wowdash.register_blueprint(user_bp) 


#cryptocurrency
@wowdash.route('/wallet')
def wallet():
    return render_template('cryptocurrency/wallet.html',
        title='Wallet',
        subtitle='Wallet'
    )

#other pages
@wowdash.route('/calendar-main')
def calendarMain():
    return render_template('calendarMain.html',
        title='Calendar',
        subtitle='Components / Calendar',
        multi_script=['assets/js/full-calendar.js', 'assets/js/flatpickr.js']
    )

@wowdash.route('/chat-empty')
def chatEmpty():
    return render_template('chatEmpty.html',
        title='Chat',
        subtitle='Components / Chat'
    )

@wowdash.route('/chat-message')
def chatMessage():
    return render_template('chatMessage.html',
        title='Chat',
        subtitle='Chat'
    )

@wowdash.route('/chat-profile')
def chatProfile():
    return render_template('chatProfile.html',
        title='Chat',
        subtitle='Chat'
    )

@wowdash.route('/email')
def email():
    return render_template('email.html',
        title='Email',
        subtitle='Components / Email'
    )

@wowdash.route('/faq')
def faq():
    return render_template('faq.html',
        title='Faq',
        subtitle='Faq'
    )

@wowdash.route('/gallery')
def gallery():
    return render_template('gallery.html',
        title='Gallery',
        subtitle='Gallery'
    )

@wowdash.route('/image-upload')
def imageUpload():
    return render_template('imageUpload.html',
        title='Radio',
        subtitle='Components / Radio'
    )

@wowdash.route('/kanban')
def kanban():
    return render_template('kanban.html',
        title='Kanban',
        subtitle='Kanban'
    )

@wowdash.route('/page-error')
def pageError():
    return render_template('pageError.html',
        title='404',
        subtitle='404'
    )

@wowdash.route('/pricing')
def pricing():
    return render_template('pricing.html',
        title='Pricing',
        subtitle='Pricing'
    )

@wowdash.route('/starred')
def starred():
    return render_template('starred.html',
        title='Email',
        subtitle='Components / Email'
    )

@wowdash.route('/terms-condition')
def termsCondition():
    return render_template('termsCondition.html',
        title='Terms & Conditions',
        subtitle='Terms & Conditions',
        multi_script=['assets/js/editor.highlighted.min.js', 'assets/js/editor.quill.js', 'assets/js/editor.katex.min.js']
    )

@wowdash.route('/view-details')
def viewDetails():
    return render_template('viewDetails.html',
        title='Email',
        subtitle='Components / Email'
    )

@wowdash.route('/widgets')
def widgets():
    return render_template('widgets.html',
        title='Widgets',
        subtitle='Widgets',
        script='assets/js/widgets.js'
    )


if __name__ == '__main__':
    wowdash.run(debug=True)