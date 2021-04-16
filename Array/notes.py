from collections import defaultdict

checkin={}
journey=defaultdict(lambda: [0,0])

void checkIn(int id, string stationName, int t):
    checkin[id]=[stationName,t]
    
void checkOut(int id, string stationName, int t):
    chkinS,chkinT=checkin[id]
    journey[(chkinS,stationName)][0]+=t-checkin
    journey[(chkinS,stationName)][1]+=1
    
void get
    
    

