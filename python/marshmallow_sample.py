from marshmallow import Schema, fields, post_load, validates, ValidationError
from marshmallow.validate import Range
import datetime
from pprint import pprint

"""
以下のような形式にする
{
  name: str(必須),
  age: int(デフォルト:10)(0<=age<=100)
  email: email
  body_data: {
    weight:float
    height:float
  }
  json:{
    key1: str
    key2: str:
    key3: [
      {
        sub_key1:bool(必須)
        subkey:float
      }
    ]
  }
  updated:datetime
}
"""


class SubJsonSchema(Schema):
  sub_key1 = fields.Bool(required=True,error_messages={"required":"this is required."})
  sub_key2 = fields.Float()
  
class JsonSchema(Schema):
  key1 = fields.Str()
  key2 = fields.Int()
  key3 = fields.List(fields.Nested(SubJsonSchema))
  
class BodyDataSchema(Schema):
  height = fields.Float()
  weight = fields.Float()

class UserSchema(Schema):
  name = fields.Str(required=True, error_messages={"required":"name is required."})
  age = fields.Int(load_default=10)
  email = fields.Email()
  body_data = fields.Nested(BodyDataSchema)
  json = fields.Nested(JsonSchema)
  updated=fields.DateTime()

  
  @validates("age")
  def validate_age(self, value):
    if value < 0:
      raise ValidationError("age must be greater than 0.")
    if value > 100:
      raise ValidationError("age must not be greater than 100.")

data = dict(
  name="tanaka",
  age=-20,
  email = "test@test.com",
  body_data = dict(
    height = 170.1,
    weight = 64.4
  ),
  updated="2020-01-11T05:26:03.869245",
  json = dict(
    key1="value1",
    key2=2,
    key3=[
      dict(
        sub_key1 = True,
        sub_key2 = 10.1
      ),
      dict(
        sub_key1 = True,
      ),
      dict(
        sub_key2= 1.1
      ),
      dict(
        sub_key1 = "test",
        sub_key2 = 100.2
      )
    ]
  )
)

schema = UserSchema()
result3 = schema.validate(data)
#print(result3)
# {'json': {'key3': {2: {'sub_key1': ['this is required.']}, 3: {'sub_key1': ['Not a valid boolean.']}}}, 'age': ['age must be greater than 0.']}
class ValidateTestSchema(Schema):
  value = fields.Str(required=True)
  test = fields.Str()
  @validates("value")
  def validate_value(self, value):
    if not "-" in value:
      raise ValidationError("must be contained '-'.")
  
schema = ValidateTestSchema()
data = {"value":"tst-1"}
#print(schema.load(data,partial=True))

data = {"test":"test"}
#print(schema.load(data,partial=True))


""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

class SubSchema(Schema):
  key1 = fields.String(required=True)
  key2 = fields.String(required=True)
  
class MainSchema(SubSchema):
  key3 = fields.String(required=True)
  key4 = fields.Integer(allow_none=True,validate=Range(min=-1,max=0))
  
  
sub_data = {"key1":"value1","key2":"value2"}
main_data1 = {"key1":"value1","key2":"value2","key3":"value3"}
main_data2 = {"key1":"","key2":"value2","key3":"value3","key4":-2}
sub_schema = SubSchema()
main_schema = MainSchema()

print(sub_schema.load(sub_data))
print(sub_schema.load(main_data1))
print(sub_schema.load(main_data2))
print(main_schema.load(sub_data))
print(main_schema.load(main_data1))
print(main_schema.load(main_data2))