from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Configuração do banco de dados
DATABASE_URL = "sqlite:///tweets.db"

engine = create_engine(DATABASE_URL)
Base = declarative_base()

# Modelo de dados
class Tweet(Base):
    __tablename__ = 'tweets'
    id = Column(Integer, primary_key=True, autoincrement=True)
    created_at = Column(DateTime)
    user = Column(String)
    text = Column(String)

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

def store_tweets(tweet_data):
    for tweet in tweet_data:
        tweet_record = Tweet(created_at=tweet[0], user=tweet[1], text=tweet[2])
        session.add(tweet_record)
    session.commit()
