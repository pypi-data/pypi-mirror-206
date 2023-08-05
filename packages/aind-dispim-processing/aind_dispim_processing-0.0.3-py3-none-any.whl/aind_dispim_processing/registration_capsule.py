"""
Schema and Entrypoint for Registration CO Capsule.
"""
import os

# import shutil
import subprocess

import argschema  # Analogous to pydantic, input validation
import argschema.fields as fld
import psutil


class RegistrationSchema(argschema.ArgSchema):
    """
    Standardized Input to Registration Capsule validated by Argschema.
    """

    dataset_path = fld.String(
        required=True, metadata={"description": "Path to mounted dataset"}
    )
    xml_path = fld.String(
        required=True, metadata={"description": "Path to XML for registration"}
    )
    downsample_factor = fld.Int(
        required=False,
        load_default=8,
        metadata={"description": "Exponents of 2: 2^0, 2^1, 2^2, ..."},
    )
    anchor_tile = fld.Int(
        required=False,
        load_default=0,
        metadata={"description": "Index of tile in dataset to be fixed."},
    )
    output_path = fld.String(
        required=True,
        metadata={
            "description": "Output xml path containing registration transforms."
        },
    )


def get_hardware_macro() -> str:
    """
    Returns ImageJ hardware configuration macro with maximal hardware utilization.
    """

    mem_mb = psutil.virtual_memory().total / (1024 * 1024)
    usable_mb = mem_mb * 0.8
    n_cpus = os.cpu_count()

    MACRO = f"""
run("Memory & Threads...", "maximum={usable_mb} parallel={n_cpus}");
    """
    return MACRO


def get_registration_macro() -> str:
    """
    Returns ImageJ phase correlation macro with parameters from RegistrationSchema parser.
    """
    reg_parser = argschema.ArgSchemaParser(schema_type=RegistrationSchema)

    MACRO = f"""
run("Calculate pairwise shifts ...", "select=[{RegistrationSchema.xml_path}]
process_angle=[All angles] process_channel=[All channels] process_illumination=[All illuminations] process_tile=[All tiles] process_timepoint=[All Timepoints]
method=[Phase Correlation]
downsample_in_x={reg_parser.downsample_factor}
downsample_in_y={reg_parser.downsample_factor}
downsample_in_z={reg_parser.downsample_factor}");
run("Optimize globally and apply shifts ...", "select=[{RegistrationSchema.xml_path}]
process_angle=[All angles] process_channel=[All channels] process_illumination=[All illuminations] process_tile=[All tiles] process_timepoint=[All Timepoints]
relative=2.500 absolute=3.500 global_optimization_strategy=[Two-Round using Metadata to align unconnected Tiles]
fix_group_0-{reg_parser.anchor_tile}");
"""
    return MACRO


def execute_macro(macro: str) -> None:
    """
    Spawns headless ImageJ process to run input macro.
    """

    # Simply overwrites any existing macro file
    macro_path = "/results/macro.ijm"
    with open(macro_path, "w") as f:
        f.write(macro)

    command = [
        "ImageJ",
        "-Dimagej.updater.disableAutocheck=true",
        "--headless",
        "--console",
        "--run",
    ]
    popen = subprocess.Popen(
        command, stdout=subprocess.PIPE, universal_newlines=True, shell=True
    )
    for stdout_line in iter(popen.stdout.readline, ""):
        yield str(stdout_line).strip()
    popen.stdout.close()
    return_code = popen.wait()
    if return_code:
        raise subprocess.CalledProcessError(return_code, command)


def main():
    """Capsule Entrypoint."""
    RUN_SCRIPT = "".join(get_hardware_macro()).join(get_registration_macro())
    execute_macro(RUN_SCRIPT)


if __name__ == "__main__":
    main()
