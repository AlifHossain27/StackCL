#!/usr/bin/env python3
import sys
import requests
from simple_term_menu import TerminalMenu
import webbrowser



def stackCL():
     # Getting the search
     words=str(' '.join(sys.argv[1:]))
     try:
          # Getting Stack Overflow search results
          data=[]
          resp  = requests.get(f"https://api.stackexchange.com/2.2/search?order=desc&sort=activity&intitle={str(words)}&site=stackoverflow")
          d=resp.json()
          for i in d['items']:
            json_data={i["title"]:i["link"]}
            data.append(json_data)
          
          # Adding Options
          options=['Quit']
          for i in d['items']:
            options.append(i['title'])

          mainMenu=TerminalMenu(options,title = "Stackoverflow Search Results: ")
          quitting=False

          # Functionality of the Options
          while quitting ==False:
            optionsIndex=mainMenu.show()
            optionsChoice=options[optionsIndex]
            if optionsChoice=='Quit':
              quitting=True
            for option in data:
              key, value = list(option.items())[0]
              if key == optionsChoice:
                print(value)
                webbrowser.open(value, new=0, autoraise=True)
                quitting =True
              else:
                pass
          
     except Exception as e:
          print(e)


# Executing the Function
if __name__=='__main__':
     stackCL()