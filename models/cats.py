
from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String
from config.db import meta, engine

baseCat = Table("cats", meta, 
                        Column("id", Integer, primary_key=True, autoincrement=True),
                        Column("catName", String(200)),
                        Column("catRace", String(100)),
                        Column("catYear", Integer),
                        Column("catImg", String(255))
            )

meta.create_all(engine)
