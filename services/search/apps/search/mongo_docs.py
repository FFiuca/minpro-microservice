import mongoengine

# meta example : https://mangadex.org/title/c52b2ce3-7f95-469c-96b0-479524fb7a1a/jujutsu-kaisen?tab=chapters

class Chapter(mongoengine.EmbeddedDocument):
    title = mongoengine.StringField()
    uploader_id = mongoengine.StringField()
    uploader = mongoengine.StringField()
    created_at = mongoengine.DateTimeField()
    view = mongoengine.IntField()
    language = mongoengine.StringField()
    tags = mongoengine.ListField()

class TagBase(mongoengine.DynamicEmbeddedDocument):
    key = mongoengine.StringField()
    value = mongoengine.StringField()

    meta = {'allow_inheritance': True}

class TagManga(TagBase):
    pass

# use dynamic docs to can save with new field future
class Manga(mongoengine.DynamicDocument):
    title = mongoengine.StringField()
    rating = mongoengine.FloatField()
    bookmark_count = mongoengine.IntField()
    view = mongoengine.IntField()
    author = mongoengine.ListField()
    artist = mongoengine.ListField()
    genre = mongoengine.ListField()
    theme = mongoengine.ListField()
    demographic = mongoengine.ListField()
    track = mongoengine.ListField()
    alternative_title = mongoengine.ListField()
    language = mongoengine.ListField()
    tag = mongoengine.ListField(mongoengine.EmbeddedDocumentField(TagManga))


