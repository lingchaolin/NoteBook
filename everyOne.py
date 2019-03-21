# -*- coding: utf-8 -*- 

import os
import os.path
import time

class java2md():
	strList = []
	strList.append(".git")
	strList.append(".idea")
	strList.append(".log.")
	strList.append("logs")
	strList.append(".md")
	strList.append(".py")
	strList.append(".settings")
	strList.append(".svn")
	strList.append("target")
	strList.append(".classpath")
	strList.append(".project")
	strList.append(".py")

	outdir = ""
	def __init__(self,rootdir):
		self.rootdir=rootdir
		self.outdir = os.path.join(rootdir,"new.md")
	def containAny(self,string):#
		for c in self.strList:
			print(c,string)
			if c in string:
				return True
			else:
				continue
			return False
	#语言格式
	def languageMethod(self,string):
		if(".java" in string):
			return "java"
		elif(".xml" in string):
			return "xml"
		elif(".sql" in string):
			return "sql"
		elif(".xml" in string):
			return "xml"
		elif(".html" in string):
			return "html"
		elif(".css" in string):
			return "css"
		elif(".py" in string):
			return "python"
		elif(".js" in string):
			return "JavaScript"
		else:
			return "General"
	#复制粘贴文件
	def transferFile(self,filePath,filesup,language):
		with open(filePath,'r',encoding='UTF-8') as file_object:
			contents = file_object.read()
			with open(self.outdir,'a',encoding='UTF8') as file_out:
				file_out.write("\r\n")
				file_out.write("@toc")
				file_out.write("\r\n")
				file_out.write("### ")
				file_out.write(filesup)
				file_out.write("\r\n")
				file_out.write("```"+language)
				file_out.write("\r\n")
				file_out.write(contents)
				file_out.write("\r\n")
				file_out.write("```")
				file_out.write("\r\n")
		# with open(filePath,'r',encoding='UTF-8') as file_object:#一行一行检查
		# 	for line in file_object:
		# 		print(line)
	# 逻辑方法
	def run(self):
		for parent, dirnames, filename in os.walk(self.rootdir):
			for name in filename:
				newPath = os.path.join(parent,name)
				if(not self.containAny(newPath)):
					print(newPath,self.containAny(newPath))
					language = self.languageMethod(newPath)
					filesup = newPath.replace(rootdir,"")
					self.transferFile(newPath,filesup,language)
					# print(newPath.replace(rootdir,""))


# rootdir = 'D:\\ExtraApp\\GitData\\NewMybatis'
rootdir="D:\\Java\\IdeaProjects\\base\\common-core"
j = java2md(rootdir)
# print(j.containAny(".logs"))
# print(j.strList)
j.run()


