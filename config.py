import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", 'postgresql://briefs_user:B3nDmCciukKnNVVFTLV1Ud4sBWpxZrF8@dpg-cuq8ie1u0jms73bv33ag-a.frankfurt-postgres.render.com/briefs')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True


