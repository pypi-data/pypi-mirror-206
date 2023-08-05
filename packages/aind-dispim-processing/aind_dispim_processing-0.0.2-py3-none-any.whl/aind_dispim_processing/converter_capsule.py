"""
Schema and Entrypoint for Converter CO Capsule.
"""
import json

import argschema  # Analogous to pydantic, input validation
import argschema.fields as fld
import boto3
from aind_data_transfer.transformations import converters, file_io


class ConversionSchema(argschema.ArgSchema):
    """
    Standardized Input to Conversion Capsule validated by Argschema.
    """

    dataset_path = fld.String(
        required=True, metadata={"description": "Path to mounted dataset"}
    )

    bucket_name = fld.String(
        required=True, metadata={"description": "Name of dataset bucket"}
    )

    tile_query = fld.String(
        required=False,
        load_default="",
        metadata={"description": "Tile query for tiles to register"},
    )

    output_path = fld.String(
        required=True,
        metadata={"description": "Output path of registration xml"},
    )


# def write_json(bucket_name: str, path: str, json_data: dict):
#     """Writes json dict to bucket/path."""
#     s3 = boto3.resource("s3")
#     s3object = s3.Object(bucket_name, path)
#     s3object.put(Body=(bytes(json.dumps(json_data).encode("UTF-8"))))


def main():
    """Capsule Entrypoint."""
    parser = argschema.ArgSchemaParser(schema_type=ConversionSchema)
    args = dict(parser.args)

    log_dict = file_io.read_log_file(
        args["dataset_path"] + "/" + "schema_log.log"
    )
    acq_obj = converters.log_to_acq_json(log_dict)
    write_json(args["bucket_name"], args["dataset_path"], acq_obj)

    # NOTE: Need to sort out precise paths that go into xml files
    xml_tree = converters.acq_json_to_xml(
        acq_obj, args["dataset_path"], zarr=True, condition=args["tile_query"]
    )

    file_io.write_xml(xml_tree, path=args["output_path"] + "/output.xml")


if __name__ == "__main__":
    main()
