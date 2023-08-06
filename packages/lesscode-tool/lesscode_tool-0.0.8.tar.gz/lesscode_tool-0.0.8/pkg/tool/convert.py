import re


def to_camel_case(x):
    """转驼峰法命名"""
    return re.sub('_([a-zA-Z])', lambda m: (m.group(1).upper()), x)


def to_upper_camel_case(x):
    """转大驼峰法命名"""
    s = re.sub('_([a-zA-Z])', lambda m: (m.group(1).upper()), x)
    return s[0].upper() + s[1:]


def to_lower_camel_case(x):
    """转小驼峰法命名"""
    s = re.sub('_([a-zA-Z])', lambda m: (m.group(1).upper()), x)
    return s[0].lower() + s[1:]


def retain_filed_quotation(key, origin):
    if isinstance(origin, str):
        origin = f"'{origin}'"
    elif key == "type":
        origin = origin.__repr__()
    return origin


def field_type_handle(field_type):
    return field_type


def dict2params_str(source: dict):
    return ','.join([f"{k}={retain_filed_quotation(k, v)}" for k, v in source.items()])
