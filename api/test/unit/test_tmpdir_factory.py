import json
from _pytest._py.path import LocalPath


def test_tmpdir_factory(db_init: LocalPath) -> None:
    with db_init.open() as file:
        data = json.load(file)
        print(data["domains"][0])
        assert data["domains"][0] == '{"id": 1, "label": "Compute", "value": "Compute"}'
