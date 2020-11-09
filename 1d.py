import os
import getpass


def menu():
    print("\n\n")
    print("""
    Press 1 to run a new container
    Press 2 to manage containers
    Press 3 to manage images
    Press 4 for info and stats
    Press 5 to exit
    """)
    i = int(input("Enter your choice : "))
    print(i)
    while i == 1:
        newc()
    while i == 2:
        manc()
    while i == 3:
        mai()
    while i == 4:
        ias()
    while i == 5:
        print("=================================================================")
        print("..................Thankyou for using my menu..................... ")
        print("=================================================================")
        exit()
    else:
        print("You have entered a wrong key please try again...")
        menu()
def newc():
    print("""
    Press 1 if you want only to start a new container
    Press 2 if you want to start container in background
    Press 3 to go back to main Menu
    Press 4 to exit
    """)
    j = int(input("Enter your choice : "))
    while j == 1:
        a = input("Please enter the image name (e.g., ubuntu:14.04) : ")
        os.system("docker run {}".format(a))
        os.system("docker ps -a")
        newc()
    while j == 2:
        c = input("Please enter the image name (e.g., ubuntu:14.04) : ")
        os.system("docker run -d {}".format(c))
        os.system("docker ps -a")
        newc()
    while j == 3:
        menu()
    else:
        print("=================================================================")
        print("..................Thankyou for using my menu.....................")
        print("=================================================================")
        exit()
def manc():
    print("""
    Press 1 if you want to show list of running containers
    Press 2 if you want to show a list of all containers
    Press 3 if you want to stop a running container
    Press 4 if you want to start a stopped container
    Press 5 if you want to delete a container
    Press 6 if you want to delete a stopped container
    Press 7 if you want to delete a running container
    Press 8 to go to the previous Menu
    Press 9 to exit
    """)
    k = int(input("Enter your choice : "))
    while k == 1:
        os.system("docker ps")
        manc()
    while k == 2:
        os.system("docker ps -a")
        manc()
    while k == 3:
        os.system("docker ps")
        e = input("Enter the container ID (running container) from above IDs : ")
        os.system("docker stop {}".format(e))
        manc()
    while k == 4:
        os.system("docker ps -a")
        f = input("Enter the container ID (stopped container) from above IDs : ")
        os.system("docker start {}".format(f))
        os.system("docker ps -a")
        manc()
    while k == 5:
        os.system("docker ps -a")
        g = input("Enter the container ID from above IDs to delete : ")
        os.system("docker rm {}".format(g))
        os.system("docker ps -a")
        manc()
    while k == 6:
        os.system("docker ps -a")
        d = input("Enter the container ID (stopped container) from above IDs : ")
        os.system("docker rm {}".format(d))
        os.system("docker ps -a")
        manc()
    while k == 7:
        os.system("docker ps")
        h = input("Enter the container ID (running container) from above IDs : ")
        os.system("docker rm -f {}".format(h))
        manc()
    while k == 8:
        menu()
    else:
        print("=================================================================")
        print("..................Thankyou for using my menu..................... ")
        print("=================================================================")
        exit()
def mai():
    print("""
    Press 1 if you want to download an image
    Press 2 if you want to delete an image
    Press 3 if you want to see the list of all images
    Press 4 if you want to delete all unused images
    Press 5 to go to back Menu
    Press 6 to exit the Menu
    """)
    l = int(input("Enter your choice : "))
    while l == 1:
        m = input("Please provide the image name to download (e.g., ubuntu:14.04) : ")
        os.system("docker pull {}".format(m))
        os.system("docker images")
        mai()
    while l == 2:
        n = input("Please provide the image name to delete (e.g., ubuntu:14.04) : ")
        os.system("docker pull {}".format(n))
        os.system("docker images")
        mai()
    while l == 3:
        os.system("docker images")
        mai()
    while l == 4:
        os.system("docker images -a")
        mai()
    while l == 5:
        menu()
    else:
        print("=================================================================")
        print("..................Thankyou for using my menu..................... ")
        print("=================================================================")
        exit()
def ias():
    print("""
    Press 1 if you want to see the logs of container
    Press 2 if you want to see the stats of running containers
    Press 3 if you want to see the processes of container
    Press 4 if you want to see the docker version
    Press 5 to go to the previous Menu
    Press 6 to exit from my Menu
    """)
    p = int(input("Enter your choice : "))
    while p == 1:
        os.system("docker ps -a")
        q = input("Please enter the container ID : ")
        os.system("docker logs {}".format(q))
        ias()
    while p == 2:
        os.system("docker stats")
        ias()
    while p == 3:
        os.system("docker ps -a")
        r = input("Please enter the container ID : ")
        os.system("docker top {}".format(r))
        ias()
    while p == 4:
        os.system("docker version")
        ias()
    while p == 5:
        menu()
    else:
        print("=================================================================")
        print("..................Thankyou for using my menu..................... ")
        print("=================================================================")
        exit()
os.system("tput setaf 5")
print("\t\t\tWelcome to my Docker Menu !!!")
os.system("tput setaf 2")
print("\t\t\t=============================")

passwd = getpass.getpass("Enter your password : ")
if passwd != "bkp":
    print("Password Incorrect!!!")
    exit()
else:
    menu()
