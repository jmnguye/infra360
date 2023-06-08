from dataclasses import dataclass
import traceback
import json


@dataclass
class DomainDAO:
    id: int | None
    label: str
    value: str

    def __str__(self):
        return dict(id=self.id, label=self.label, value=self.value)

    def json(self):
        return json.dumps({"id": self.id, "label": self.label, "value": self.value})

    def update(self, data):
        print(list(data))
        for key in list(data):
            try:
                self.__setattr__(key, data.get(key))
            except AttributeError as e:
                traceback.print_tb(e.__traceback__)
        return self
