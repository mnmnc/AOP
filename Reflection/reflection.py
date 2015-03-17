import random

class Reflected():
	"""
	Class that is being filled by reflection.
	"""
	angle = ''
	source = ''
	surface = ''
	absorption = ''


class Mirror():
	"""
	Class that is performing reflection.
	Checks the type of passed argument, and acts accordingly.
	"""
	@staticmethod
	def reflect(reflected, reflection_props):
		if reflection_props is not None:

			# IF INT RECEIVED
			if type(reflection_props) is int:

				print('Connection to database')
				database_data = {
					'angle': random.randint(0, 360) / reflection_props,
					'source': 'Moon',
					'surface': 'wood',
					'absorption': 90
				}
				print('Elements read from database:')
				for key in database_data.keys():
					print('\t', key, ':\t', database_data[key] )

				for element in dir(reflected):
					attribute = getattr(reflected.__class__, element)
					if not callable(attribute) and element.find('__') != 0 and element in database_data.keys():
						setattr(reflected, element, database_data[element])

			# IF DICTIONARY RECEIVED
			elif type(reflection_props) is dict:
				for element in dir(reflected):
					attribute = getattr(reflected.__class__, element)
					if not callable(attribute) and element.find('__') != 0 and element in reflection_props.keys():
						setattr(reflected, element, reflection_props[element])

			else:
				print('Data type unrecognized. Unable to fill the object.')
		else:
			print('Unable to fill the object. Missing properties.')


def main():

	random.seed()
	ref = Reflected()

	dic = {'angle' : 76, 'source': 'Sun', 'surface': 'glossy', 'absorption': 40}

	# Make first reflection
	Mirror.reflect(ref, dic)

	# Show results
	print(ref.__dict__)

	# Make second reflection
	Mirror.reflect(ref, 3)

	# Show results
	print(ref.__dict__)

if __name__ == '__main__':
	main()


