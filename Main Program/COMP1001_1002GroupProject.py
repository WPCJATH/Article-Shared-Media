import random
import sys
from tkinter.filedialog import askopenfilename
import datetime


#
# Whole codes mainly using MVC (Model-View-Controller) Pattern
#
# Part of codes contains Oriented-Object Programming
#
#@author Liu, YI   Shu, Kunxin   WANG, Xiangzhi    Begins on Dec.5
#
#
# Function distinguished based on class belong's to 
#
# Class of View: OutPutControl, InPutControl, SignIn, UserView,
#
# Class of Controller: Controller(mian() contians)
#
# Class of Model: 
#       Dynamic classes: User, Article
#
#       Static classes: dataPool, dataPool.accessFiles, dataPool.Translators, ramdomIDs
#


#####################################################View################################################

#class for control the print ways
class OutPutControl:

    # print welcome messages
    @staticmethod
    def Welcome():
        print('''
***************************************************************************************
*  __     ___     __ _______  __      _______  _______  ___     ___      ________     *
*  \ \   |\  \   |/||/______||/|     /\_____| /  __//\ |   \   | //\    |/______|     *
*   \ \  |\|\ \  |/||/|_____/|/|    |\|      |  /  \//|| |\ \  | |\/\   |/|_____      *
*    \ \ |\| \ \ |/||/______||/|    |\|      | |    |/|| | \ \ | | \/\  |/______|     *
*     \ \|\|  \ \|/||/|_____/|/|___ |\|_____ |  \__/ /|| |  \ \| |  \/\ |/|_____      *
*      \___|   \___||_______||_____| \______| \______/ |_|   \___|   \_\|_______|     *
*                                                                                     *
***************************************************************************************

# (^V^) Welcome to C-Media!
#
# You can choose 'help' to get how to start.
# Or choose 'signin' to sign in.
# Or choose 'signup' to sign up.
# You can choose 'quit' or 'exit' to shut down the System any time you want.
# You can choose 'save' to save all changes by you any time you want.
# But if you shut down the System directly, your change won't be saved.
''')
    # this is for print user Guide
    @staticmethod
    def userGuide():
        print('''
# This is the user guide for C-Media.
# 
# You can enter an number for Diagues supplies, then your can enter the corresponding interface or perform the desired action.
# Each page and selection is based on the form of a dialog box, so it's easy to understand.
# 
# You can Sign Up if you are a new User of C-Media.
# Or you can Sign In based on a stored account of youself.
# 
# After Sign In you can Post an Article, add Friends or View other's articles in the View Area.
# Also, you can quote somebody's article for your articles. However, one article can only quote one article.
# But an article can be quote by several aritlces directly or indirectly.
# 
# You can enter 'exit' or 'quit' any time to shut down this System, System will ask you whether to save the changes you made.
# You changes will be only save after your aggreement.
# 
# !!!If you want to quit, please mannully enter 'exit' or 'quit', if you directly kill the System by 
# click Abort button outside of the system, your operations won't be save this running time at all!!!
# Including your new account, your new articles and your new friends.
# 
# (For testing and checking, every password is 123456 )
''')

    # show the successfully message to the user
    @staticmethod
    def Success(ms):
        print("# (^V^)",ms)

    # show the fail message to the user
    @staticmethod
    def Fail(ms):
        print("# (>_<)",ms)

    # show the the message to the user if the user has a illegal input
    @staticmethod
    def Illegal(ms):
        print("# (-_-)",ms)

    # if System cannot find an User or article, this function will be called
    @staticmethod
    def NotFound(ms):
        print("# (@_@)",ms)

    # normally print without some emotional expression
    @staticmethod
    def Print(ms=""):
        print("#",ms)

    # this function is for print out the content of an article
    # out of the lines in a txt file has already contains '\n', so line feed is unnesccessay
    @staticmethod
    def PrintNoLn(ms):
        print("#",ms,end="")



# class for obtian user's input in several ways
class InputControl:

    @staticmethod
    def Normal():
        s = input("# >_> ")
        return s

    @staticmethod
    def transMs(ms):
        s = input("# "+ms)
        return s

    # get main command from user
    # main command only includes ['help','quit||exit','signup','signin','save','admin']
    @staticmethod
    def GetCommand():
        ops = ['Sign In','Sign Up','Get Help','Save Changes','Admin Sign In','Quit the System']
        op = InputControl.Dialog("Which operation do you want to do?",ops)
       
        if op == 5: InputControl.askSave()

        Controller.Reader(op)
        
    # user for ask User to operate which specified instruction
    # Input: message text, options for user
    # Output: the option index of user
    @staticmethod
    def Dialog(message,options = ["Yes","Cancel"]):
        OutPutControl.Print()
        OutPutControl.Print(message)
        OutPutControl.Print("Enter the number before the option to execute.")

        numbers = []
        for i in range(1,len(options)+1):
            OutPutControl.Print(str(i)+'. '+options[i-1])
            numbers.append(str(i))

        op = InputControl.Normal()
        while op not in numbers:
            if str.lower(op.split(' ')[0]) in ['exit','quit']:
                InputControl.askSave()
                return -1

            else: 
                OutPutControl.Illegal("Connot recognize your input, please enter again.")
            op = InputControl.Normal()

        return int(op)-1

    # Ask the User whether he or she want the changes made
    # if yes chosen, the changes will be saved
    # if the changes won't be saved 
    @staticmethod
    def askSave():
        op = InputControl.Dialog("You have entered 'exit' or 'quit', do you want to save all the changes?")
        
        if op == 0:
            dataPool.accessFiles.Save()
            sys.exit(0)
        else:
            OutPutControl.Print("Exit operation canceled.")

# class to provide the sign in/up page  
class SignIn:
    # if a user choosed sign in, this function will be called
    # Only when the user enter the ID system stored and the right Password, the sign in will be conpleted
    # The user can enter 'back' to back to the previous page.
    @staticmethod
    def UserSignIn():
        flag = False
        isContinue = True
        while not flag:
            id = InputControl.transMs("Enter your ID(or enter 'back' to previous page): ")
            if id in dataPool.UsersDict:
                flag = True
            else:
                if (str.lower(id) == "back"): 
                    isContinue = False
                    break
                else: OutPutControl.Illegal("Cannot find the ID your entered.")
        
        flag = False
        while not flag and isContinue:
            password = InputControl.transMs("Enter your Password(or enter 'back' to previous page): ")
            if password == dataPool.UsersDict[id].password:
                flag = True
            else:
                OutPutControl.Illegal("You Entered a wrong password.")

        if isContinue:
            dataPool.currentState = '2' 
            dataPool.currentUser = dataPool.UsersDict[id]

            UserView.enter()

    # Once the user enter the right admin password, the admin sign in will be competed
    @staticmethod
    def adminSignIn():
        flag = False
        isContinue = True
        while not flag :
            password = InputControl.transMs("Enter Admin Password(or enter 'back' to previous page): ")
            #print(dataPool.AdminPassword)
            if password == dataPool.AdminPassword:
                flag = True
            else:
                if (str.lower(password)=='back'): 
                    isContinue = False
                    flag = True 
                else: OutPutControl.Illegal("You Entered a wrong password.")

        if isContinue: UserView.adminEnter()

    # this function is to help a new user to sign up an account for this system
    # when he or she competed filling the neccessary infomation, the account will be created and sign in automaticlly
    @staticmethod
    def UserSignUp():#firstName,lastName,password,birthday,email,friendIDs = [],articleIDs = []
        firstName = InputControl.transMs("Enter your firstName: ")
        lastName = InputControl.transMs("Enter your lastName: ")
        Birthday = InputControl.transMs("Enter your birthday(For exmple, 01-01-1990): ")
        email = InputControl.transMs("Enter your email: ")

        id = randomIds.UserId()
        OutPutControl.Print("This is your ID of C-Media: "+id)
        OutPutControl.Print("Please remember it clearly.")
        password = InputControl.transMs("Set your password: ")

        newUser = User(id,firstName,lastName,password,Birthday,email)
        dataPool.UsersDict.update({id:newUser})

        OutPutControl.Success("You account has been created successfully!")
        OutPutControl.Print()
        OutPutControl.Success("The system has automatically signed in for you.")
        dataPool.currentState = '2' 
        dataPool.currentUser = dataPool.UsersDict[id]

        UserView.enter()


# supply the pages and functions for user when a sign in or sign up completed
class UserView:

    # this function is for a normal user sign in 
    @staticmethod
    def enter():
        OutPutControl.Success("Welcome! Belows are your infomation.")
        dataPool.currentUser.showInfo()

        ops = ["Viewing Area","Look over my firends","Look over my articles","Add a new Friend","Post a new Article","Show KOLs","Sign out"]
        
        op = -1
        while op != 6:
            op = InputControl.Dialog("Your options.",ops)
            if op == 0: UserView.ViewArea()
            elif op == 1: dataPool.currentUser.showFriends()
            elif op == 2: dataPool.currentUser.showArticles()
            elif op == 3: UserView.addNewFriends()
            elif op == 4: UserView.PostArticle()
            elif op == 5: UserView.KOLs()

        
        dataPool.currentState = '1' 
        dataPool.currentUser = None

    # this function is for admin after signing in 
    @staticmethod
    def adminEnter():
        ops = ["Set P","Set T","View Area","see KOLs","Sign Out"]

        flag = True
        while flag:
            op = InputControl.Dialog("Select your operation.",ops)
            if op == 0: UserView.SetP()
            elif op == 1: UserView.SetT()
            elif op == 2: UserView.ViewArea()
            elif op == 3: UserView.KOLs()
            else: flag = False


    # this function is for adimin setting the T
    @staticmethod
    def SetT():
        flag = True
        while flag:
            T = InputControl.transMs("Please enter the T: ")
            try:
                T = int(T)
                if 0 < T <= len(dataPool.UsersDict):
                    dataPool.T = T
                    OutPutControl.Success("T set successfully!")
                    flag = False
                else:
                    OutPutControl.Fail("T cannot be negative or larger than the number of current users.")
            except:
                if str.lower(T) == 'back': flag = False
                else: OutPutControl.Illegal("You didn't enter a number.")

    # this function is for admin setting the P
    @staticmethod
    def SetP():
        flag = True
        while flag:
            P = InputControl.transMs("Please enter the P: ")
            try:
                P = int(P)
                if 0 < P <= 100:
                    dataPool.P = P
                    OutPutControl.Success("P set successfully!")
                    flag = False
                else:
                    OutPutControl.Fail("K cannot be negative or larger than 100.")
            except:
                if str.lower(k) == 'back': flag = False
                else: OutPutControl.Illegal("You didn't enter a number.")


    # this method is used for seeing KOLs
    @staticmethod
    def KOLs():
        OutPutControl.Print("P = "+str(dataPool.P))
        OutPutControl.Print("T = "+str(dataPool.T))
        for userID in dataPool.KOLs:
            dataPool.UsersDict[userID].showInfo()
            OutPutControl.Print()

    # this page is for a user to veiw other's or himself's article Some social software recommendations section
    @staticmethod
    def ViewArea():
        counter = 0
        till = 10
        flag = True
        ops = ["Show me more","I want to view an article","Back"]
        isContinue = True

        while flag and isContinue:
            while counter <= till:
                OutPutControl.Print()
                if (counter < len(dataPool.ArticleIDS)):
                    #print(len(dataPool.ArticleIDS))
                    OutPutControl.Print("Article "+str(counter+1))
                    dataPool.ArticleDict[dataPool.ArticleIDS[counter]].showInfo()
                    counter += 1
                else:
                    OutPutControl.Fail("Not more.")
                    OutPutControl.Print()
                    break
            
            op = InputControl.Dialog("Enter your option.",ops)
            if op == 0: till += 10
            elif op == 1:
                while True:
                    num = InputControl.transMs("Please enter the number of the Article(Or enter 'back' to previous page): ")
                    if (str.lower(num) == 'back'):
                            isContinue = False
                            break
                    try:
                        num = int(num) - 1 
                        if (0<=num<counter):
                            dataPool.ArticleDict[dataPool.ArticleIDS[num]].showContent()
                            break
                        else:
                            OutPutControl.Illegal("There is no article in this number.")
                    except:
                        OutPutControl.Illegal("You don't enter numbers.")
            else: flag = False

    # this is for a user to add another user as his or her friend
    @staticmethod
    def addNewFriends():
        flag = False
        isContinue = True
        while not flag and isContinue:
            id = InputControl.transMs("Enter the ID of whom you want to be a friend with(Or enter 'back' to previous page): ")
            if id in dataPool.UsersDict:
                flag = True
            else:
                if (str.lower(id) == 'back'):
                    flag = True
                    isContinue = False
                else: OutPutControl.Illegal("Cannot find the ID your entered.")

        if isContinue:
            dataPool.currentUser.addFriend(id)
            OutPutControl.Success("Friend Successfully added!")

    # this function is for a user to post a article to the system
    @staticmethod
    def PostArticle():
        id = None
        while id == None:
            id = dataPool.accessFiles.selectFile()
        
        title = InputControl.transMs("Enter your article's title: ")

        flag = True
        while flag:
            op = InputControl.Dialog("Does your article quotes someone's artice?",["Yes","No"])
            if op == 1:
                quote = ""
                break
            else:
                flag = False
                isContinue = True
                while not flag :
                    Qid = InputControl.transMs("Enter the ID of the author whom you quoted(Or enter 'back' to previous page): ")
                    if Qid in dataPool.UsersDict:
                        if dataPool.UsersDict[Qid].articleIDs!=[]:
                            flag = True
                            break
                        else:
                            OutPutControl.Illegal("The author doesn't has any article, please try again.")
                    else:
                        if (str.lower(Qid) == 'back'): isContinue = False
                        else: OutPutControl.Illegal("Cannot find the ID your entered.")

                flag = False
                ops = []
                for i in dataPool.UsersDict[Qid].articleIDs:
                    ops.append(dataPool.ArticleDict[i].title)
                ops.append('back')

                while isContinue:
                    op = InputControl.Dialog("Enter the number of the article you quoted: ",ops)
                    if op == len(ops) - 1:
                        isContinue = False
                    else:
                        quote = dataPool.UsersDict[Qid].articleIDs[op]
                        dataPool.ArticleDict[quote].AddBeQuoted(id)
                        flag = False
                        isContinue = False


        author = dataPool.currentUser.id
        date = datetime.datetime.strftime(datetime.datetime.now(),'%d-%m-%Y')

        newArt = Ariticle(id,title,author,quote,date)#id,title,author,quote,date

        dataPool.currentUser.addAritle(id)
        dataPool.ArticleIDS.append(id)
        dataPool.ArticleDict.update({id:newArt})

        OutPutControl.Success("New article added Successfully!")

#########################################################################################################

#####################################################Controller##########################################

class Controller:

    # read Operations 'help','signup','signin','save','admin'
    @staticmethod
    def Reader(c):

        # ['signin','signup','help','save','admin']
        if c==0: SignIn.UserSignIn()
        elif c==1: SignIn.UserSignUp()
        elif c==2: OutPutControl.userGuide()
        elif c==3: dataPool.accessFiles.Save()
        elif c==4: SignIn.adminSignIn()

    @staticmethod
    def main():
        dataPool.accessFiles.init()
        OutPutControl.Welcome()
        isContinue = True

        while True:
            InputControl.GetCommand()

#####################################################################################################

#####################################################Model###########################################

# class for User Object
# store user's infomation
class User:

    # init a User Object
    def __init__(self,id,firstName,lastName,password,birthday,email,friendIDs = [],articleIDs = []):
        self.firstName = firstName
        self.lastName = lastName
        self.name = firstName + ', ' + lastName
        self.id = id
        self.password = password
        self.birthday = birthday
        self.email = email

        if friendIDs == [""]: friendIDs = []
        self.friendIDs = friendIDs

        if articleIDs == [""]: articleIDs = []    
        self.articleIDs = articleIDs

    # add a friend for self
    def addFriend(self,friendID):
        self.friendIDs.append(friendID)
        dataPool.UsersDict[friendID].friendIDs.append(self.id)

    # delete a friend for self
    def deleteFriend(self,friendID):
        self.friendIDs.remove(friendID)
        dataPool.UsersDict[friendID].remove(self.id)
        #OutPutControl.Success("Successfully removed.")

    # add an article for self
    def addAritle(self,article):
        self.articleIDs.append(article)

    # print the infomation of self
    def showInfo(self):
        OutPutControl.Print("The infomation of "+self.name)
        OutPutControl.Print("Id: "+self.id)
        OutPutControl.Print("Birthday: "+self.birthday)
        OutPutControl.Print("E-mail: "+self.email)
        OutPutControl.Print()

    # print the friends of this
    def showFriends(self):
        if self.friendIDs == []: OutPutControl.Fail("Oops! You don't have any friends by now")
        else:
            OutPutControl.Print("Here are your friend(s):")

            for friendID in self.friendIDs:
                friend = dataPool.UsersDict[friendID]
                OutPutControl.Print(friend.name+' '+friend.id)
            
            OutPutControl.Print()

    # print the friends of user's friend
    def showFriends_(self):
        if self.friendIDs == []: OutPutControl.Fail("Oops! {}, {} don't have any friends by now".format(firstName,lastName))
        else:
            OutPutControl.Print("Here are his or her friend(s):")

            for friend in self.friendIDs:
                friend = dataPool.UsersDict[friendID]
                OutPutControl.Print(friend.name+' '+friend.id)
            
            OutPutControl.Print()

    # print the articles of this
    def showArticles(self):
        if self.articleIDs == []: OutPutControl.Fail("Oops! You don't have any articles by now")
        else:
            ops = []
            for articleID in self.articleIDs:
                article = dataPool.ArticleDict[articleID]
                ops.append(article.title)
            ops.append('Back')

            op = InputControl.Dialog("Here are your article(s),you can enter the number before the article to view.",ops)
            if op == len(ops) - 1: pass
            else:
                dataPool.ArticleDict[self.articleIDs[op]].showContent()

    # print the articles of other users(not self)
    def showArticles_(self):
        if self.articleIDs == []: OutPutControl.Fail("Oops! {} don't have any articles by now".format(self.name))
        else:
            OutPutControl.Print("Here are his or her article(s):")
        
            for article in self.articles:
                article = dataPool.ArticleDict[articleID]
                OutPutControl.Print(article.title)

            OutPutControl.Print()


# class for Article Object
# store article's infomation
class Ariticle:

    # init a articel Object
    def __init__(self,id,title,author,quote,date):
        self.id = id
        self.title = title
        self.author = author
        self.quote = quote
        self.date = date
        self.beQuoted = []

    # if self be Quoted, the fuction will be called
    def AddBeQuoted(self,articleID):
        self.beQuoted.append(articleID)

    # show the infomation about the article
    def showInfo(self):
        OutPutControl.Print("The infomation of "+self.title+":")
        OutPutControl.Print("author: "+dataPool.UsersDict[self.author].name+" ID: "+self.author)
        OutPutControl.Print("date: "+self.date)
        OutPutControl.Print("Quote: "+(dataPool.ArticleDict[self.quote].title if self.quote!= "" else "None"))

        bequoted = "None" if self.beQuoted == [] else dataPool.ArticleDict[self.beQuoted[0]].title
        for i in range(1,len(self.beQuoted)):
            bequoted += ", "
            bequoted += dataPool.ArticleDict[self.beQuoted[i]].title

        OutPutControl.Print("Be Quoted: "+bequoted)
        OutPutControl.Print()

    # nicely print the content of an article
    def showContent(self):
        self.showInfo()
        OutPutControl.Print("The content of "+self.title+":")
        dataPool.accessFiles.showArticle(self.id)


# class for store current data which is very possible to be accessed
#
# once system starts the class will access stored files to read
# all data stored before so that the system won't be a disposable system
# it can store data and read data in files 
class dataPool():
    # read stored data and put all User in this dict()
    UsersDict = dict()# id, User user

    # for store current User, not for admin
    currentUser = ''

    # to store current state # '1' no one sign in '2' user sign in '3' admin sign in
    currentState = '1' 

    # read and stored all Articles stored and put all Article in this dict()
    ArticleDict = dict()# id, Article article

    # store all the articlesIDS
    ArticleIDS = []

    # store the password of admin
    AdminPassword = ''

    # store the T for caculating KOL
    T = 0

    # store the P for caculating KOL
    P = 0

    # Store all KOLs
    # Once someone push a new Artice, or the system starts, or the admin changes the K,P, KOLs will update
    KOLs = list()



    # class for access files stored before
    class accessFiles:

        # the system will store all the user infomation in a file named "User.txt"
        # so once the system starts, the system will access the file and read all info in it.
        # id,firstName,lastName,password,birthday,email,friendIDs = [],articleIDs = []
        # line id[{}]firstName[{}]LastName[{}]password[{}]birthday[{}]email[{}]artcle1:article2:article3[{}]friend1:friend2:friend3
        @staticmethod
        def readAllUser():
            File = open(".\\files\\" + "User.txt","r",encoding='utf-8')
            lines = File.readlines()

            for line in lines:
                line = dataPool.Translator.decode(line)#id,firstName,lastName,password
                s = line.split("[{}]")
                dataPool.accessFiles.newUser(s)

        # once the system starts, the system will read all User infomation stored before and 
        # create new Objects to load the User's infomation in python cache
        @staticmethod
        def newUser(s):
            friends = []
            articles = []
            
            #print(s)
            dataPool.accessFiles.getUserArtFri(s[6:],friends,articles)#send friends and articles to update
            user = User(s[0],s[1],s[2],s[3],s[4],s[5],friends,articles)

            dataPool.UsersDict.update({s[0]:user})

        # load the Articles and Friends for User
        @staticmethod
        def getUserArtFri(items,users,articles):
            for art in items[0].split(":"):
                articles.append(art)

            for friend in items[1].split(":"):
                users.append(friend)
        
        # load all Article information
        @staticmethod
        def readAllArt():
            File = open(".\\files\\" + "Articles.txt","r",encoding='utf-8')
            lines = File.readlines()
            for i in range(len(lines)):
                lines[i] = dataPool.Translator.decode(lines[i])
            dataPool.accessFiles.newArts(lines)
        
        # push article infomation to python cache
        # line id[{}]title[{}]author[{}]quote[{}]date
        @staticmethod
        def newArts(lines):
            for line in lines:
                line = line.split("[{}]")

                newArt = Ariticle(line[0],line[1],line[2],line[3],line[4])#id,title,author,quote,date
                dataPool.ArticleDict.update({line[0]:newArt})
                dataPool.ArticleIDS.append(line[0])

        # after all articles read in ArticleDicts
        # add articles which quotes the article for every article 
        @staticmethod
        def addQuotes():
            for articleID in dataPool.ArticleDict:
                Quote = dataPool.ArticleDict[articleID].quote
                if Quote != "":
                    dataPool.ArticleDict[Quote].AddBeQuoted(articleID)

        # read the information of admin
        # line password[{}]T[{}]P[{}]
        @staticmethod
        def readAdmin():
            File = open(".\\files\\" + "Admin.txt","r",encoding='utf-8')
            lines = File.readlines()
            File.close()

            line = dataPool.Translator.decode(lines[0]).split("[{}]")
            if len(line) == 1 or len(line) == 0:
                pass
            else:
                dataPool.AdminPassword = line[0]
                dataPool.T = int(line[1])
                dataPool.P = int(line[2])

        # get the KOLs after calcuating
        @staticmethod
        def calcuKOL():
            numAllowed = int(dataPool.P/100 * len(dataPool.UsersDict))
            potentialUser = []
            
            for userID in dataPool.UsersDict:
                flag = False
                for articleID in dataPool.UsersDict[userID].articleIDs:
                    counter = dataPool.accessFiles.calcuBeQutoed(articleID)
                    if counter >= dataPool.T: flag = True

                if flag: potentialUser.append(userID)

            dataPool.KOLs = potentialUser[:numAllowed]
        
        # calculate the number of article's which quote the ariticle directly or indirectly
        @staticmethod
        def calcuBeQutoed(articleID):
            counter = 0
            for articleid in dataPool.ArticleDict:
                article = dataPool.ArticleDict[articleid]
                
                flag = False
                while article.quote != "":
                    article = dataPool.ArticleDict[article.quote]
                    if article.id == articleID:
                        flag = True
                        break
                
                if flag: counter += 1

            return counter


        # read data from files by calling methods below to init the System
        @staticmethod
        def init():
            dataPool.accessFiles.readAllUser()
            dataPool.accessFiles.readAllArt()
            dataPool.accessFiles.addQuotes()
            dataPool.accessFiles.readAdmin()
            dataPool.accessFiles.calcuKOL()

        # save all changes by Rewrite archive files
        @staticmethod
        def Save():
            File = open(".\\files\\" + "User.txt","w",encoding='utf-8')
            for user in dataPool.UsersDict:
                File.write(dataPool.accessFiles.UserStorageMaker(dataPool.UsersDict[user])+"\n")
            File.close()

            File = open(".\\files\\" + "Articles.txt","w",encoding='utf-8')
            for user in dataPool.ArticleDict:
                File.write(dataPool.accessFiles.ArtStorageMaker(dataPool.ArticleDict[user])+"\n")
            File.close()

            File = open(".\\files\\" + "Admin.txt","w",encoding='utf-8')
            File.write(dataPool.accessFiles.AdiminStorageMaker())
            File.close()

            OutPutControl.Success("Changes saved successfully!")

        # line password[{}]K[{}]P[{}]
        @staticmethod
        def AdiminStorageMaker():
            strForStore = ""
            strForStore += dataPool.AdminPassword + "[{}]"
            strForStore += str(dataPool.T) + "[{}]"
            strForStore += str(dataPool.P) + "[{}]"

            return dataPool.Translator.encrypt(strForStore)

        # Package the cached user data and send it to Save ()
        # line # line id[{}]firstName[{}]LastName[{}]password[{}]birthday[{}]email[{}]artcle1:article2:article3[{}]friend1:friend2:friend3
        @staticmethod
        def UserStorageMaker(user):
            strForStore = ""
            strForStore += user.id + "[{}]"
            strForStore += user.firstName + "[{}]"
            strForStore += user.lastName + "[{}]"
            strForStore += user.password + "[{}]"
            strForStore += user.birthday + "[{}]"
            strForStore += user.email + "[{}]"

            if user.articleIDs == []: strForStore += "[{}]"
            else:
                strForStore += user.articleIDs[0]
                for i in range(1,len(user.articleIDs)):
                    strForStore += ":" + user.articleIDs[i]
                strForStore += "[{}]"

            if user.friendIDs == []: strForStore += "[{}]"
            else:
                strForStore += user.friendIDs[0]
                for i in range(1,len(user.friendIDs)):
                    strForStore += ":" + user.friendIDs[i]
                strForStore += "[{}]"

            return dataPool.Translator.encrypt(strForStore)

        # Package the cached article data and send it to Save ()
        #line id[{}]title[{}]author[{}]quote[{}]date
        @staticmethod
        def ArtStorageMaker(article):
            strForStore = ""
            strForStore += article.id + "[{}]"
            strForStore += article.title + "[{}]"
            strForStore += article.author + "[{}]"
            strForStore += article.quote + "[{}]"
            strForStore += article.date + "[{}]"

            return dataPool.Translator.encrypt(strForStore)

        # nicely print out content of an article
        @staticmethod
        def showArticle(name):
            OutPutControl.Print()
            File = open(".\\files\\" + name,"r",encoding='utf-8')
            lines = File.readlines()

            for line in lines:
                OutPutControl.PrintNoLn(dataPool.Translator.decode(line))

            OutPutControl.Print()
            OutPutControl.Print()

        # open the file select window and let the user select an txt file to upload the article
        @staticmethod
        def selectFile():
            Path=askopenfilename(title='Select a .txt file', filetypes=[('TXT', '*.txt')])

            if Path:
                File=open(Path,'r', encoding='utf-8')

                lines = File.readlines()
                File.close()

                id = randomIds.ArticleId()
                newFile = open(".\\files\\"+id,'w',encoding='utf-8')

                for line in lines:
                    newFile.write(dataPool.Translator.encrypt(line))

                
                newFile.close()

                dataPool.accessFiles.showArticle(id)
                return id

            else:
            #except:
                OutPutControl.Fail("Fail to Open the file, please try again.")

            return None


               
    # class for encrypt a fine so that the file can stored and will not be viewed by anyone
    # Or decode a fine so that the specified user may access him files
    class Translator():
        
        # encrtpt one line by encrypt the chars in line one by one, Blank included
        @staticmethod
        def encrypt(line):
            newLine = ""
            for s in line:
                newLine += dataPool.Translator.encryptChar(s)

            return newLine

        # encrpty the parameter char by using the key below
        @staticmethod
        def encryptChar(s):
            key = {'!': ')', '"': '{', '#': 'a', '$': '!', '%': 'w', '&': ';', "'": 'o', '(': '4', ')': 'X', '*': 'R', '+': 'b', ',': 'S', '-': '^', '.': 'P', '/': '.', '0': 'Y', '1': 'z', '2': ']', '3': 'j', '4': 'W', '5': '3', '6': 't', '7': 'T', '8': 'p', '9': '~', ':': "'", ';': 'U', '<': '1', '=': 'J', '>': ',', '?': 'u', '@': 'g', 'A': 'H', 'B': '+', 'C': 'C', 'D': 'v', 'E': '}', 'F': '@', 'G': '&', 'H': 'M', 'I': 'c', 'J': '$', 'K': 'N', 'L': 'l', 'M': '/', 'N': '9', 'O': 'F', 'P': 'Q', 'Q': '*', 'R': '?', 'S': '2', 'T': '<', 'U': 'y', 'V': 'x', 'W': 'q', 'X': 'n', 'Y': ':', 'Z': '=', '[': '5', '\\': '(', ']': '[', '^': 'm', '_': '-', '`': '|', 'a': 'f', 'b': '8', 'c': 'D', 'd': '0', 'e': 'e', 'f': 'r', 'g': 'E', 'h': 'h', 'i': '_', 'j': 'O', 'k': '%', 'l': '\\', 'm': '#', 'n': 'G', 'o': '6', 'p': 'L', 'q': '7', 'r': 'Z', 's': '"', 't': '`', 'u': 'I', 'v': '>', 'w': 'A', 'x': 's', 'y': 'K', 'z': 'd', '{': 'B', '|': 'i', '}': 'k', '~': 'V'}
            if 33<=ord(s)<=126:
                return key[s]
            else:
                return s

        # decode one line by decode the chars in line one by one, Blank included
        @staticmethod
        def decode(line):
            newLine = ''
            for s in line:
                newLine += dataPool.Translator.decodeChar(s)

            return newLine

        # decode the parameter char by using the opKey which is the oppsite of Key doing encrpty above
        @staticmethod
        def decodeChar(s):
            opKey = {')': '!', '{': '"', 'a': '#', '!': '$', 'w': '%', ';': '&', 'o': "'", '4': '(', 'X': ')', 'R': '*', 'b': '+', 'S': ',', '^': '-', 'P': '.', '.': '/', 'Y': '0', 'z': '1', ']': '2', 'j': '3', 'W': '4', '3': '5', 't': '6', 'T': '7', 'p': '8', '~': '9', "'": ':', 'U': ';', '1': '<', 'J': '=', ',': '>', 'u': '?', 'g': '@', 'H': 'A', '+': 'B', 'C': 'C', 'v': 'D', '}': 'E', '@': 'F', '&': 'G', 'M': 'H', 'c': 'I', '$': 'J', 'N': 'K', 'l': 'L', '/': 'M', '9': 'N', 'F': 'O', 'Q': 'P', '*': 'Q', '?': 'R', '2': 'S', '<': 'T', 'y': 'U', 'x': 'V', 'q': 'W', 'n': 'X', ':': 'Y', '=': 'Z', '5': '[', '(': '\\', '[': ']', 'm': '^', '-': '_', '|': '`', 'f': 'a', '8': 'b', 'D': 'c', '0': 'd', 'e': 'e', 'r': 'f', 'E': 'g', 'h': 'h', '_': 'i', 'O': 'j', '%': 'k', '\\': 'l', '#': 'm', 'G': 'n', '6': 'o', 'L': 'p', '7': 'q', 'Z': 'r', '"': 's', '`': 't', 'I': 'u', '>': 'v', 'A': 'w', 's': 'x', 'K': 'y', 'd': 'z', 'B': '{', 'i': '|', 'k': '}', 'V': '~'}
            if 33<=ord(s)<=126:
                return opKey[s]
            else:
                return s



# class for create ids for new Users or new Ariticles
class randomIds():

    # get a random id for new User but cannot repeated
    @staticmethod
    def UserId():
        newId = randomIds.get_id()
        while newId in dataPool.UsersDict:
            newId = get_id()

        return newId

    # get a random id for new Article but cannot repeated
    @staticmethod
    def ArticleId():
        newId = randomIds.get_id() + ".txt"
        while newId in dataPool.ArticleDict:
            newId = get_id() + ".txt"

        return newId

    # built for UserId() and ArticleId() above
    # can create a String(length = 6) of digits with ramdom chars from 0 to 9
    @staticmethod
    def get_id():
        id = ''
        for j in range(6):
            id += str(random.randint(0,9))

        return id

#########################################################################################################


       
if __name__ == "__main__":
    Controller.main()
        