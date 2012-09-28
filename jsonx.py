import json

def to_dict(obj):
    result = {}
    for attrname in dir(obj):
        if not attrname.startswith('__') and not callable(getattr(obj, attrname)):
            result.update({attrname: getattr(obj, attrname)}) 
    return result

def to_json_str(obj, encoding='UTF-8'):
    result = to_dict(obj)
    return json.dumps(result, encoding=encoding)

def to_json_obj(str, encoding='UTF-8'):
    return json.loads(str)
