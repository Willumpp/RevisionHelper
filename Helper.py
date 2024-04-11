import random, time, os

class Program:
    def __init__(self, start_dir, fraction_removed):
        self.main_dir = start_dir
        self.folder_history = []
        self.fraction_removed = fraction_removed
        self.script_dir = self.GetDir()
        self.q_history = []

        #If folder, add to history
        if ".txt" not in start_dir:
            self.folder_history.append(start_dir)
            self.ChangeDir(start_dir)
    
    #Change working directiory
    def ChangeDir(self, new_dir):
        os.chdir(new_dir)
    
    #Get working directory
    def GetDir(self):
        return os.getcwd()

    def GetRandomFile(self, directory):
        dirs = os.listdir(directory)
        f_num = 0

        if (len(dirs) > 0):
            f_num = random.randint(0, len(dirs)-1) #Get random number from directory length
            return dirs[f_num]
        else:
            return ""

    def AddToHistory(self, new_dir):
        self.folder_history.append(new_dir)
    
    def SaveHistory(self):
        with open(os.path.join(self.script_dir,"History.txt"),"w") as f:
            for i in self.folder_history:
                f.write(str(i)+"\n")
    
    def WhiteSpace(self,  file_name):
        #User friendly gap
        for i in range(5): print("\n")

        print(file_name) #Display name for context

    def ClearLine(self, line):
        #Remove words by specified fraction
        full_line = [i for i in line]
        new_line = [i for i in line]

        for i in range(0, len(line) // self.fraction_removed):
            n = random.randint(1,len(line)-1) #Get random index

            while len(line[n]) <= 3:
                n = random.randint(1,len(line)-1) #Get random index
            
            new_line[n] = "______"

        #Display line
        for word in new_line: print(word, end=" ")
        print("\n")

        input() #Wait until guess is finished

        print("Full line was:")
        for word in full_line: print(word, end=" ")
        print("\n")
        input()

    def ClearLineSpecified(self, line, index):
        #New lists to avoid conflicts
        full_line = [i for i in line]
        new_line = [i for i in line]

        #Replace specified positions with blank, +1 to avoid wildcard
        for i in index:
            new_line[int(i)+1] = "______"

        #Display line with specified blanks
        for word in new_line: print(word, end=" ")
        print("\n")

        input()

        for word in full_line: print(word, end=" ")
        print("\n")

        input()

    def GetLine(self, line_list):
        non_read_chars = ["#","CLE","*"]
        read_chars = ["-","CLS","RLS"]

        line = ""
        orig_line = ""

        '''or (line in self.q_history)'''
        
        #Find valid line randomly
        for attempts in range(0,300):
            if (len(line) <= 0) or (line[0] not in read_chars and line[0][0] != "["):
                line = random.choice(line_list) #Choose random line
                orig_line = line
                line = line.split() #Split line

        self.q_history.append(line)

        return line, orig_line

    #Reading game
    def ReadFile(self, selected_file, file_name):
        f = open(selected_file, "r") #Open file
        lines = f.readlines()

        #If file is not empty...
        if len(lines) > 0:
            #Find "=" wildcards in file
            for i in lines:
                temp = i.split()
                
                #If first char is "=", always say
                if len(temp) > 0: 
                    if temp[0] == "=":
                        self.q_history.append(temp) #Add to history
                        self.WhiteSpace(file_name) #User friendly whitespace
                        self.ClearLine(temp) #Perform clear

            #print (line)

            line, orig_line = self.GetLine(lines)

            self.WhiteSpace(file_name)

            #Non-specified removal
            if len(line) > 0 and line[0] == "-": self.ClearLine(line) #Regular note

            #Specified removal
            if len(line) > 0 and line[0][0] == "[":
                index_list = line[0].strip("][").split(",") #Convert index in brackets to list of strings with indexes

                self.ClearLineSpecified(line, index_list) #Game with specified clears
                

            #Consecutive list
            if len(line) > 0 and line[0] == "CLS":

                #Display top line
                for word in line: print(word, end=" ")
                print("\n")

                #Get top of line index
                top = lines.index(orig_line)
                c_line = "CLS"
                count = 0 #Position in list

                #Repeat unilt break is found
                while lines[top + count + 1].replace("\n","") != "CLE":
                    count += 1 #Increment count
                    c_line = lines[top + count].split() #Get line in list

                    #If line has characters and is regular line
                    if len(c_line) > 0 and c_line[0] == "*":

                        self.ClearLine(c_line) #Remove game

                    elif len(c_line) > 0 and c_line[0][1] == "[":
                        index_list = c_line[0].strip("]*[").split(",") #Convert index in brackets to list of strings with indexes

                        self.ClearLineSpecified(c_line, index_list) #Game with specified clears

            #Reveal list
            if len(line) > 0 and line[0] == "RLS":

                #Display top line
                for word in line: print(word, end=" ")
                print("\n")

                #Get top of line index
                top = lines.index(orig_line)
                c_line = "RLS"
                count = 0 #Position in list

                input() #Wait until user input for reveal

                #Repeat unilt break is found
                while lines[top + count + 1].replace("\n","") != "RLE":
                    count += 1 #Increment count
                    c_line = lines[top + count].split() #Get line in list

                    #If line has characters and is regular line
                    if len(c_line) > 0 and c_line[0] == "*":
                        
                        #Display full line
                        for word in c_line: print(word, end=" ")
                        print("\n")
                    
                    #Uppon finding break point
                    if len(c_line) > 0 and c_line[0] == "RBP":
                        input() #Wait until user input
                        print("\n")

                input()

        f.close()

    #Find file to work with
    def Locator(self):
        last_file = self.folder_history[-1] #Get last file opened
        dirs = os.listdir(last_file) #Get all directories of latest file

        rand_file = self.GetRandomFile(last_file)

        selected_file = os.path.join(last_file, rand_file)

        #If a text file
        if ".txt" in selected_file:
            self.ReadFile(selected_file, rand_file)

            self.AddToHistory(self.main_dir) #Current file is now first

        #If a folder
        elif "." not in selected_file: #If folder
            self.AddToHistory(selected_file) #Add selected file to history
            return ""

        #If directory is empty
        elif rand_file == "":
            self.AddToHistory(self.main_dir) #Current file is now first

            return ""

        

        
main_dir = input("Input file directory: ")
frac_removed = int(input("Fraction of line to be removed: "))
q_asked = int(input("How many questions should be asked: "))
repeatable = input("Type 'n' for NON-repeatable questions: ")

p = Program(main_dir, frac_removed)


#Folder
if ".txt" not in main_dir:
    
    for i in range(0, q_asked):
        output = ""

        #Repeat until file is found
        while output == "":
            output = p.Locator()

#Text file
elif ".txt" in main_dir:
    for i in range(0, q_asked):
        p.ReadFile(main_dir, os.path.basename(main_dir))

p.SaveHistory()

#D:\Revision Notes\History\American West\Key Topic 1\Figures.txt