from flask import render_template
from flask import Blueprint

aiapplication_bp = Blueprint('aiapplication', __name__, template_folder='templates', static_folder='static')

@aiapplication_bp.route('/code-generator')
def codeGenerator():
    return render_template('aiapplication/codeGenerator.html',
        title='Code Generator',
        subtitle='Code Generator',
    )

@aiapplication_bp.route('/code-generatorNew')
def codeGeneratorNew():
    return render_template('aiapplication/codeGeneratorNew.html',
        title='Code Generator',
        subtitle='Code Generator',
    )

@aiapplication_bp.route('/image-generator')
def imageGenerator():
    return render_template('aiapplication/imageGenerator.html',
        title='Image Generator',
        subtitle='Image Generator',
    )

@aiapplication_bp.route('/text-generator')
def textGenerator():
    return render_template('aiapplication/textGenerator.html',
        title='Text Generator',
        subtitle='Text Generator',
    )

@aiapplication_bp.route('/text-generatorNew')
def textGeneratorNew():
    return render_template('aiapplication/textGeneratorNew.html',
        title='Text Generator',
        subtitle='Text Generator',
    )

@aiapplication_bp.route('/video-generator')
def videoGenerator():
    return render_template('aiapplication/videoGenerator.html',
        title='Video Generator',
        subtitle='Video Generator',
    )

@aiapplication_bp.route('/voice-generator')
def voiceGenerator():
    return render_template('aiapplication/voiceGenerator.html',
        title='Voice Generator',
        subtitle='Voice Generator',
    )
