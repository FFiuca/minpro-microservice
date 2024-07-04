import factory
from factory import django
from faker import Faker
from faker.providers import address, person, lorem
from search.mongo_docs import Manga
import random
import numpy

fake = Faker()
fake.add_provider(address)
fake.add_provider(person)
fake.add_provider(lorem)

class MangaFactory(factory.mongoengine.MongoEngineFactory):
    class Meta:
        model = Manga

    @staticmethod
    def generate_rating(obj):
        rating = random.random()
        if rating>0.5:
            rating-= 0.5

        return rating* 10

    @staticmethod
    def generate_author(obj):
        fn = [
            fake.name,
            # fake.kana_name,
            # fake.last_name_islamic,
            # fake.last_name_hinduism,
            # fake.romanized_name,
        ]
        count = len(fn)-1

        res = [fn[random.randint(0, count)]() for i in range(0, random.randint(1, 3))]
        return res

    @staticmethod
    def generate_genre(obj):
        manga_genres = [
            "Action",
            "Adventure",
            "Comedy",
            "Drama",
            "Fantasy",
            "Historical",
            "Horror",
            "Isekai",
            "Josei",
            "Magic",
            "Martial Arts",
            "Mecha",
            "Mystery",
            "Psychological",
            "Romance",
            "School Life",
            "Sci-Fi",
            "Seinen",
            "Shoujo",
            "Shoujo Ai",
            "Shounen",
            "Shounen Ai",
            "Slice of Life",
            "Sports",
            "Supernatural",
            "Tragedy",
            "Vampire",
            "Yaoi",
            "Yuri"
        ]
        count = len(manga_genres)

        res = [manga_genres[random.randint(0, count-1)] for i in range(0, random.randint(0,5))]
        res = numpy.unique(numpy.array(res)).tolist()

        return res

    @staticmethod
    def generate_theme(obj):
        manga_themes = [
            "Aliens",
            "Cyberpunk",
            "Demons",
            "Detective",
            "Game",
            "Harem",
            "High Fantasy",
            "Historical",
            "Idols (Male)",
            "Idols (Female)",
            "Military",
            "Music",
            "Ninja",
            "Office Workers",
            "Police",
            "Post-Apocalyptic",
            "Reincarnation",
            "Samurai",
            "School",
            "Space",
            "Super Power",
            "Survival",
            "Time Travel",
            "Vampire",
            "Villainess"
        ]
        count = len(manga_themes)

        res = [manga_themes[random.randint(0, count-1)] for i in range(0, random.randint(0,5))]
        res = numpy.unique(numpy.array(res)).tolist()

        return res

    @staticmethod
    def generate_demographic(obj):
        manga_demographics = [
            "Children",
            "Shounen (Young Boys)",
            "Shoujo (Young Girls)",
            "Seinen (Adult Men)",
            "Josei (Adult Women)"
        ]
        count = len(manga_demographics)

        res = [manga_demographics[random.randint(0, count-1)] for i in range(0, random.randint(0,5))]
        res = numpy.unique(numpy.array(res)).tolist()

        return res

    @staticmethod
    def generate_language(obj):
        manga_languages = [
            "Japanese",
            "English",
            "Chinese",
            "Korean",
            "Spanish",
            "French",
            "German",
            "Italian",
            "Portuguese",
            "Russian",
            "Thai",
            "Vietnamese",
            "Indonesian",
            "Malay",
            "Tagalog"
        ]
        count = len(manga_languages)

        res = [manga_languages[random.randint(0, count-1)] for i in range(0, random.randint(0,5))]
        res = numpy.unique(numpy.array(res)).tolist()

        return res

    @staticmethod
    def generate_tag(obj):
        res = []
        for i in range(0, random.randint(0,10)):
            res.append({
                'key': fake.word(),
                'value': fake.word()
            })

        return res

    title = factory.Sequence(lambda obj: fake.sentence())
    rating = factory.LazyAttribute(generate_rating)
    bookmark_count = factory.LazyAttribute(lambda obj: random.randrange(0, 99999))
    view = factory.LazyAttribute(lambda obj: random.randrange(0, 99999))
    author = factory.LazyAttribute(generate_author)
    artist = factory.LazyAttribute(generate_author)
    genre = factory.LazyAttribute(generate_genre)
    theme = factory.LazyAttribute(generate_theme)
    demographic = factory.LazyAttribute(generate_demographic)
    track = None
    alternative_title = factory.LazyAttribute(lambda obj: [fake.name() for i in range(0, random.randint(0,5))])
    language = factory.LazyAttribute(generate_language)
    tag = factory.LazyAttribute(generate_tag)



