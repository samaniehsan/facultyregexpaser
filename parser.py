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


def read_name(content) :
    cleanContent = re.sub("\r\n|\n", r" ", content)
    cleanContent = re.sub(' +',' ', cleanContent)
    rexp= re.compile(r"(?<=\<li\sclass=\"current\"\>)(.*?)(?=\</li\>)", re.DOTALL)
    found= rexp.search(cleanContent)
    if found :
        return found.group(0).strip()
    return ""

def read_email(content) :
    cleanContent = re.sub("\r\n|\n", r" ", content)
    cleanContent = re.sub(' +',' ', cleanContent)
    username = ""
    domain = ""
    rexp= re.compile(r"(?<=email_image/\?user=)(.*?)(?=&)", re.DOTALL)
    usernameGroup= rexp.search(cleanContent)
    
    if usernameGroup :
        username = usernameGroup.group(0)

    rexp2= re.compile(r"(?<=domain=)(.*?)(?=&)", re.DOTALL)
    domainGroup= rexp2.search(cleanContent)

    if domainGroup :
        domain = domainGroup.group(0)

    return username + "@" + domain

def read_research(content) :
    cleanContent = re.sub("\r\n|\n", r" ", content)
    cleanContent = re.sub(' +',' ', cleanContent)
    rexp= re.compile(r"(?<=Research Interests)(.*?)(?=\</p\>)", re.DOTALL)
    found= rexp.search(cleanContent)
    if found :
        uncleanContent = found.group(0)
        rexp2= re.compile(r"(?<=\<p\>)(.*)", re.DOTALL)
        found2= rexp2.search(uncleanContent)
        if found2 :
            return found2.group(0)
    return ""

def read_education(content) :
    cleanContent = re.sub("\r\n|\n", r" ", content)
    cleanContent = re.sub(' +',' ', cleanContent)
    rexp= re.compile(r"(?<=Education)(.*?)(?=\</p\>)", re.DOTALL)
    found= rexp.search(cleanContent)
    if found :
        uncleanContent = found.group(0)
        rexp2= re.compile(r"(?<=\<p\>)(.*)", re.DOTALL)
        found2= rexp2.search(uncleanContent)
        if found2 :
            return found2.group(0)
    return ""

def read_webpage(content) :
    cleanContent = re.sub("\r\n|\n", r" ", content)
    cleanContent = re.sub(' +',' ', cleanContent)
    rexp= re.compile(r"(?<=\<small>)(.*?).(?=Homepage)", re.DOTALL)
    found= rexp.search(cleanContent)
    if found :
        uncleanContent = found.group(0)
        print("webpage:" + uncleanContent)
        rexp2= re.compile(r"(?<=href)(.*?)(?=\>)", re.DOTALL)
        found2= rexp2.search(uncleanContent)
        if found2 :
            uncleanContent3= found2.group(0)
            rexp3= re.compile(r"(?<=\")(.*?)(?=\")", re.DOTALL)
            found3= rexp3.search(uncleanContent3)
            if found3:
                return found3.group(0)
    return ""

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




