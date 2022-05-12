import os

def MakeCommit(days:int):
    if days<1:
        return os.system('git push')
    else:
        dates=f'(days) days ago'
        
        with open('data.txt','a') as file:
            file.write(f'{dates}\n')
            
            
            
    #Staging
    os.system('git add data.txt')
    #Commiting
    os.system('git commit --date"'+dates+'" -m "Initial Commit"')  
    return days*MakeCommit(days-1)      


MakeCommit(365)
