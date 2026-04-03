import sqlglot
from sqlglot.expressions import Column, Where, Literal

RETAIL_COLUMNS = {"retailer_id", "store_id", "channel", "store_type"}
RETAIL_VALUES = {"retail", "store", "physical"}

def detect_retail_filter(tree):
    where = tree.find(Where)
    matches = []

    if not where:
        return False, matches

    for node in where.walk():
        if isinstance(node, Column):
            if node.name.lower() in RETAIL_COLUMNS:
                matches.append(node.name)

        if isinstance(node, Literal):
            if str(node.this).lower() in RETAIL_VALUES:
                matches.append(str(node.this))

    return len(matches) > 0, matches