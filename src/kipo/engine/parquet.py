from pathlib import Path

import polars as pl


def excel_to_parquet(
        input_file: str | Path,
        output_file: str | Path
) -> Path:
    input_file = Path(input_file)
    output_file = Path(output_file)

    df = pl.read_excel(input_file)

    df.write_parquet(output_file)

    return output_file
