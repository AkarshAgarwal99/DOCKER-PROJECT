import os
import getpass
os.system("tput setaf 2")
print("\t\t\tHello World of Redhat make life easy")
os.system("tput setaf 3")
print("\t\t\t ----------------------------------------------")

print("Where you want to go remote/local")
location = input()

apass = "redhat"
password = getpass.getpass("Enter Your Password")
if apass != password:
    print("Authentication failed")
    exit()


if location == "remote":
    print("Tell me IP of remote system")
    IP = input()
    os.system("tput setaf 4")
    print("\t\t\tPlease ENTER TO CONTINUE : ")
    os.system("tput setaf 5")
    os.system("ssh-keygen -y")
    os.system("ssh-copy-id root@{}".format(IP))

while True:
        print("""1. to see date 
press 2 : to check cal
press 3 : to start web server
press 4 : to create user
press 5 : to exit from command
Press 6 : To Start docker Services
Press 7 : To Create your own website 
Press 8 " To Stop the Running Site
        """)
        print("Enter Your Choice",end="")
        ch = input()
        print(ch)

        if location == "local":
            if int(ch)==1:
                os.system("date")
            elif int(ch)==2:
                os.system("cal")
            elif int(ch)==3:
                os.system("systemctl start httpd")
                print("Your Server is Started")
            elif int(ch)==5:
                exit()
            elif int(ch)==4:
                print("Please enter the name of the user")
                i = input()
                os.system("useradd {}".format(i))
            elif int(ch)==7:
                os.system("docker-compose up -d")
                print("Your Services is Started")
            elif int(ch)==8:
                os.system("docker-compose stop")
            elif int(ch)==6:
                print("""1. Do want to See the images of docker")
                2. If the container is already launched to see the containers
                3. Do You want to launced any container""")
                p = int(input("Enter any number please"))
                if p==1:
                    os.system("docker images")
                elif p==2:
                    os.system("docker ps -a")
                elif p==3:
                    print("""press 1 : For Ubuntu
                    Press 2 : For CentOS 
                    press 3 : For Your own Created Image 
                    """)
                    l = int(input())
                    if l==1:
                        print("Tell me Your OS container name ")
                        k = input()
                        os.system("docker run -it --name {} ubuntu:14.04".format(k))
                    elif l==2:
                        print("Tell me Your OS container Name")
                        k = input()
                        os.system("docker run -it --name {} centos:latest".format(k))
                    elif l==3:
                        print("Tell me Your Os container name ")
                        k = input()
                        os.system("docker run -it --name {} akarsh:latest".format(k))
        if location == "remote":
            if int(ch)==1:
                os.system("ssh {} date".format(IP))
            elif int(ch)==2:
                os.system("ssh {} cal".format(IP))
            elif int(ch)==3:
                os.system("ssh {} systemctl start httpd".format(IP))
                print("Your Server is Started")
            elif int(ch)==5:
                exit()
            elif int(ch)==4:
                print("Please enter the name of the user")
                i = input()
                os.system("ssh {} useradd {}".format(IP,i))
            elif int(ch)==6:
                print("""1. Do want to See the images of docker")
                2. If the container is already launched to see the containers
                3. Do You want to launced any container""")
                p = int(input("Enter any number please"))
                if p==1:
                    os.system("ssh {} docker images".format(IP))
                elif p==2:
                    os.system("ssh {} docker ps -a".format(IP))
                elif p==3:
                    print("""press 1 : For Ubuntu
                    aPress 2 : For CentOS
                    press 3 : For Your own Created Image
                    """)
                    l = int(input())
                    if l==1:
                        print("Tell me Your OS container name ")
                        os.system("ssh {} docker run -it  ubuntu:14.04".format(IP))
                    elif l==2:
                        print("Tell me Your OS container Name")
                        k = input()
                        os.system("ssh {} docker run -it --name {} centos:latest".format(IP,k))
                    elif l==3:
                        print("Tell me Your Os container name ")
                        k = input()
                        os.system("ssh {} docker run -it --name {} akarsh:latest".format(IP,k))


        o = input("Please Enter to continue")
        os.system("clear")
        




