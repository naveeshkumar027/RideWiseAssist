import ast
import io
import re
import streamlit as st
import pytesseract
from pathlib import Path
from PIL import Image
from pypdf import PdfReader

source = Path("app.py").read_text(encoding="utf-8")
tree = ast.parse(source)

wanted = {"load_policies", "find_relevant_policies"}
nodes = [
    node for node in tree.body
    if isinstance(node, ast.FunctionDef) and node.name in wanted
]

if len(nodes) != 2:
    raise RuntimeError("Could not find both policy functions in app.py")

module = ast.Module(body=nodes, type_ignores=[])
ast.fix_missing_locations(module)

namespace = {
    "st": st,
    "io": io,
    "re": re,
    "pytesseract": pytesseract,
    "Image": Image,
    "Path": Path,
    "PdfReader": PdfReader,
    "POLICY_DIR": Path("data/policies"),
}

exec(compile(module, "app.py", "exec"), namespace)

documents = namespace["load_policies"]()
print("Loaded policy pages:", len(documents))

question = (
    "For booking B-0001, what late-return fee applies "
    "to a Gold-tier customer who returned 20 minutes late?"
)

result = namespace["find_relevant_policies"](
    question, documents, limit=5
)

print(result)

if "annexure a" in result.lower() and "30 minutes" in result.lower():
    print("\nPASS: Gold grace-period rule was retrieved.")
else:
    print("\nFAIL: Gold grace-period rule was not retrieved.")