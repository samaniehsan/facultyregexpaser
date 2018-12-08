#first read our input file
inputFile= open("gao.html","r")
inputContent= inputFile.read()
print(inputContent)
#fields
name= ""
education= ""
research= ""
email= ""
webpage= ""
# create the output file 
outputFile= open("gao-parsed.txt","w")

#write results

nameFieldPrefix = "Name:"
educationFieldPrefix = "Education:"
researchFieldPrefix = "Research interests:"
emailFieldPrefix = "Email:"
webpageFieldPrefix = "Webpage:"

outputFile.write(nameFieldPrefix + name)
outputFile.write(educationFieldPrefix + education)
outputFile.write(researchFieldPrefix + research)
outputFile.write(emailFieldPrefix + email)
outputFile.write(webpageFieldPrefix + webpage)
outputFile.close()
