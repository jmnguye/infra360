from app.models.domain import DomainDAO
from flask import abort


class DomainsDAO:
    def __init__(self, domains):
        self.domains = domains

    def add(self, data):
        id = self.get_id()
        new_domain = DomainDAO(id, data["label"], data["value"])
        self.domains["domains"].append(new_domain)
        return self.domains

    def get_id(self):
        reserved_id = [domain.id for domain in self.domains.get("domains")]
        for index in range(1, 1000):
            if index not in reserved_id:
                return index
        return None

    def get_by(self, id) -> DomainDAO:
        for domain in self.domains["domains"]:
            if domain.id == id:
                return domain
        abort(404, "domain id not found")

    def update(self, domain: DomainDAO) -> None:
        for existing_domain in self.domains["domains"]:
            if existing_domain.id == domain.id:
                self.domains["domains"].remove(existing_domain)
                self.domains["domains"].append(domain)
                return
        abort(404, "domain id not found")

    def delete(self, domain: DomainDAO) -> None:
        for existing_domain in self.domains["domains"]:
            if existing_domain.id == domain.id:
                self.domains["domains"].remove(existing_domain)
                return
        abort(404, "domain id not found")

    def __str__(self):
        return {"domains": [self.domains]}
