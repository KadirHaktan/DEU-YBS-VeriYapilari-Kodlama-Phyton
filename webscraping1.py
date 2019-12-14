
import urllib.request as request
from bs4 import BeautifulSoup


##Import to required libraries


gitHub_Source=request.urlopen("https://github.com/trending").read()
gitHub_Soup=BeautifulSoup(gitHub_Source,'lxml')
##request url and read to requested url.After all create the Beautiful Soup instance and Beautiful Soup constructor needs to
##two paramters.First parameter is **read url** and **taking html tags formats=>lxml**


articles=gitHub_Soup.find_all("article")

#Find to all article tags

for article in articles:
        try:
            articleName=article.find('h1').text.split()
            articleProgrammingLanguages=article.find('span',attrs={'itemprop':'programmingLanguage'}).text.split()
            RepoCreator=articleName[0].strip()
            RepoName=articleName[2].strip()
            RepoProgrammingLanguage=articleProgrammingLanguages[0].strip()
            print("Repo Creator:"+RepoCreator)
            print("Repo Name:  "+RepoName)
            print("Repo Programming Language: "+RepoProgrammingLanguage)
            print("")
            
        except:
            print("Repo Programming Language:None")
            print("")
            pass

#I wrote the try and except blocks.Because some data can be null.Asspecialy repo programming language can be null.So null
##variable can throw exception from these program and program can work badly.So ı had to took precaution




    
    
        
    


    
    
    

    
    

