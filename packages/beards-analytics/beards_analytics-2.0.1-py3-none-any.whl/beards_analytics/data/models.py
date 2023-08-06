from datetime import date, datetime
import pydantic
import pendulum


class BaseModel(pydantic.BaseModel):
    @pydantic.validator('*', pre=True)
    def __v(cls, value, values, config, field: pydantic.fields.ModelField):
        if field.type_ in (date, datetime) and type(value) is str:
            value = datetime.fromtimestamp(pendulum.parser.parse(value).timestamp())
        
        return value
    
    class Config:
        json_encoders = {
            date: lambda dt: dt.isoformat()
        }
