from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

ssl_args = {'ssl': {'ssl_ca': 'ca-certificate.crt'}}
SQL_ADDRESS = 'mysql+pymysql://gate:AVNS_e2qSpDJ9xrH7tVV-wfn@testing-do-user-11495581-0.b.db.ondigitalocean.com:25060/gate?charset=utf8mb4'

engine = create_engine(SQL_ADDRESS, connect_args=ssl_args)

Session = sessionmaker(bind=engine)

Base = declarative_base()
