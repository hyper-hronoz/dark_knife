import json
import ast

def ebisVseVRot() -> dict:
    with open("./hyi.hyi", "r") as file:
        # print(json.loads(content))
        content = file.read()
        return ast.literal_eval(content)

