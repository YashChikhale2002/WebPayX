from flask import render_template
from flask import Blueprint

invoice_bp = Blueprint('invoice', __name__, template_folder='templates', static_folder='static')

@invoice_bp.route('/invoice-add')
def invoiceAdd():
    return render_template('invoice/invoiceAdd.html',
        title='Invoice List',
        subtitle='Invoice List',
        script='assets/js/invoice.js'
    )

@invoice_bp.route('/invoice-edit')
def invoiceEdit():
    return render_template('invoice/invoiceEdit.html',
        title='Invoice List',
        subtitle='Invoice List',
        script='assets/js/invoice.js'
    )

@invoice_bp.route('/invoice-list')
def invoiceList():
    return render_template('invoice/invoiceList.html',
        title='Invoice List',
        subtitle='Invoice List',
    )

@invoice_bp.route('/invoice-preview')
def invoicePreview():
    return render_template('invoice/invoicePreview.html',
        title='Invoice List',
        subtitle='Invoice List',
    )