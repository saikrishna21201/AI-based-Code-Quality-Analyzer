import ast

def extract_features(code):
    tree = ast.parse(code)
    return {
        "nodes": len(list(ast.walk(tree)))
    }

