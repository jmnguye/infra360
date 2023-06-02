from flask_restx import Resource, Namespace

DOMAINS = {
    "1": {"label": "Compute", "value": "Compute"},
    "2": {"label": "Network", "value": "Network"},
    "3": {"label": "Storage", "value": "Storage"},
}

api = Namespace("domains", description="family class")


@api.route("")
class Domains(Resource):
    def get(self):
        return DOMAINS
