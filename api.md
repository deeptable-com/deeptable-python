# Files

Types:

```python
from deeptable.types import File
```

Methods:

- <code title="get /v1/files/{file_id}">client.files.<a href="./src/deeptable/resources/files.py">retrieve</a>(file_id) -> <a href="./src/deeptable/types/file.py">File</a></code>
- <code title="get /v1/files">client.files.<a href="./src/deeptable/resources/files.py">list</a>(\*\*<a href="src/deeptable/types/file_list_params.py">params</a>) -> <a href="./src/deeptable/types/file.py">SyncCursorIDPage[File]</a></code>
- <code title="delete /v1/files/{file_id}">client.files.<a href="./src/deeptable/resources/files.py">delete</a>(file_id) -> None</code>
- <code title="get /v1/files/{file_id}/content">client.files.<a href="./src/deeptable/resources/files.py">download</a>(file_id) -> BinaryAPIResponse</code>
- <code title="post /v1/files">client.files.<a href="./src/deeptable/resources/files.py">upload</a>(\*\*<a href="src/deeptable/types/file_upload_params.py">params</a>) -> <a href="./src/deeptable/types/file.py">File</a></code>

# StructuredSheets

Types:

```python
from deeptable.types import StructuredSheetsResponse
```

Methods:

- <code title="post /v1/structured-sheets">client.structured_sheets.<a href="./src/deeptable/resources/structured_sheets/structured_sheets.py">create</a>(\*\*<a href="src/deeptable/types/structured_sheet_create_params.py">params</a>) -> <a href="./src/deeptable/types/structured_sheets_response.py">StructuredSheetsResponse</a></code>
- <code title="get /v1/structured-sheets/{structured_sheets_id}">client.structured_sheets.<a href="./src/deeptable/resources/structured_sheets/structured_sheets.py">retrieve</a>(structured_sheets_id) -> <a href="./src/deeptable/types/structured_sheets_response.py">StructuredSheetsResponse</a></code>
- <code title="get /v1/structured-sheets">client.structured_sheets.<a href="./src/deeptable/resources/structured_sheets/structured_sheets.py">list</a>(\*\*<a href="src/deeptable/types/structured_sheet_list_params.py">params</a>) -> <a href="./src/deeptable/types/structured_sheets_response.py">SyncCursorIDPage[StructuredSheetsResponse]</a></code>
- <code title="delete /v1/structured-sheets/{structured_sheets_id}">client.structured_sheets.<a href="./src/deeptable/resources/structured_sheets/structured_sheets.py">delete</a>(structured_sheets_id) -> None</code>
- <code title="post /v1/structured-sheets/{structured_sheets_id}/cancel">client.structured_sheets.<a href="./src/deeptable/resources/structured_sheets/structured_sheets.py">cancel</a>(structured_sheets_id) -> <a href="./src/deeptable/types/structured_sheets_response.py">StructuredSheetsResponse</a></code>
- <code title="get /v1/structured-sheets/{structured_sheets_id}/download">client.structured_sheets.<a href="./src/deeptable/resources/structured_sheets/structured_sheets.py">download</a>(structured_sheets_id, \*\*<a href="src/deeptable/types/structured_sheet_download_params.py">params</a>) -> BinaryAPIResponse</code>

## Tables

Types:

```python
from deeptable.types.structured_sheets import TableResponse, TableListResponse
```

Methods:

- <code title="get /v1/structured-sheets/{structured_sheets_id}/tables/{table_id}">client.structured_sheets.tables.<a href="./src/deeptable/resources/structured_sheets/tables.py">retrieve</a>(table_id, \*, structured_sheets_id) -> <a href="./src/deeptable/types/structured_sheets/table_response.py">TableResponse</a></code>
- <code title="get /v1/structured-sheets/{structured_sheets_id}/tables">client.structured_sheets.tables.<a href="./src/deeptable/resources/structured_sheets/tables.py">list</a>(structured_sheets_id) -> <a href="./src/deeptable/types/structured_sheets/table_list_response.py">TableListResponse</a></code>
- <code title="get /v1/structured-sheets/{structured_sheets_id}/tables/{table_id}/download">client.structured_sheets.tables.<a href="./src/deeptable/resources/structured_sheets/tables.py">download</a>(table_id, \*, structured_sheets_id, \*\*<a href="src/deeptable/types/structured_sheets/table_download_params.py">params</a>) -> BinaryAPIResponse</code>
