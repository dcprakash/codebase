
checkin={id1:[checkin1,time1], id2:()}
checkout=collections.defaultdict(lambda: [0,0])

def checkOut(int id, string stationName, int t):
    checkinSt, checkinT = checkin.pop(id)
    checkout[(checkinSt, stationName)][0]+=1
    checkout[(checkinSt, stationName)][1]+=t-checkinT