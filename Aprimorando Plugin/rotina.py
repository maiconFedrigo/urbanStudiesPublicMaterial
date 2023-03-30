IN = [
	[
		"L-001",
		"L-002"
	],
	[
		[(-48.384869, -27.607316), (-48.382694, -27.607851), (-48.386541, -27.612488),(-48.388294,-27.611534)],
		[(-48.389993, -27.610140), (-48.389176, -27.610112), (-48.389128, -27.610790),(-48.389966,-27.610734)]
	]
]


def generate_coordinate_line(coordinates):
	result = ""
	for i in coordinates:
		result = result + f"            [{i[0]}, {i[1]}],\n"
	result = result + f"            [{coordinates[0][0]}, {coordinates[0][1]}],\n"
	result = result[:-2]
	return result


def generate_polygon(name, coordinates):
	result = ""

	result = result + '''   {
      "type": "Feature",
      "geometry": {
        "type": "Polygon",
        "coordinates": [
          ['''

	result = result + "\n" + generate_coordinate_line(coordinates) + "\n"
	result = result + '''          ]
        ]
      },'''

	result = result + '''      "properties": {
        "Name": "@@@"
      },
      "id": "@@@"
    },'''.replace("@@@", name)
	return result


NAMES = IN[0]
POINTS = IN[1]

starter_line = '''{"type" : "FeatureCollection","features": ['''
end_of_json = ''']}'''

content = starter_line

for n,p in zip(NAMES,POINTS):
	content = content + generate_polygon(n,p) + "\n"

content_comma_correction = content[:-2] + "\n"

final_completion = content_comma_correction + end_of_json


print(final_completion)