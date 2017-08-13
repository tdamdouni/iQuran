#!/usr/bin/python

#~~~~~~~~~~IN THE NAME OF ALLAH~~~~~~~~~~~

# A small and terminal base Quran application in 3 translations

# quran.py in 3 languages [arabic , english , persian]

        # quran.py                     This Help
        # quran.py -r                  Random Ayah
        # quran.py -a num1:num2        Ayah at num1:num2

# data are stored in non standard csv format with '|' delimiter

# quran files of translations have been downloaded from http://qurandatabase.org/

import random
import sys

class Quran:

	def q_load(self,q_dict_path):
		self._q_lst=[]
		self.q_dict_path=q_dict_path
		
		for path in q_dict_path.values():
			q_file=open(path,'r')
			self._q_lst.insert(0, q_file.readlines())
			
			
			
	def q_random_ayah(self):
		rnd = random.randint(0,len(self._q_lst[0]))
		return(self.q_gen_output(rnd))
		
		
		
	def q_index(self,location):
		i=0
		for line in self._q_lst[0]:
			if line.startswith(location):
				return self.q_gen_output(i)
			i=i+1
		return 'sorry no result !'
		
		
		
	def q_gen_output(self,line):
		output=''
		i=len(self._q_lst)-1
		for q_file in self._q_lst:
			output = output+ '\n\n' + self.q_dict_path.keys()[i] + '\n' + q_file[line]
			i = i - 1
			
		return output
		
		
		
	def q_size(self):
		return len(self._q_lst[0])
		
		
	def q_slice(self,ayah):
		pass
		
		
		
if __name__=='__main__' :
	quran = Quran()
	quran.q_load({'Persian':'file/persian.csv','English':'file/english.csv','Arabic':'file/arabic.csv'})
	
	output = ''
	
	if len(sys.argv)>2 and sys.argv[1] == '-a':
		if sys.argv[2] != None :
			location = sys.argv[2].replace(":","|")
			output = quran.q_index(location)
			
			
	if len(sys.argv)>1 and sys.argv[1] == '-r':
		output = quran.q_random_ayah()
		
		
		
	if len(output) < 1 :
		output ='''
		quran.py in 3 languages [arabic , english , persian]
		
		quran.py                        This Help
		quran.py -r                     Random Ayah
		quran.py -a num1:num2           Ayah at num1:num2
		
		
		'''
		
print(output)

