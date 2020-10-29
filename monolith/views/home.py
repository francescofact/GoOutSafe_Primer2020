from flask import Blueprint, render_template

from monolith.database import db, Restaurant, Like, Positive
from monolith.auth import current_user
from monolith.forms import ReservationForm

home = Blueprint("home", __name__)


@home.route("/")
def index():
    restaurants = db.session.query(Restaurant)
    form = ReservationForm()
    n_positive = db.session.query(Positive).filter_by(marked=True).count()
    n_healed = (
        db.session.query(Positive)
        .filter_by(marked=False)
        .distinct(Positive.user_id)
        .count()
    )

    return render_template(
        "index.html", restaurants=restaurants, form=form,  n_positive=n_positive, n_healed=n_healed
    )
