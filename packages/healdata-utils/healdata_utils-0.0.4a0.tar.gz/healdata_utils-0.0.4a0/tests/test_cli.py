import os
from pathlib import Path
from healdata_utils.cli import convert_to_vlmd


# test convert vlmd with redcap csv
def test_convert_to_vlmd_with_redcap_csv_no_output():
    data_dictionary_metadata = {
        "description": (
            "This is a proof of concept to demonstrate"
            " the healdata-utils functionality"
        ),
        "title": "Healdata-utils Demonstration Data Dictionary",
    }
    filepath = "data/example_redcap_demo.redcap.csv"
    data_dictionaries = convert_to_vlmd(
        filepath, data_dictionary_props=data_dictionary_metadata
    )
    csvtemplate = data_dictionaries["csvtemplate"]
    jsontemplate = data_dictionaries["jsontemplate"]
    errors = data_dictionaries["errors"]

    assert csvtemplate[5] == {
        "name": "telephone_1",
        "type": "string",
        "constraints.pattern": "^[0-9]{3}-[0-9]{3}-[0-9]{4}$",
        "description": "Contact Information: Phone number",
        "title": "Phone number",
        "module": "demographics",
    }
    assert csvtemplate[7] == {
        "name": "email",
        "type": "string",
        "format": "email",
        "description": "Contact Information: E-mail",
        "title": "E-mail",
        "module": "demographics",
    }
    assert csvtemplate[8] == {
        "name": "sex",
        "type": "integer",
        "encodings": "0=Female|1=Male",
        "constraints.enum": "0|1",
        "description": "Contact Information: Gender",
        "title": "Gender",
        "module": "demographics",
    }

    assert jsontemplate["description"] == data_dictionary_metadata["description"]
    assert jsontemplate["title"] == data_dictionary_metadata["title"]
    assert jsontemplate["data_dictionary"][5] == {
        "name": "telephone_1",
        "type": "string",
        "constraints": {"pattern": "^[0-9]{3}-[0-9]{3}-[0-9]{4}$"},
        "description": "Contact Information: Phone number",
        "title": "Phone number",
        "module": "demographics",
    }
    assert jsontemplate["data_dictionary"][7] == {
        "name": "email",
        "type": "string",
        "format": "email",
        "description": "Contact Information: E-mail",
        "title": "E-mail",
        "module": "demographics",
    }
    assert jsontemplate["data_dictionary"][8] == {
        "name": "sex",
        "type": "integer",
        "encodings": {"0": "Female", "1": "Male"},
        "constraints": {"enum": ["0", "1"]},
        "description": "Contact Information: Gender",
        "title": "Gender",
        "module": "demographics",
    }

    assert errors["jsontemplate"] == {"valid": True, "errors": []}
    assert errors["csvtemplate"] == {"valid": True, "errors": []}


os.chdir(Path(__file__).parent)
test_convert_to_vlmd_with_redcap_csv_no_output()
print("SUCCESS")
