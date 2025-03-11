from config import db
import config as cf

def get_all_buildings():
    query = (
        db.session.query(
            Building.title.label("Здание"),
            TypeBuilding.name.label("Тип"),
            Country.name.label("Страна"),
            City.name.label("Город"),
            Building.year.label("Год"),
            Building.height.label("Высота")
          )
        .select_from(Building)
        .join(TypeBuilding)
        .join(City)
        .join(Country)
    )
    return [query.statement.columns.keys(), query.all()]

class Country(db.Model):
    __tablename__ = 'Country'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    cities = db.relationship("City", back_populates="country", cascade='all, delete')

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        query = Country.query.all()
        for item in query:
            row = "id: {}, name: {}".format(item.id, item.name)
            return row

class TypeBuilding(db.Model):
    __tablename__ = 'TypeBuilding'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    type = db.Column(db.String(50), nullable=False)
    buildings = db.relationship("Building", back_populates="type_building", cascade='all, delete')

    def __init__(self, type):
        self.type = type

    def __repr__(self):
        query = TypeBuilding.query.all()
        for item in query:
            row = "id: {}, type: {}".format(item.id, item.type)
            return row

class City(db.Model):
    __tablename__ = 'City'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    country_id = db.Column(db.Integer, db.ForeignKey('Country.id'))
    country = db.relationship("Country", back_populates="cities")
    buildings = db.relationship("Building", back_populates="city", cascade='all, delete')

    def __init__(self, name, country_id):
        self.name = name
        self.country_id = country_id

    def __repr__(self):
        query = City.query.all()
        for item in query:
            row = "id: {}, name: {}, type: {}".format(item.id, item.name, item.country_id)
            return row

class Building(db.Model):
    __tablename__ = 'Building'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200))
    type_building_id = db.Column(db.Integer, db.ForeignKey('TypeBuilding.id'))
    city_id = db.Column(db.Integer, db.ForeignKey('City.id'))
    year = db.Column(db.Integer)
    height = db.Column(db.Integer)

    type_building = db.relationship("TypeBuilding", back_populates="buildings")
    city = db.relationship("City", back_populates="buildings")

    def __init__(self, title, type_building_id, city_id, year, height):
        self.title = title
        self.type_building_id = type_building_id
        self.city_id = city_id
        self.year = year
        self.height = height
    def __repr__(self):
        query = Building.query.all()
        for item in query:
            query = Building.query.all()
            for item in query:
                row = ("id: {}, title: {}, type_building_id: {}, city_id: {}, year: {}, height: {}".
                       format(item.id, item.title, item.type_building_id, item.city_id, item.year, item.height))
                return row

cf.app.app_context().push()
with cf.app.app_context():
    db.create_all()
