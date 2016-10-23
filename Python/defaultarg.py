import sys
#Playing with Default and Variable Order and Number of arguments.Variable Number of Arguments are also discussed in one more program.Here arguments are not actually variable because we are implicitly using default arguments

def sex_movie(performer='Iona Grace',genre='BDSM',company='Infernal Restraints',movie='Subject 146'):
	print("The best AVN performer year of the award goes to "+performer+" for",movie+" by",company,"in genre",genre)
sex_movie()
sex_movie("Sunny Leone","Hardcore","Sunny Leone Productions","Virginity Hit")
sex_movie(genre='Hardcore')