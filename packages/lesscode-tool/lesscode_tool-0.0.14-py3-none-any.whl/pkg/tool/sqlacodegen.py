from sqlalchemy import create_engine, inspect, MetaData
from sqlalchemy.ext.automap import automap_base

from pkg.tool.convert import to_upper_camel_case, dict2params_str


def sqlacodegen(url, schemas=None, table_names=None, file=None):
    packages = dict()
    engine = create_engine(url, pool_recycle=7200)
    isp = inspect(engine)
    if engine.url.database is not None:
        dbs = [engine.url.database]
    elif schemas is not None:
        dbs = schemas
    else:
        dbs = isp.get_schema_names()

    tables = list()
    if table_names is None:
        for db in dbs:
            if db not in tables:
                db_tables = isp.get_table_names(schema=db)
                tables.extend([{"db": db, "table": t, "columns": []} for t in db_tables])
    else:
        for db in dbs:
            if db not in tables:
                db_tables = isp.get_table_names(schema=db)
                tables.extend([{"db": db, "table": t, "columns": []} for t in db_tables if t in table_names])
    for t in tables:
        t["columns"] = isp.get_columns(t.get("table"), schema=t.get("db"))
        table_class_str = f"""\n\nclass {to_upper_camel_case(t.get("table"))}(Base):\n    __tablename__ = '{t.get("table")}'\n\n"""
        metadata = MetaData()
        metadata.reflect(bind=engine, schema=t.get("db"), only=[t.get("table")])
        base = automap_base(metadata=metadata)
        base.prepare()

        # ow就是overwatch表对应的内
        ow = getattr(base.classes, t.get("table"))
        # 获取主键
        primary_key = inspect(ow).primary_key
        primary_key_names = []
        if primary_key:
            for pk in primary_key:
                primary_key_names.append(pk.name)

        for column in t["columns"]:
            if column.get("name") in primary_key_names:
                column["primary_key"] = True
            field_type = column.get("type")
            if field_type:
                field_module = field_type.__class__.__module__
                field_class_name = field_type.__class__.__name__
                if field_module not in packages:
                    packages[field_module] = []
                if field_class_name not in packages[field_module]:
                    packages[field_module].append(field_class_name)
            if "type" in column:
                column["type_"] = column.pop("type")
            table_class_str += f"    {column.get('name')} = Column({dict2params_str(column)})\n"
        t["class_model"] = table_class_str

    file_content = "# coding: utf-8\nfrom sqlalchemy.ext.declarative import declarative_base\n" \
                   "from sqlalchemy import Column\n"
    for p, c in packages.items():
        file_content += f'from {p} import {", ".join(c)}\n'
    file_content += "\nBase = declarative_base()\n"
    for t in tables:
        file_content += t.get("class_model")
    if file:
        with open(file, "w+") as f:
            f.write(file_content)
    else:
        print(file_content)
