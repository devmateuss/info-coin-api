from pydantic import Field
from pydantic_settings import BaseSettings


class AplicationSettings(BaseSettings):
    database_url: str = Field(
        env='DATABASE_URL' ,
        default='postgresql://admin:admin@db:5432/mercadobitcoin_db'
    )
    secret_key: str = Field(env='SECRET_KEY')
    jwt_expire_minutes: int = Field(env='JWT_EXPIRE_MINUTES', default=60)


aplication_settings = AplicationSettings()

