import pyttsx3
import os 
import time

while(1==1):

        pyttsx3.speak("Welcome to chat bot")
        print("Welcome to chat bot")

        pyttsx3.speak("how can i help you")
        print("How can I help you :" ,end=' ')
        p = input()

        if (("run" in p) or ("launch" in p) or ("open" in p) or ("execute" in p)) and (("chrome" in p) or ("google" in p)):
                if ("dont" in p):
      	                print("OK as you wish")
                else:
                        pyttsx3.speak("Opening Chrome")
                        os.system("start chrome")
                        time.sleep(5)

        elif (("run" in p) or ("launch" in p) or ("open" in p) or ("execute" in p)) and (("notepad" in p) or ("notebook" in p) or ("editor" in p)):
                if ("dont" in p):
      	                print("OK as you wish")
                else:                
                        pyttsx3.speak("Opening notepad")
                        os.system("notepad")

        elif (("run" in p) or ("launch" in p) or ("execute" in p) or ("open" in p)) and (("media" in p) or ("player" in p)):
                if ("dont" in p):
      	                print("OK as you wish")
                else:                
                        pyttsx3.speak("opening windows media player")
                        os.system("start wmplayer")

        elif (("run" in p) or ("launch" in p) or ("execute" in p) or ("open" in p)) and (("explorer" in p) or ("browser" in p)):
                if ("dont" in p):
      	                print("OK as you wish")
                else:                
                        pyttsx3.speak("opening internet explorer")
                        os.system("start iexplore")

        elif (("run" in p) or ("launch" in p) or ("execute" in p) or ("open" in p)) and (("outlook" in p)):
                if ("dont" in p):
      	                print("OK as you wish")
                else:                
                        pyttsx3.speak("opening microsoft outlook")
                        os.system("start outlook")

        elif (("run" in p) or ("launch" in p) or ("execute" in p) or ("open" in p)) and (("powerpoint" in p)):
                if ("dont" in p):
      	                print("OK as you wish")
                else:   
                        pyttsx3.speak("opening microsoft powerpoint")
                        os.system("start powerpnt")

        elif (("run" in p) or ("launch" in p) or ("execute" in p) or ("open" in p)) and (("computer" in p) or ("pc" in p)):
                if ("dont" in p):
      	                print("OK as you wish")
                else:                
                        pyttsx3.speak("opening my computer")
                        os.system("start explorer")

        elif (("run" in p) or ("launch" in p) or ("execute" in p) or ("open" in p)) and (("calculator" in p) or ("calculations" in p)):
                if ("dont" in p):
      	                print("OK as you wish")
                else:                
                        pyttsx3.speak("opening calculator")
                        os.system("calc")

        elif (("run" in p) or ("launch" in p) or ("execute" in p) or ("open" in p)) and (("magnifier" in p) or ("zoom" in p)):
                if ("dont" in p):
      	                print("OK as you wish")
                else:                
                        pyttsx3.speak("opening magnifier")
                        os.system("start magnify")

        elif (("run" in p) or ("launch" in p) or ("execute" in p) or ("open" in p)) and (("paint" in p) or ("draw" in p)):
                if ("dont" in p):
      	                print("OK as you wish")
                else:                
                        pyttsx3.speak("opening paint")
                        os.system("start mspaint")

        elif (("run" in p) or ("launch" in p) or ("execute" in p) or ("open" in p)) and (("registry" in p) and ("editor" in p)):
                if ("dont" in p):
      	                print("OK as you wish")
                else:                
                        pyttsx3.speak("opening registry editor")
                        os.system("start regedit")

        elif (("run" in p) or ("launch" in p) or ("execute" in p) or ("open" in p)) and (("wordpad" in p) or ("word" in p)):
                if ("dont" in p):
      	                print("OK as you wish")
                else:                
                        pyttsx3.speak("opening wordpad")
                        os.system("start write")

        elif (("run" in p) or ("launch" in p) or ("execute" in p) or ("open" in p)) and (("system" in p) and ("configuration" in p)):
                if ("dont" in p):
      	                print("OK as you wish")
                else:                
                        pyttsx3.speak("opening system configuration")
                        os.system("msconfig")
	
        elif (("run" in p) or ("launch" in p) or ("execute" in p) or ("open" in p)) and (("command" in p) and ("promt" in p) or ("cmd" in p)):
                if ("dont" in p):
      	                print("OK as you wish")
                else:                
                        pyttsx3.speak("opening command promt")
                        os.system("start cmd.exe")

        elif ("exit" in p) or ("quit" in p):
                if ("dont" in p):
      	                print("OK as you wish")
                else:                
                        pyttsx3.speak("Thanks for coming    Had good time with you")
                        print("Thanks for coming . Had good time with you")
                break

        elif (("take" in p) or ("capture" in p)) and (("screenshot" in p) or ("ss" in p) or ("screen" in p)):
                if ("dont" in p):
      	                print("OK as you wish")
                else:                
                        pyttsx3.speak("Taking Screenshot")  
                        import pyautogui
                        from tkinter import filedialog
                        myScreenshot = pyautogui.screenshot()
                        file_path = filedialog.asksaveasfilename(defaultextension='.jpg')
                        myScreenshot.save(file_path)
                        time.sleep(5)
        else : 
                print("dont support")
   


