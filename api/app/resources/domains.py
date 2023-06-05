from flask_restx import Resource, Namespace, fields
from app.models.domain import DomainDAO
from app.models.domains import DomainsDAO
import json

DOMAINS = {
    "domains": [
        DomainDAO(1, "Compute", "Compute"),
        DomainDAO(2, "Network", "Network"),
        DomainDAO(3, "Storage", "Storage"),
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
domain_put_fields = api.model(
    "DomainPut",
    {
        "label": fields.String(description="Label displayed"),
        "value": fields.String(description="Value"),
    },
    strict=True,
)


domainsDAO = DomainsDAO(DOMAINS)


@api.route("")
class Domains(Resource):
    @api.marshal_with(domains_dict_fields)
    def get(self):
        return domainsDAO.domains

    @api.marshal_with(domains_dict_fields)
    @api.expect(domain_post_fields, validate=True)
    def post(self):
        return domainsDAO.add(api.payload)


@api.route("/<int:id>")
class Domain(Resource):
    @api.marshal_with(domain_get_fields)
    @api.expect(domain_put_fields, validate=True)
    def put(self, id):
        domainJson = self.get(id)
        domain = DomainDAO.domainFactory(domainJson)
        updatedDomain = domain.update(api.payload)
        domainsDAO.update(updatedDomain)
        return json.loads(updatedDomain.json())

    def get(self, id):
        domain = domainsDAO.get_by(id)
        return json.loads(domain.json())


# on va mettre la modification avec le put
# on va ajouter la suppression avec le delete
