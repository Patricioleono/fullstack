from sqlalchemy import MetaData, create_engine


engine = create_engine("mysql+pymysql://root:patricio1992@localhost:3306/prueba_tecnica")
meta = MetaData()
conn = engine.begin() #probar con connect

