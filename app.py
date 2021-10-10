from flask import Flask, Response, request
import requests
from flask_cors import CORS


app = Flask(__name__)
CORS(app)


HEADERS = {"User-Agent": "proxy"}
BASE_URL_RT = "https://rt.data.gov.hk/v1/transport"
BASE_URL_DATA = "https://data.etabus.gov.hk/v1/transport"


@app.route("/")
def index():
    return "Works"


@app.route("/v1/transport/kmb/eta/<stop_id>/<route>/<dir>")
def eta(stop_id, route, dir):
    r = requests.get(
        f"{BASE_URL_DATA}/kmb/eta/{stop_id}/{route}/{dir}",
        headers=HEADERS
    )
    return Response(r.text, mimetype='application/json')


@app.route("/v1/transport/kmb/stop-eta/<stop_id>")
def stop_eta(stop_id):
    r = requests.get(
        f"{BASE_URL_DATA}/kmb/stop-eta/{stop_id}",
        headers=HEADERS
    )
    return Response(r.text, mimetype='application/json')


@app.route("/v1/transport/kmb/route-eta/{route}/{service_type}")
def route_eta(route, service_type):
    r = requests.get(
        f"{BASE_URL_DATA}/kmb/route-eta/{route}/{service_type}",
        headers=HEADERS
    )
    return Response(r.text, mimetype='application/json')


@app.route("/v1/transport/citybus-nwfb/eta/<company_id>/<stop_id>/<route>")
def citybus_nwfb(company_id, stop_id, route):
    r = requests.get(
        f"{BASE_URL_RT}/citybus-nwfb/eta/{company_id}/{stop_id}/{route}",
        headers=HEADERS
    )
    return Response(r.text, mimetype='application/json')


@app.route("/v1/transport/batch/stop-eta/<company_id>/<stop_id>")
def batch(company_id, stop_id):
    r = requests.get(
        f"{BASE_URL_RT}/batch/stop-eta/{company_id}/{stop_id}",
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


if __name__ == "__main__":
    app.run(ssl_context='adhoc')
