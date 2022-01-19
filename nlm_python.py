from time import sleep
from playsound import playsound
import winsound
import os
import sys

def clear_screen():
    command = 'clear'
    if os.name in ('nt', 'dos'):
        command = 'cls'
    os.system(command)

# main = winsound.PlaySound("main.wav", winsound.SND_ASYNC | winsound.SND_ALIAS)
clear_screen()
print("Legyen már Tamás is milliomos! v1.0")

def mark1():
    playsound('C:/Users/Felhasználó/OneDrive/Desktop/DESKTOP_TEMP_20210924/NLMTIM_WD/NLM_python/mark1.wav')
    
def mark2():
    playsound('C:/Users/Felhasználó/OneDrive/Desktop/DESKTOP_TEMP_20210924/NLMTIM_WD/NLM_python/mark2.wav')
    
def back1():
    back1 = winsound.PlaySound("back1.wav", winsound.SND_ASYNC | winsound.SND_ALIAS)
    
def back2():
    back2 = winsound.PlaySound("back2.wav", winsound.SND_ASYNC | winsound.SND_ALIAS)
    
def back3():
    back3 = winsound.PlaySound("back3.wav", winsound.SND_ASYNC | winsound.SND_ALIAS)
  
def next1():
    playsound('C:/Users/Felhasználó/OneDrive/Desktop/DESKTOP_TEMP_20210924/NLMTIM_WD/NLM_python/next1.wav')
    
def next2():
    playsound('C:/Users/Felhasználó/OneDrive/Desktop/DESKTOP_TEMP_20210924/NLMTIM_WD/NLM_python/next2.wav')
    
def win1():
    playsound('C:/Users/Felhasználó/OneDrive/Desktop/DESKTOP_TEMP_20210924/NLMTIM_WD/NLM_python/win1.wav')

def lose1():
    playsound('C:/Users/Felhasználó/OneDrive/Desktop/DESKTOP_TEMP_20210924/NLMTIM_WD/NLM_python/lose1.wav')
    print("You have lost! You won: 0 Ft")
    sys.exit()
    
def win2():
    playsound('C:/Users/Felhasználó/OneDrive/Desktop/DESKTOP_TEMP_20210924/NLMTIM_WD/NLM_python/win2.wav')

def lose2():
    playsound('C:/Users/Felhasználó/OneDrive/Desktop/DESKTOP_TEMP_20210924/NLMTIM_WD/NLM_python/lose2.wav')
    print("You have lost! You won: 100.000 Ft")
    sys.exit()
    
def win3():
    playsound('C:/Users/Felhasználó/OneDrive/Desktop/DESKTOP_TEMP_20210924/NLMTIM_WD/NLM_python/win3.wav')

def lose3():
    playsound('C:/Users/Felhasználó/OneDrive/Desktop/DESKTOP_TEMP_20210924/NLMTIM_WD/NLM_python/lose2.wav')
    print("You have lost! You won: 1.500.000 Ft")
    sys.exit()

def question_1():
    back1()
    while True:
        try:
            back1()
            print("1. A deviaton from the specified or expected behaviour that is visible to end-users is called: ")
            print("A: An error")
            print("B: A fault")
            print("C: A failure")
            print("D: A defect")
            answer1 = input("Select an uppercase letter: ")
        except ValueError:
            answer1 = input("Write a letter! Try again! ")
        if answer1 != "C":
            lose1()
            continue
        else:
            win1()
            print("You won 5.000 Ft!")
            sleep(3)
            clear_screen()
            question_2()

def question_2():
    back1()
    while True:
        try:
            print("2. Which is not a testing principle?")
            print("A: Early testing")
            print("B: Defect clustering")
            print("C: Pesticidie paradox")
            print("D: Exhaustive testing")
            answer2 = input("Select an uppercase letter: ")
        except ValueError:
            answer2 = input("Write a letter! Try again! ")
        if answer2 != "D":
            lose1()
        else:
            win1()
            print("You won 10.000 Ft!")
            sleep(3)
            clear_screen()
            question_3()

def question_3():
    back1()
    while True:
        try:
            print("3. What is the process of analysing and removing causes of failures in software?")
            print("A: Validation")
            print("B: Testing")
            print("C: Debugging")
            print("D: Verification")
            answer2 = input("Select an uppercase letter: ")
        except ValueError:
            answer2 = input("Write a letter! Try again! ")
        if answer2 != "C":
            lose1()
        else:
            win1()
            print("You won 25.000 Ft!")
            sleep(3)
            clear_screen()
            question_4()         
           
def question_4():
    back1()
    while True:
        try:
            print("4. Exhaustive Testing...")
            print("A: Is impractical but possible")
            print("B: Is practically possible")
            print("C: Is impractical and impossible")
            print("D: Is always possible")
            answer2 = input("Select an uppercase letter: ")
        except ValueError:
            answer2 = input("Write a letter! Try again! ")
        if answer2 != "C":
            lose1()
        else:
            win1()
            print("You won 50.000 Ft!")
            sleep(3)
            clear_screen()
            question_5()
                      
def question_5():
    back1()
    while True:
        try:
            print("5. Below is a list of problems that can be observed during testing or operation. Which is MOST likely a failure?")
            print("A: The product crashed when the user selected an option in a dialogue box")
            print("B: One source code file included in the build was the wrong version")
            print("C: The computation algorithm used the wrong input variables")
            print("D: The developer misinterpreted te requirement for the algorithm")
            answer2 = input("Select an uppercase letter: ")
        except ValueError:
            answer2 = input("Write a letter! Try again! ")
        if answer2 != "A":
            lose2()
        else:           
            win2()
            print("You won 100.000 Ft!")
            sleep(3)
            clear_screen()
            next1()
            question_6()
            
def question_6():
    back2()
    while True:
        try:
            print("6. Static analysis is...")
            print("A: Same as static testing")
            print("B: Done by the developers")
            print("C: Both")
            print("D: None")
            answer2 = input("Select an uppercase letter: ")
            mark1()
        except ValueError:
            answer2 = input("Write a letter! Try again! ")
        if answer2 != "C":
            lose2()
        else:
            win2()
            print("You won 200000 Ft!")
             sleep(3)
            clear_screen()
            next1()
            question_7()      
            
def question_7():
    back2()
    while True:
        try:
            print("7. 'BVA' in hungarian is:")
            print("A: Büdös Vámpír Analízis")
            print("B: Ekvivalencia-partícionálás")
            print("C: A hét tesztelési alapelv összefoglaló neve")
            print("D: Határérték-analízis")
            answer2 = input("Select an uppercase letter: ")
            mark1()
        except ValueError:
            answer2 = input("Write a letter! Try again! ")
        if answer2 != "D":
            lose2()
        else:
            win2()
            print("You won 300.000 Ft!")
            sleep(3)
            clear_screen()
            next1()
            question_8()
          
def question_8():
    back2()
    while True:
        try:
            print("8. White Box Testing is...")
            print("A: Same as glass box testing")
            print("B: Same as clear box testingg")
            print("C: Both")
            print("D: None")
            answer2 = input("Select an uppercase letter: ")
            mark1()
        except ValueError:
            answer2 = input("Write a letter! Try again! ")
        if answer2 != "C":
            lose2()
        else:
            win2()
            print("You won 500.000 Ft!")
            sleep(3)
            clear_screen()
            next1()
            question_9()         

def question_9():
    back2()
    while True:
        try:
            print("9. Mikor beszélhetünk kockázatról (risk)?")
            print("A: A jövőben a negatív következmények biztosan bekövetkeznek")
            print("B: A jövőben a negatív következmények lehet, hogy bekövetkeznek")
            print("C: A tesztelés tárgyára vonatkozó következmények")
            print("D: Hagyjál békén, Tamás!")
            answer2 = input("Select an uppercase letter: ")
            mark1()
        except ValueError:
            answer2 = input("Write a letter! Try again! ")
        if answer2 != "B":
            lose2()
        else:
            win2()
            print("You won 800.000 Ft!")
            sleep(3)
            clear_screen()
            next1()
            question_10()        
            
def question_10():
    back2()
    while True:
        try:
            print("10. Who are the persons involved in a Formal Review? I. Manager, II. Moderator / Facilitator, III. Scribe / Recorder, IV. Assistant Manager")
            print("A: FALSE: II, III, TRUE: I, IV")
            print("B: TRUE: I, II, III, FALSE: IV")
            print("C: FALSE: I, II, III, TRUE: IV")
            print("D: TRUE: I, III, FALSE: II, IV")
            answer2 = input("Select an uppercase letter: ")
            mark1()
        except ValueError:
            answer2 = input("Write a letter! Try again! ")
        if answer2 != "B":
            lose2()
        else:
            win3()
            print("You won 1.500.000 Ft!")
            sleep(3)
            clear_screen()
            next1()
            question_11()        
            
def question_11():
    back3()
    while True:
        try:
            print("11. Hány ekvivalencia-partíciót kell létrehozni, ha egy jegyértékelési rendszert tesztelünk: 0-20%: 1, 21-40: 2, 41-60%: 3, 61-80% 4: 81-100%: 5")
            print("A: 4")
            print("B: 5")
            print("C: 6")
            print("D: 7")
            answer2 = input("Select an uppercase letter: ")
            mark2()
        except ValueError:
            answer2 = input("Write a letter! Try again! ")
        if answer2 != "B":
            lose2()
        else:
            win3()
            print("You won 3.000.000 Ft!")
            sleep(3)
            clear_screen()
            next1()
            question_12()      
            
def question_12():
    back3()
    while True:
        try:
            print("12. Hány tesztesetet kell írni, ha négy feltételünk van? (decision table, Y/N) (^ = hatványozás)")
            print("A: 4^2")
            print("B: 2^2")
            print("C: 2^3")
            print("D: 2^4")
            answer2 = input("Select an uppercase letter: ")
            mark2()
        except ValueError:
            answer2 = input("Write a letter! Try again! ")
        if answer2 != "D":
            lose2()
        else:
            win3()
            print("You won 5.000.000 Ft!")
            sleep(3)
            clear_screen()
            next1()
            question_13()

def question_13():
    back3()
    while True:
        try:
            print("13. Which is the correct order?")
            print("A: Rework, [...], Follow up, [...], Planning")
            print("B: Planning, [...], Follow up, [...], Rework")
            print("C: Rework, [...], Planning, [...], Follow up")
            print("D: Planning, [...], Rework, [...], Follow up")
            answer2 = input("Select an uppercase letter: ")
            mark2()
        except ValueError:
            answer2 = input("Write a letter! Try again! ")
        if answer2 != "D":
            lose2()
        else:
            win3()
            print("You won 10.000.000 Ft!")
            sleep(3)
            clear_screen()
            next1()
            question_6()
            
def question_14():
    back3()
    while True:
        try:
            print("14. Which of the following is a Key Charachteristics of Walk Through?")
            print("A: Scenario, Dry Run, Peer Group")
            print("B: Pre-Meeting Preparations")
            print("C: Formal Follow Up Process")
            print("D: Includes Metrics")
            answer2 = input("Select an uppercase letter: ")
            mark2()
        except ValueError:
            answer2 = input("Write a letter! Try again! ")
        if answer2 != "A":
            lose2()
        else:
            win3()
            print("You won 20.000.000 Ft!")
            clear_screen()
            next2()
            question_15()
            
def question_15():
    back3()
    while True:
        try:
            print("15. Which of the following is a purpose of the review planning phase?")
            print("A: Log defects")
            print("B: Explain the documents to the participants")
            print("C: Gather metrics")
            print("D: Allocate the individual roles")
            answer2 = input("Select an uppercase letter: ")
            mark2()
        except ValueError:
            answer2 = input("Write a letter! Try again! ")
        if answer2 != "D":
            lose2()
        else:
            win3()
            print("You won 40.000.000 Ft!")
            sleep(3)
            clear_screen()
            next1()
            sys.exit()
            
            
question_1()
