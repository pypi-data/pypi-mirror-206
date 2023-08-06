# PDFix SDK Package

Cross-Platform PDF Library

## Features
- Make PDF Accessible with an Automated PDF Remediation and Auto-Tagging
- PDF Data Extraction into structured formats (JSON, XML, HTML)
- PDF to HTML Conversion in fixed, reflowable, and structure-based layout
- Standard PDF Features like render, edit content, watermark, markup, sign, redact, fill-in forms, OCR

## Installation 

```
pip install pdfix-sdk
```

## Example

```
from pdfixsdk.Pdfix import *

pdfix = GetPdfix()
doc = pdfix.OpenDoc("path/to/your.pdf", "")
print(doc.GetNumPages())
doc.Close()
```

