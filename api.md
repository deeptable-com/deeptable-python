# Files

Types:

```python
from deeptable.types import File, FileListResponse
```

Methods:

- <code title="get /v1/files/{file_id}">client.files.<a href="./src/deeptable/resources/files.py">retrieve</a>(file_id) -> <a href="./src/deeptable/types/file.py">File</a></code>
- <code title="get /v1/files">client.files.<a href="./src/deeptable/resources/files.py">list</a>(\*\*<a href="src/deeptable/types/file_list_params.py">params</a>) -> <a href="./src/deeptable/types/file_list_response.py">FileListResponse</a></code>
- <code title="delete /v1/files/{file_id}">client.files.<a href="./src/deeptable/resources/files.py">delete</a>(file_id) -> None</code>
- <code title="post /v1/files">client.files.<a href="./src/deeptable/resources/files.py">upload</a>(\*\*<a href="src/deeptable/types/file_upload_params.py">params</a>) -> <a href="./src/deeptable/types/file.py">File</a></code>

# StructuredSheets

Types:

```python
from deeptable.types import StructuredSheetResponse, StructuredSheetListResponse
```

Methods:

- <code title="post /v1/structured-sheets">client.structured_sheets.<a href="./src/deeptable/resources/structured_sheets/structured_sheets.py">create</a>(\*\*<a href="src/deeptable/types/structured_sheet_create_params.py">params</a>) -> <a href="./src/deeptable/types/structured_sheet_response.py">StructuredSheetResponse</a></code>
- <code title="get /v1/structured-sheets/{structured_sheets_id}">client.structured_sheets.<a href="./src/deeptable/resources/structured_sheets/structured_sheets.py">retrieve</a>(structured_sheets_id) -> <a href="./src/deeptable/types/structured_sheet_response.py">StructuredSheetResponse</a></code>
- <code title="get /v1/structured-sheets">client.structured_sheets.<a href="./src/deeptable/resources/structured_sheets/structured_sheets.py">list</a>(\*\*<a href="src/deeptable/types/structured_sheet_list_params.py">params</a>) -> <a href="./src/deeptable/types/structured_sheet_list_response.py">StructuredSheetListResponse</a></code>
- <code title="delete /v1/structured-sheets/{structured_sheets_id}">client.structured_sheets.<a href="./src/deeptable/resources/structured_sheets/structured_sheets.py">delete</a>(structured_sheets_id) -> None</code>

## Exports

Methods:

- <code title="get /v1/structured-sheets/{structured_sheets_id}/exports/sqlite">client.structured_sheets.exports.<a href="./src/deeptable/resources/structured_sheets/exports.py">download_sqlite</a>(structured_sheets_id) -> BinaryAPIResponse</code>
