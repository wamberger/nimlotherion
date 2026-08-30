

__all__ = [
    'read_file',
    'FileYAML',
    'FileJSON',
    'FileTOML',
    'FileCSV']


from nimlotherion.file.yaml_ import FileYAML
from nimlotherion.file.toml_ import FileTOML
from nimlotherion.file.json_ import FileJSON
from nimlotherion.file.csv_ import FileCSV


type DataObject = FileCSV | FileYAML | FileTOML | FileJSON


def read_file(file_format: str, file: str) -> DataObject:
    """
    Args:
        file_format (str): one of the formats: 'YAML', 'Toml', 'JSON' or 'CSV'.
        file: Absolute path to the file with the file name.

    Returns:
        Dict[str, T]: dict with str keys and values of any type.
    """

    try:
        match file_format.lower():
            case "csv":
                return FileCSV(file)
            case "yaml":
                return FileYAML(file)
            case "toml":
                return FileTOML(file)
            case "json":
                return FileJSON(file)
            case _:
                raise IOError(f"Not supported format: '{file_format}'")
    except IOError as e:
        raise e
