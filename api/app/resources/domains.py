from flask_restx import Resource, Namespace, fields
from flask import current_app

DOMAINS = {
    "domains": [
        {"id": 1, "label": "Compute", "value": "Compute"},
        {"id": 2, "label": "Network", "value": "Network"},
        {"id": 3, "label": "Storage", "value": "Storage"},
    ]
}


api = Namespace("domains", description="family class")

domain_post_fields = api.model(
    "DomainPost",
    {
        "label": fields.String(required=True, description="Label displayed"),
        "value": fields.String(required=True, description="Value"),
    },
    strict=True,
)
domain_get_fields = api.model(
    "DomainGet",
    {
        "id": fields.Integer(required=False, description="Domain ID"),
        "label": fields.String(required=True, description="Label displayed"),
        "value": fields.String(required=True, description="Value"),
    },
)
domains_dict_fields = api.model(
    "DomainsDict",
    {
        "domains": fields.List(
            fields.Nested(domain_get_fields), description="List of domains"
        ),
    },
)


class DomainsDAO:
    def __init__(self, domains):
        self.domains = domains

    def add(self, data):
        data["id"] = self.get_id()
        self.domains["domains"].append(data)

    def get_id(self):
        reserved_id = [domain["id"] for domain in self.domains.get("domains")]
        for index in range(1, 1000):
            if index not in reserved_id:
                return index


DAO = DomainsDAO(DOMAINS)


@api.route("")
class Domains(Resource):
    @api.marshal_with(domains_dict_fields)
    def get(self):
        return DAO.domains

    @api.expect(domain_post_fields, validate=True)
    @api.doc(expect=domain_post_fields)
    def post(
        self,
    ):
        DAO.add(api.payload)
        return DAO.domains
