from marshmallow import Schema, fields


class ItemSchema(Schema):
    id = fields.Str(dump_only=True)
    name = fields.Str(dump_only=True)
    price = fields.Float(required=True)
    store_id = fields.Str(required=True)


class ItemUpdateSchema(Schema):
    name = fields.Str(dump_only=True)
    price = fields.Float(required=True)


class StoreSchema(Schema):
    id = fields.Str(dump_only=True)
    name = fields.Str(dump_only=True)
