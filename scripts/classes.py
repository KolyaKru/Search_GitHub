from os import path
from sqlite3 import connect
from github import Github
import webbrowser
import requests
import pyodbc

class Git:

    def getrepos(self, name_user):
        try:
            git = Github('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')
            user = git.get_user(name_user)
            repos= user.get_repos()
            return repos
        except:
            print('Ошибка!')
    
    def getinforepos(self, repo):
        try:
            info = {}
            info = {
                    'name' : repo.name,
                    'owner': repo.owner.login,
                    'description' : repo.description,
                    'date_created' : str(repo.created_at),
                    'date_push' : str(repo.pushed_at),
                    'homepage' : repo.homepage,
                    'language' : repo.language,
                    'url' : 'https://github.com/' + repo.full_name
                }

            if (info['homepage'] == None):
                info['homepage'] = '-'
            if (info['description'] == None):
                info['description'] = '-'

            return info
        except:
            print('Ошибка!')
    
    def getnamerepos(self, name_repos):
        try:
            git = Github('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')
            repos = git.search_repositories(name_repos)
            return repos
        except:
            print('Ошибка!')
    

    def downloadrepo(self, repo):
        try:
            branches = repo.get_branches()
            for branch in branches:
                url = 'https://github.com/' + repo.full_name + "/zipball/" + branch.name
                webbrowser.open(url)
        except:
            print('Ошибка!')
    
    def switch(self, repo):
        try:
            url = 'https://github.com/' + repo.full_name
            webbrowser.open(url)
        except:
            print('Ошибка!')

class Sql:  

    def insertdb(self, repo):

        connect = pyodbc.connect('DRIVER={SQL Server};'
                                    'SERVER=DEVIL_MACHINE;'
                                    'DATABASE=GitHub;')

        cursor = connect.cursor()
        
        cursor.execute(f"INSERT INTO Repositories (Name, Owner, Description, Date_created, Date_push, Homepage, Language, Url) " +
                       f"VALUES ('{repo.name}', '{repo.owner.login}', '{repo.description}', " + 
                       f"CONVERT(smalldatetime, '{str(repo.created_at)}', 121), CONVERT(smalldatetime, '{str(repo.pushed_at)}', 121), " +
                       f"'{repo.homepage}', '{repo.language}', 'https://github.com/{repo.full_name}')")
        
        connect.commit()
        connect.close()