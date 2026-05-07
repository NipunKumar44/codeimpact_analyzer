import ast

def parse_file(file_path):

    with open(file_path, "r") as f:
        source = f.read()

    tree = ast.parse(source)

    functions = []

    ignored_functions = ["print"]

    for node in ast.walk(tree):

        if isinstance(node, ast.FunctionDef):

            function_name = node.name

            calls = []

            for child in ast.walk(node):

                if isinstance(child, ast.Call):

                    if isinstance(child.func, ast.Name):

                        if child.func.id not in ignored_functions:

                            calls.append(child.func.id)

            functions.append({
                "name": function_name,
                "calls": calls
            })

    return functions