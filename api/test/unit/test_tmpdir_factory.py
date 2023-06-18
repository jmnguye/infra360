import json


def test_tmpdir_factory(db_init):
    with db_init.open() as file:
        data = json.load(file)
        print(data["domains"][0])
        assert data["domains"][0] == '{"id": 1, "label": "Compute", "value": "Compute"}'
