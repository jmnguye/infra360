from flask_restx import Resource, Namespace, fields

DOMAINS = {
    "domains": [
        {"label": "Compute", "value": "Compute"},
        {"label": "Network", "value": "Network"},
        {"label": "Storage", "value": "Storage"},
    ]
}


api = Namespace("domains", description="family class")

domain_fields = api.model("Domain", {"label": fields.String, "value": fields.String})
domains_dict_fields = api.model(
    "DomainsDict",
    {
        "domains": fields.List(fields.Nested(domain_fields)),
    },
)


@api.route("")
class Domains(Resource):
    @api.marshal_with(domains_dict_fields)
    def get(self):
        return DOMAINS

    def post(self):
        pass
