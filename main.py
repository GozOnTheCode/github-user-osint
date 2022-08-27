import requests
import os
from tabulate import tabulate
import json
import hyperlink

os.system("cls")
os.system("title " + "☠️ M0NEGASQUE TOOLS ☠️")

print("This tool, developed by M0NEGASQUE, is a tool\nto retrieve information about a github account, easy\nto use tool !")
print('''
 ███▄ ▄███▓ ███▄    █ ▓█████   ▄████  ▄▄▄        ██████   █████   █    ██ ▓█████ 
▓██▒▀█▀ ██▒ ██ ▀█   █ ▓█   ▀  ██▒ ▀█▒▒████▄    ▒██    ▒ ▒██▓  ██▒ ██  ▓██▒▓█   ▀ 
▓██    ▓██░▓██  ▀█ ██▒▒███   ▒██░▄▄▄░▒██  ▀█▄  ░ ▓██▄   ▒██▒  ██░▓██  ▒██░▒███   
▒██    ▒██ ▓██▒  ▐▌██▒▒▓█  ▄ ░▓█  ██▓░██▄▄▄▄██   ▒   ██▒░██  █▀ ░▓▓█  ░██░▒▓█  ▄ 
▒██▒   ░██▒▒██░   ▓██░░▒████▒░▒▓███▀▒ ▓█   ▓██▒▒██████▒▒░▒███▒█▄ ▒▒█████▓ ░▒████▒
░ ▒░   ░  ░░ ▒░   ▒ ▒ ░░ ▒░ ░ ░▒   ▒  ▒▒   ▓▒█░▒ ▒▓▒ ▒ ░░░ ▒▒░ ▒ ░▒▓▒ ▒ ▒ ░░ ▒░ ░
░  ░      ░░ ░░   ░ ▒░ ░ ░  ░  ░   ░   ▒   ▒▒ ░░ ░▒  ░ ░ ░ ▒░  ░ ░░▒░ ░ ░  ░ ░  ░
░      ░      ░   ░ ░    ░   ░ ░   ░   ░   ▒   ░  ░  ░     ░   ░  ░░░ ░ ░    ░   
       ░            ░    ░  ░      ░       ░  ░      ░      ░       ░        ░  ░
                                                                                 
▄▄▄█████▓ ▒█████   ▒█████   ██▓      ██████                                      
▓  ██▒ ▓▒▒██▒  ██▒▒██▒  ██▒▓██▒    ▒██    ▒                                      
▒ ▓██░ ▒░▒██░  ██▒▒██░  ██▒▒██░    ░ ▓██▄                                        
░ ▓██▓ ░ ▒██   ██░▒██   ██░▒██░      ▒   ██▒                                     
  ▒██▒ ░ ░ ████▓▒░░ ████▓▒░░██████▒▒██████▒▒                                     
  ▒ ░░   ░ ▒░▒░▒░ ░ ▒░▒░▒░ ░ ▒░▓  ░▒ ▒▓▒ ▒ ░                                     
    ░      ░ ▒ ▒░   ░ ▒ ▒░ ░ ░ ▒  ░░ ░▒  ░ ░                                     
  ░      ░ ░ ░ ▒  ░ ░ ░ ▒    ░ ░   ░  ░  ░                                       
             ░ ░      ░ ░      ░  ░      ░                                       
                                                             ''')

while True:

    try:
        print("\n")
        user_demande = input("Enter github user : ")

        response = requests.get(f'https://api.github.com/users/{user_demande}')
        the_response = response.json()

        login_value = the_response['login']
        id_value = the_response['id']
        avatar_value = the_response['avatar_url']
        location_value = the_response['location']
        blog_value = the_response['blog']
        email_value = the_response['email']
        twitter_value = the_response['twitter_username']
        github_value = the_response['url']
        fullname_value = the_response['name']
        follower_value = the_response['followers']
        following_value = the_response['following']
        company_value = the_response['company']

        url = hyperlink.parse(f'{avatar_value}')
        better_url = url.replace(scheme=u'https', port=443)
        org_url = better_url.click(u'.')

        text_tableau = [
            {
                'Github Name',
                'Github Id',
                'Github Avatar'
            }
        ]

        value_tableau = [
            {
            login_value,
            id_value,
            avatar_value
            }
        ]

        for key,value in the_response.items():
            print("\n")
            print(tabulate([['Name', login_value],
             ['Id', id_value],
              ['Avatar', avatar_value],
               ['Location', location_value],
                ['Blog', blog_value],
                 ['Email', email_value],
                  ['Twitter', twitter_value],
                   ['Full Name', fullname_value]
                   , ['Followers', follower_value],
                    ['Followings', following_value],
                     ['Company', company_value]],
                      headers=['Informations', 'Results'], tablefmt='row'))
            break
    except:
        print("Not found !")
