from flask import Blueprint, render_template

cars_bp = Blueprint('cars', __name__, template_folder='cars_templates')

@cars_bp.route('/cars')
def list_cars():
    return render_template('list_cars.html')
chsh -s /bin/zsh