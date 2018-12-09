#!/usr/bin/python
import sys
import re

inputfileName = ""
outputFileName = ""

if len(sys.argv) > 1:
    inputfileName = sys.argv[1]
else:
    inputfileName = "gao.html"

if len(sys.argv) > 2:
    outputFileName = sys.argv[2]
else:
    outputFileName = inputfileName + "-parsed.txt"; 


def get_value(expression, content) :
    cleanContent = re.sub("\r\n|\n", r" ", content)
    cleanContent = re.sub(' +',' ', cleanContent)
    rexp= re.compile(expression, re.DOTALL)
    found= rexp.search(cleanContent)
    print("name:") 
    print(found)
    if found :
        return found.group(0).strip()
    return ""

def read_name(content) :
    return get_value(r"(?<=\<li\sclass=\"current\"\>)(.*?)(?=\</li\>)", content)

def read_email(content) :
    return get_value(r"(?<=\<li class=\"current\"\>)(.*?)(?=\</li\>)", content)

def read_research(content) :
    return get_value(r"(?<=Research Interests\s\</h3\>\s\</div\>\s\<div\sclass=\"panel-body\"\>\s\<p\>)(.*?)(?=\</p\>\</div\>)", content)

def read_education(content) :
    return get_value(r"(?<=Education\</h3\>\s</div\>\s\<div\sclass=\"panel-body\"\>\<p\>)(.*?)(?=\</p\>\</div\>)", content)

def read_webpage(content) : 
    return get_value(r"(?<=\<a)(.*?)(?=\>Homepage\</a\>)", content)

def read_values() :
    #first read our input file
    inputFile= open(inputfileName,"r")
    inputContent= inputFile.read()
    
    if len(inputContent) > 0:
        return read_name(inputContent), read_education(inputContent), read_research(inputContent), read_email(inputContent), read_webpage(inputContent)

    return "", "", "", "", ""

def write_values(name, education, research, email, webpage):
    # create the output file 
    outputFile= open(outputFileName,"w")
    nameFieldPrefix = "Name:"
    educationFieldPrefix = "Education:"
    researchFieldPrefix = "Research interests:"
    emailFieldPrefix = "Email:"
    webpageFieldPrefix = "Webpage:"

    outputFile.write(nameFieldPrefix + name)
    outputFile.write("\n")
    outputFile.write(educationFieldPrefix + education)
    outputFile.write("\n")
    outputFile.write(researchFieldPrefix + research)
    outputFile.write("\n")
    outputFile.write(emailFieldPrefix + email)
    outputFile.write("\n")
    outputFile.write(webpageFieldPrefix + webpage)

    outputFile.close()

#fields
name, education, research, email, webpage = read_values()
#write results
write_values(name, education, research, email, webpage)




