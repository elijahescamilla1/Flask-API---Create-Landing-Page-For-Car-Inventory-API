import os

class Config:
    SECRET_KEY = os.getenv('Anaheim')
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres.bedlmcmwyjtgsnahdarh:Lifetime__20xqw@aws-0-us-west-1.pooler.supabase.com:6543/postgres'
    SQLALCHEMY_TRACK_MODIFICATIONS = False