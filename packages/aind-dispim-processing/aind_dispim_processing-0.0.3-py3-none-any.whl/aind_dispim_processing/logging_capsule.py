"""
Schema and Entrypoint for Logging CO Capsule.
"""
import argschema  # Analogous to pydantic, input validation
import argschema.fields as fld
import boto3
import ng_link


class LoggingSchema(argschema.ArgSchema):
    """
    Standardized Input to Logging Capsule validated by Argschema.
    """

    base_xml_path = fld.String(
        required=True,
        metadata={"description": "Local Path to XML for registration"},
    )
    s3_uri = fld.String(
        required=True, metadata={"description": "S3 URI of dataset directory"}
    )
    dispim = fld.Boolean(
        required=True,
        metadata={"description": "Trigger Exaspim or Dispim Schemas."},
    )


class ExaspimSchema(argschema.ArgSchema):
    """
    Special Inputs for Exaspim Dataset.
    """

    max_dynamic_range = fld.Int(
        required=False,
        load_default=200,
        metadata={"description": "Max Dynamic Range"},
    )
    opacity = fld.Float(
        required=False, load_default=0.5, metadata={"description": "Opacity"}
    )
    blend = fld.String(
        required=False,
        load_default="default",
        metadata={"description": "Blending"},
    )


class DispimSchema(argschema.ArgSchema):
    """
    Special Inputs for Dispim Dataset.
    """

    coreg_xml_path = fld.String(
        required=True,  # Required!
        metadata={
            "description": "Local Path to cross-channel registration XML"
        },
    )

    deskew_angle = fld.Float(
        required=False,
        load_default=45,
        metadata={"description": "Deskew Angle"},
    )
    max_dynamic_range = fld.Int(
        required=False,
        load_default=800,
        metadata={"description": "Max Dynamic Range"},
    )
    opacity = fld.Float(
        required=False, load_default=0.5, metadata={"description": "Opacity"}
    )
    blend = fld.String(
        required=False,
        load_default="additive",
        metadata={"description": "Blending"},
    )


def write_txt_file(content: str, filepath: str) -> None:
    """
    Writes content to a textfile at given filepath.
    """
    with open(filepath, "w") as f:
        f.write(content)


def write_file_s3(local_path: str, bucket_name: str, bucket_path: str) -> None:
    """
    Writes local file S3 at bucket_name/bucket_path.
    """

    s3_client = boto3.client("s3")
    s3_client.upload_file(local_path, bucket_name, bucket_path)


def main():
    """Capsule Entrypoint."""
    logging_parser = argschema.ArgSchemaParser(schema_type=LoggingSchema)
    params = dict(logging_parser.args)

    # Dispim Link
    if params["dispim"] is True:
        parser = argschema.ArgSchemaParser(schema_type=DispimSchema)
        params.update(dict(parser.args))
        ng_link.generate_dispim_link(
            params["base_xml_path"],
            params["coreg_xml_path"],
            params["s3_uri"],
            params["max_dynamic_range"],
            params["opacity"],
            params["blend"],
            params["deskew_angle"],
            params["output_json_path"],
        )

    # Exaspim Link
    else:
        parser = argschema.ArgSchemaParser(schema_type=ExaspimSchema)
        params.update(dict(parser.args))
        ng_link.generate_exaspim_link(
            params["base_xml_path"],
            params["s3_uri"],
            params["max_dynamic_range"],
            params["opacity"],
            params["blend"],
            params["output_json_path"],
        )

    # Finally, upload process_output.json to dataset bucket
    s3_uri_list = params["s3_uri"].split("/")
    local_json_path = params["output_json_path"] + "/" + "process_output.json"
    bucket_name = s3_uri_list[2]
    bucket_path = s3_uri_list[3]
    write_file_s3(local_json_path, bucket_name, bucket_path)
    write_txt_file(
        f"https://aind-neuroglancer-sauujisjxq-uw.a.run.app#!s3://{bucket_name}/bucket_path/process_output.json",
        "/results/ng-link.txt",
    )


if __name__ == "__main__":
    main()
