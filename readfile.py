# -*- encoding: utf-8 -*-

class filecls(object):
	#实例化类，并且加上classmethod的方法 才能被其他文本调用
	@classmethod     
	def readfilerobot(self,url):
		self.url = url
		try:
			file_read = open(self.url,'r',encoding='utf-8')
			file_read_contests = file_read.readlines() 
			file_read.close()
		except UnicodeDecodeError:
			file_read = open(self.url,'r')
			file_read_contests = file_read.readlines() 
			file_read.close()
		return file_read_contests
		
	@classmethod 
	def writefilerobot(self,listlines):
		self.listlines = listlines
		file_write = open("元素层.txt",'w',encoding='utf-8')
		list_write = []		
		for contests in self.listlines:
			print(contests)
			if contests== "*** Test Cases ***\n":
				contests = "*** Keywords ***\n"
			
			if "##" in contests :		
				list_guanjianzi = contests.split("##")
				if  list_guanjianzi[0] == " ":
					list_write.append(list_guanjianzi[0]+"\n")
				

				list_yuansu = list_guanjianzi[1].split(",")
				print(list_yuansu)
				list_write.append("\n"+list_yuansu[0]+"\n")
			
				if list_yuansu[1] != "/":
					list_write.append("    [Arguments]\t"+list_yuansu[1]+"\n")
		
				if list_yuansu[2] != "/\n":
					list_write.append("    [Return]\t"+list_yuansu[2])
				
				contests = ""
				list_write.append(contests)
					
			list_write.append(contests)
		
		file_write.writelines(list_write)	
	
		file_write.close()
		
	@classmethod 
	def writeymfilerobot(self,listlines):
		self.listlines = listlines
		file_write = open("页面层.txt",'w',encoding='utf-8')
		list_write = []	
		j = 0	
		for contests in self.listlines:		
			if contests== "*** Settings ***\n":
				list_write.append(contests+"\n"+"\n")
			
			if contests == "*** Test Cases ***\n":
				contests = "*** Keywords ***\n"
				list_write.append(contests)
				contests_next = self.listlines[j+1]
				list_write.append(contests_next)
			
			if "##" in contests:
				list_guanjianzi = contests.split("##")
				
				#list_guanjianzi[1] = "关键字	${a}	${b}\n"	
				list_yuansu = list_guanjianzi[1].split(",")
				#list_yuansu = ["关键字"，"${a}","${b}\n"]
				if list_yuansu[1] != "/" and list_yuansu[2] != "/\n":
						list_yuansu_re = list_yuansu[2].split("\n")
						list_write.append("    "+list_yuansu_re[0]+"\t"+list_yuansu[0]+"\t"+list_yuansu[1]+"\n")
					
				if list_yuansu[1] != "/" and list_yuansu[2] == "/\n":
						list_write.append("    "+list_yuansu[0]+"\t"+list_yuansu[1]+"\n")
				
				if list_yuansu[1] == "/" and list_yuansu[2] != "/\n":
						list_yuansu_re = list_yuansu[2].split("\n")
						list_write.append("    "+list_yuansu_re[0]+"\t"+list_yuansu[0]+"\n")
				
				if list_yuansu[1] == "/" and list_yuansu[2] == "/\n":
						list_write.append("    "+list_yuansu[0]+"\n")
			j = j+1
		
		file_write.writelines(list_write)	
	
		file_write.close()