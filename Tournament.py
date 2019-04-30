import numpy as np
from time import perf_counter_ns 
from sklearn.utils import shuffle

class Team ():
    def __init__(self):
        self.__init()
        self.__score()
    
    def __init(self):
        self.__players = np.random.uniform(0.15,1,21)

    def __score(self):
        self.__teamscore = self.__players.mean()

    def GetScore(self):
        return self.__teamscore

class Division():
    def __init__(self,pNumOfTeams,pName):
        self.__Teams = []
        self.__teamscore = np.zeros((pNumOfTeams,2))
        self.__NumOfTeams = pNumOfTeams
        self.__Name = pName
        self.__generate()

    def __generate(self):
        for i in np.arange(0,self.__NumOfTeams):
            self.__Teams.append(Team())
            self.__teamscore[i,0] = i+1
            self.__teamscore[i,1] = self.__Teams[i].GetScore()
        
        self.__teamscore = shuffle(self.__teamscore)
    
    def GetTeams(self):
        return self.__Teams
    def GetNumOfTeams(self):
        return self.__NumOfTeams

    def GetScoreMatrix(self,pSorted=False):
        if pSorted==True:
            return np.sort(self.__teamscore,0)
        else:
            return self.__teamscore
    def GetName(self):
        return self.__Name
    def GetChampion(self):
        step = self.__NumOfTeams
        champion = np.copy(self.__teamscore)
        while(step!=1):
            aux = []
            for i in np.arange(0,step,2):
                if champion[i,1] > champion[i+1,1]:
                    aux.append(champion[i])
                else:
                    aux.append(champion[i+1])
            step = int(step/2)
            champion = np.array(aux)
        return champion

class Tournament():
    def __init__(self):
        self.__divisions = []
        self.__count = 0
    def AddDivision(self,pDivision):
        self.__divisions.append(pDivision)
        self.__count+=1
    def GetWinners(self,pDebug=False):
        for i in np.arange(0,self.__count,1):
            if pDebug==True:
                print('Teams & Scores (Shuffled): {a}'.format(a=self.__divisions[i].GetScoreMatrix()))
            print ('Champion of division {a}: Team {b}. Score: {c}'.format(a=self.__divisions[i].GetName(),b=self.__divisions[i].GetChampion()[0,0],c=self.__divisions[i].GetChampion()[0,1]))
    


def main():

    start = perf_counter_ns()
    DivisionWest = Division(8,'West')
    DivisionEast = Division(8,'East')

    MyTournament = Tournament()
    MyTournament.AddDivision(DivisionWest)
    MyTournament.AddDivision(DivisionEast)
    #MyTournament.GetWinners(True)
    MyTournament.GetWinners()
    elapsedtime = perf_counter_ns()-start

    print ('Elapsed time: {a} ns ({b} s)'.format(a=elapsedtime,b=elapsedtime*1e-9))

    """
    MyDivision = Division(8)
    Teams = MyDivision.GetTeams()

    print ('Team score matrix: {a}'.format(a=MyDivision.GetScoreMatrix()))

    for i in np.arange(0,MyDivision.GetNumOfTeams()):
        print ('Team {a} score: {b}'.format(a=i+1,b=Teams[i].GetScore()))

    print('Champion: Team {a}. Score: {b}'.format(a=MyDivision.GetChampion()[0,0],b=MyDivision.GetChampion()[0,1]))
    """
if __name__=='__main__':
    main()

#players = np.random.uniform(0.15,1,21)

#print('Players Success Rate:{a}'.format(a=players))
#print('Team Success rate:{a}'.format(a=players.mean()))

#Teams = np.arange(1,9,1)
#size = np.size(Teams)
#print(size)
#match = np.zeros((int(size/2),2))
#print(match)

#print(np.random.randint(0,63,4))
#np.random.shuffle()


