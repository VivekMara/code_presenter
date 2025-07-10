import tree_sitter_python as tspython
from tree_sitter import Language, Parser

class FunctionParser:
    def __init__(self, source_code):
        self.source_code = bytes(source_code, "utf8")
        PY_LANGUAGE = Language(tspython.language())
        parser = Parser(PY_LANGUAGE)
        self.tree = parser.parse(self.source_code)
        self.root = self.tree.root_node
    
    def extract_functions(self):
        functions = []
        for child in self.root.children:
            if child.type == "function_definition":
                name_node = child.child_by_field_name("name")
                func_code = self.source_code[child.start_byte:child.end_byte].decode()
                functions.append({
                    "name": name_node.text.decode(),
                    "start": child.start_point,
                    "end": child.end_point,
                    "code": func_code
                })
        return functions

code = """
def greet(name):
    print("Hello", name)

def add(a, b):
    return a + b
"""
new_par = FunctionParser(code)
funcs = new_par.extract_functions()
for f in funcs:
    print(f"\nFunction `{f['name']}`:\n{f['code']}")