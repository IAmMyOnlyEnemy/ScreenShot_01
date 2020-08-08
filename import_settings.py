import pathlib
from os import path

def get_settings():
	''' ---------------
	Global values:
	    --------------- '''
	global settings_dict
	settings_dict = {}
	global file_name
	file_name = "Settings\\settings.txt"

	''' ---------------
	Fill the input file if there is none:
	    --------------- '''
	if not path.exists(file_name):
		fill_file()
	''' ---------------
	Filling the dictionary values from input file:
	    --------------- '''
	fill_dict()

	''' ---------------
	Return the seeting dictionary:
	    --------------- '''
	#print(settings_dict)
	return settings_dict

def fill_dict():
	file1 = open(file_name,'r')
	lines = file1.read().splitlines()
	for line in lines:
		dict_key = line.split(": ")[0]
		dict_value = line.split(": ")[1].split(", ")

		for idx, val in enumerate(dict_value):
			try:
				int(val)
				dict_value[idx] = int(val)
			except ValueError:
				pass

		settings_dict.update({dict_key : dict_value})
	file1.close()

def fill_file():
	file1 = open(file_name,'w')
	file1.writelines("TSO_dimmension: 450, 950\n")
	file1.writelines("CICS_dimmension: 600, 950\n")
	file1.writelines("TSO_option: CICS\n")
	file1.writelines("screen_list: CONT, SAVE, TREC, TBLT, TREV\n")
	file1.writelines("save_path: {0}".format(pathlib.Path().absolute()))
	file1.close()

if __name__== "__main__":
	get_settings()