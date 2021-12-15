import flask

from app.settings import Settings

Settings.TESTING = False

from app.controllers.customer_controller import CustomerController
from app.controllers.employee_controller import EmployeeController
from app.controllers.product_controller import ProductController
from app.controllers.store_controller import StoreController
from app.views.utils import StatusCode
import generators.db_control as db_control

bp = flask.Blueprint("main", __name__, template_folder="templates")


@bp.app_errorhandler(StatusCode.BAD_REQUEST_ERROR)
def bad_request_error_handler(error):
    return flask.render_template("error/400.html"), StatusCode.BAD_REQUEST_ERROR


@bp.app_errorhandler(StatusCode.NOT_FOUND_ERROR)
def not_found_error_handler(error):
    return flask.render_template("error/404.html"), StatusCode.NOT_FOUND_ERROR


@bp.app_errorhandler(StatusCode.INVALID_SERVER_ERROR)
def internal_server_error_handler(error):
    return flask.render_template("error/500.html"), StatusCode.INVALID_SERVER_ERROR


@bp.route("/")
def index():
    return flask.render_template("index.html")


@bp.route("/products")
def products_page():
    products = ProductController.find_all()
    return flask.render_template("items/product/content.html", products=products)


@bp.route("/stores")
def stores_page():
    stores = StoreController.find_all()
    return flask.render_template("items/store/content.html", stores=stores)


@bp.route("/stores/create", methods=["POST"])
def create_store():
    data = {key: (value if value else None) for key, value in flask.request.form.items()}
    try:
        StoreController.create(**data)
        flask.flash("Store created", "success")
    except Exception as error:
        print(error)
        flask.flash(str(error), "error")
    return flask.redirect(flask.url_for("main.stores_page"))


@bp.route("/employees")
def employees_page():
    employees = EmployeeController.find_all()
    return flask.render_template("items/employee/content.html", employees=employees)


@bp.route("/customers")
def customers_page():
    customers = CustomerController.find_all()
    return flask.render_template("items/customer/content.html", customers=customers)


@bp.route("/db/populate", methods=["POST"])
def populate():
    try:
        db_control.populate_mysql_db()
        flask.flash("MySQL database successfully populated", "success")
    except Exception as error:
        print(error)
        flask.flash("Something went wrong when populating MySQL database", "error")
    return flask.redirect(flask.url_for("main.index"))


@bp.route("/db/convert", methods=["POST"])
def convert():
    try:
        db_control.convert_mysql_to_mongo()
        flask.flash("Data in MySQL database successfully converted to data in Mongo database", "success")
    except Exception as error:
        print(error)
        flask.flash("Something went wrong with converting from MySQL to Mongo", "error")
    return flask.redirect(flask.url_for("main.index"))


@bp.route("/db/purge-mysql", methods=["POST"])
def purge_mysql():
    try:
        db_control.delete_data_from_mysql_db()
        flask.flash("MySQL database successfully purged", "success")
    except Exception as error:
        print(error)
        flask.flash("Something went wrong when purging MySQL database", "error")
    return flask.redirect(flask.url_for("main.index"))


@bp.route("/db/purge-mongo", methods=["POST"])
def purge_mongo():
    try:
        db_control.delete_data_from_mongo_db()
        flask.flash("Mongo database successfully purged", "success")
    except Exception as error:
        print(error)
        flask.flash("Something went wrong when purging Mongo database", "error")
    return flask.redirect(flask.url_for("main.index"))
