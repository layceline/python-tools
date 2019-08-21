from fastkml import kml
from shapely.geometry import Point

if __name__ == '__main__':
    k = kml.KML()

    doc = kml.Document(description="My doc")
    k.append(doc)

    folder = kml.Folder(description="My folder")
    doc.append(folder)

    p = kml.Placemark()
    p.geometry = Point(0, 3)
    data = kml.Data(name="myField", value="123")
    data.__name__ = "myField"
    p.extended_data = data
    folder.append(p)

    print(k.to_string(prettyprint=True))
    with open("res.kml", "w") as file:
        file.write(k.to_string(prettyprint=True))
