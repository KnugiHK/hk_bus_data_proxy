from flask import Flask, Response, request
import requests
from flask_cors import CORS


app = Flask(__name__)
CORS(app)
__version__ = "0.0.4"

HEADERS = {"User-Agent": "proxy"}
BASE_URL_RT = "https://rt.data.gov.hk"
BASE_URL_DATA = "https://data.etabus.gov.hk"


@app.route("/")
def index():
    return f"Works! Running version: {__version__}"


@app.route("/v1/transport/kmb/eta/<stop_id>/<route>/<dir>")
def eta(stop_id, route, dir):
    r = requests.get(
        BASE_URL_DATA + request.path,
        headers=HEADERS
    )
    return Response(r.text, mimetype='application/json')


@app.route("/v1/transport/kmb/stop-eta/<stop_id>")
def stop_eta(stop_id):
    r = requests.get(
        BASE_URL_DATA + request.path,
        headers=HEADERS
    )
    return Response(r.text, mimetype='application/json')


@app.route("/v1/transport/kmb/route-eta/<route>/<service_type>")
def route_eta(route, service_type):
    r = requests.get(
        BASE_URL_RT + request.path,
        headers=HEADERS
    )
    return Response(r.text, mimetype='application/json')


@app.route("/v1/transport/citybus-nwfb/eta/<company_id>/<stop_id>/<route>")
def citybus_nwfb(company_id, stop_id, route):
    r = requests.get(
        BASE_URL_RT + request.path,
        headers=HEADERS
    )
    return Response(r.text, mimetype='application/json')


@app.route("/v1/transport/batch/stop-eta/<company_id>/<stop_id>")
def batch(company_id, stop_id):
    r = requests.get(
        BASE_URL_RT + request.path,
        headers=HEADERS
    )
    return Response(r.text, mimetype='application/json')


@app.route("/gs/api/v1.0.0/locationSearch")
def gs():
    q = request.args.get('q')
    r = requests.get(
        "https://geodata.gov.hk/gs/api/v1.0.0/locationSearch",
        params={"q": q},
        headers=HEADERS
    )
    return Response(r.text, mimetype='application/json')


@app.route("/v1/transport/mtr/bus/getSchedule", methods=["POST"])
def mtr_bus():
    r = requests.post(
        BASE_URL_RT + "/v1/transport/mtr/bus/getSchedule",
        json=request.get_json(True),
        headers=HEADERS
    )
    return Response(r.text, mimetype='application/json')


if __name__ == "__main__":
    app.run(ssl_context='adhoc')
