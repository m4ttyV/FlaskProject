from app import db

def get_all_buildings():
    query = (
        db.session.query(
            Building.title.label("Здание"),
            TypeBuilding.type.label("Тип"),
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
    cities = db.relationship("City", back_populates="country")
    def __init__(self, name):
        self.name = name

class TypeBuilding(db.Model):
    __tablename__ = 'TypeBuilding'
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(50), nullable=False)
    buildings = db.relationship("Building", cascade='all, delete')
    def __init__(self, type):
        self.type = type
    def __repr__(self):
        return f"\n{self.id}. {self.type}"

class City(db.Model):
    __tablename__ = 'City'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    country_id = db.Column(db.Integer, db.ForeignKey("Country.id"))
    country = db.relationship("Country", back_populates="cities")
    buildings = db.relationship("Building", cascade='all, delete')
    def __init__(self, name, country_id):
        self.name = name
        self.country_id = country_id

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

# db.app_context().push()
#
# with db.app_context():
#     db.create_all()