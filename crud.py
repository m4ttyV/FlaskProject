import csv
from app import db, app
from structures.models import TypeBuilding
from structures.models import Country, City, Building



def completed():
    with app.app_context():
        item = TypeBuilding('Небоскрёб')
        db.session.add(item)
        item = TypeBuilding('Антенная мачта')
        db.session.add(item)
        item = TypeBuilding('Радиомачта')
        db.session.add(item)
        item = TypeBuilding('Гиперболоидная башня')
        db.session.add(item)
        item = TypeBuilding('Дымовая труба')
        db.session.add(item)
        item = TypeBuilding('Решётчатая мачта')
        db.session.add(item)
        item = TypeBuilding('Башня')
        db.session.add(item)
        item = TypeBuilding('Мост')
        db.session.add(item)
        db.session.commit()
        ##############################################################################
        query = TypeBuilding.query.filter(TypeBuilding.type.ilike('%е%'), TypeBuilding.id > 3).all()
        for item in query:
            print(item.type)
        ##############################################################################
        country_upload()
        city_upload()
        building_upload()
        Country.__repr__(Country)
        Building.__repr__(Building)

def country_upload():
    with open("./data/country.csv") as f:
        reader = csv.reader(f)
        next(reader)
        for item in reader:
            new_entry = Country(item[0])
            db.session.add(new_entry)
        db.session.commit()

def city_upload():
    with open("./data/city.csv") as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            new_entry = City(row[0], row[1])
            db.session.add(new_entry)
        db.session.commit()

def building_upload():
    with open("./data/building.csv") as f:
        reader = csv.reader(f)
        next(reader)
        for item in reader:
            new_building = Building(item[0], item[1], item[2], item[3], item[4])
            db.session.add(new_building)
        db.session.commit()


# country_upload()
# city_upload()
# building_upload()
# Country.__repr__(Country)
# Building.__repr__(Building)
with app.app_context():
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
    db.select_from(Building)
    print(query.all())

