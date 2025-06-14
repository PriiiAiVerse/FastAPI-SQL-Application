#from jupyter_client.session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
#from tf_keras.src.backend import SessionLocal

URL_DATABASE = 'mysql+pymysql://root:123456@localhost:3306/BlogApplication'

engine = create_engine(URL_DATABASE)

SessionLocal =sessionmaker(autocommit=False, autoflush=False, bind = engine)

Base = declarative_base()



