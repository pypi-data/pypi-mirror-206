import ast

_IW_ERROR_FOREIGN_KEY_CONSTRAINT = "IW09 ForeignKey without db_constraint=False"
_IW_ERROR_FOREIGN_KEY_ON_DELETE = "IW10 ForeignKey with on_delete=DO_NOTHING"

FIELD_TYPES = {"ForeignKey", "OneToOneField"}


class ForeignKeyCheckFinder(ast.NodeVisitor):
    def __init__(self, _, *args, **kwargs) -> None:
        self.issues: list[tuple] = []

        super().__init__()

    def visit_Call(self, node: ast.Call) -> ast.Call:
        is_foreign_key = (isinstance(node.func, ast.Attribute) and node.func.attr in FIELD_TYPES) or (
            isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id in FIELD_TYPES
        )

        if is_foreign_key:
            if not any([keyword.arg == "db_constraint" and keyword.value.value is False for keyword in node.keywords]):
                self.issues.append(
                    (node.func.lineno, node.func.col_offset, _IW_ERROR_FOREIGN_KEY_CONSTRAINT)
                )

            if any([keyword.arg == "on_delete" and keyword.value.attr == "DO_NOTHING" for keyword in node.keywords]):
                self.issues.append(
                    (node.func.lineno, node.func.col_offset, _IW_ERROR_FOREIGN_KEY_ON_DELETE)
                )

        self.generic_visit(node)
        return node
