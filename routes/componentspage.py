from flask import render_template
from flask import Blueprint

componentspage_bp = Blueprint('componentspage', __name__, template_folder='templates', static_folder='static')

@componentspage_bp.route('/alert')
def alert():
    return render_template('componentspage/alert.html',
        title='Alerts',
        subtitle='Components / Alerts'
    )

@componentspage_bp.route('/avatar')
def avatar():
    return render_template('componentspage/avatar.html',
        title='Avatars',
        subtitle='Components / Avatars'
    )

@componentspage_bp.route('/badges')
def badges():
    return render_template('componentspage/badges.html',
        title='Badges',
        subtitle='Components / Badges'
    )

@componentspage_bp.route('/button')
def button():
    return render_template('componentspage/button.html',
        title='Button',
        subtitle='Components / Button'
    )

@componentspage_bp.route('/calendar')
def calendar():
    return render_template('componentspage/calendar.html',
        title='Calendar',
        subtitle='Components / Calendar',
        multi_script=['assets/js/flatpickr.js', 'assets/js/full-calendar.js']
    )

@componentspage_bp.route('/card')
def card():
    return render_template('componentspage/card.html',
        title='Card',
        subtitle='Components / Card',
        multi_script=['assets/js/flatpickr.js', 'assets/js/full-calendar.js']
    )

@componentspage_bp.route('/carousel')
def carousel():
    return render_template('componentspage/carousel.html',
        title='Carousel',
        subtitle='Components / Carousel',
        script='assets/js/defaultCarousel.js'
    )

@componentspage_bp.route('/colors')
def colors():
    return render_template('componentspage/colors.html',
        title='Colors',
        subtitle='Components / Colors'
    )

@componentspage_bp.route('/dropdown')
def dropdown():
    return render_template('componentspage/dropdown.html',
        title='Dropdown',
        subtitle='Components / Dropdown'
    )

@componentspage_bp.route('/image-upload')
def imageUpload():
    return render_template('componentspage/imageUpload.html',
        title='Radio',
        subtitle='Components / Radio'
    )

@componentspage_bp.route('/lists')
def lists():
    return render_template('componentspage/lists.html',
        title='List',
        subtitle='Components / List'
    )

@componentspage_bp.route('/pagination')
def pagination():
    return render_template('componentspage/pagination.html',
        title= 'Pagination',
        subtitle='Components / Pagination'
    )

@componentspage_bp.route('/progress')
def progress():
    return render_template('componentspage/progress.html',
        title= 'Progress Bar',
        subtitle='Components / Progress Bar'
    )

@componentspage_bp.route('/radio')
def radio():
    return render_template('componentspage/radio.html',
        title= 'Radio',
        subtitle='Components / Radio'
    )

@componentspage_bp.route('/star-rating')
def starRating():
    return render_template('componentspage/starRating.html',
        title= 'Star Ratings',
        subtitle='Components / Star Ratings'
    )

@componentspage_bp.route('/switch')
def switch():
    return render_template('componentspage/switch.html',
        title= 'Radio',
        subtitle='Components / Radio'
    )

@componentspage_bp.route('/tabs')
def tabs():
    return render_template('componentspage/tabs.html',
        title= 'Tab & Accordion',
        subtitle='Components / Tab & Accordion'
    )

@componentspage_bp.route('/tags')
def tags():
    return render_template('componentspage/tags.html',
        title= 'Tags',
        subtitle='Components / Tags'
    )

@componentspage_bp.route('/tooltip')
def tooltip():
    return render_template('componentspage/tooltip.html',
        title= 'Tooltip & Popover',
        subtitle='Components / Tooltip & Popover',
        script='assets/js/defaultCarousel.js'
    )

@componentspage_bp.route('/typography')
def typography():
    return render_template('componentspage/typography.html',
        title= 'Typography',
        subtitle='Components / Typography'
    )

@componentspage_bp.route('/videos')
def videos():
    return render_template('componentspage/videos.html',
        title= 'Videos',
        subtitle='Components / Videos'
    )