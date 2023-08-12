'''


We have

train_nos a list of above train numbers.
train_names a Hash map of train number : train name.
from Hash map of train number and starting location of train.
to Hash map of train number and destination of train.
running_days a Hash map of train_no and lilst of days.
sleeper_fare a Hash Map of train no and sleeper fare.
ac_fare a hash map of train and AC fare.
You need to complete

get_train_name(train_no) it takes a train number and returns train name if it exists in the given data. It should return "Invalid Train Number" without quotes.

get_trains_for_day(day) it is a string it specifies day.Format of day should be similar to the days in this list ["Su","Mo","Tu","We","Th","Fr","Sa"] If day is given in any other format or any other string is given as day then return "Invalid Day".Otherwise return list of train numbers which run that day.

get_total_fare(train_number,passengers_dict) It takes train nnumber and a dictionary or hash map which contains two strings the data like this {"sleeper":m,"ac":n} where m,n>=0. You have whole inforation. Calculate ticket cost and return if Data is valid otherwise return -1.

You just need to complete these functions. Taking input and printing output will be handled by program.


Input Format

n an integer specifying number of queries. In each of the n lines integer q is taken. specifying type of query.
If q==1. a train number is read and get_train_name(train_no) is called
If q==2 a string day is read and get_trains_for_day(day) is called.
If q==3 a number train_no followed b passenger dict is read and get_total_fare(train_number,passengers_dict) is called.

Output Format

Contains n lines specifying result of n queries.

Sample Input 0
4
1 25627
2 We
3 25627 10 10
2 Su

Sample Output 0
Karnataka Express
16453 22642 22905
41000
25627

Sample Input 1
5
1 123
3 22905 4 5
2 Th
1 22642
2 Sun

Sample Output 1
Invalid Train Number
18343
16453 22642
Trivandrum SF Express
Invalid Day

'''

train_nos=[16453,25627,22642,22905]
train_names={16453:"Prasanti Express",25627:"Karnataka Express",22642:"Trivandrum SF Express",22905:"Okha Howrah Express"}
from_list={16453:"SBC",25627:"SBC",22642:"VSKP",22905:"ST"}
to_list={16453:"BBS",25627:"DEC",22642:"TVM",22905:"KOAA"}
running_days={16453:['Mo','We','Th'],25627:['Su','Tu'],22642:['Mo','Tu','We','Th','Fr','Sa'],22905:['We','Sa']}
sleeper_fare={16453:600,25627:1600,22642:800,22905:987}
ac_fare={16453:987,25627:2500,22642:1256,22905:2879}
trains_for_day={'Su':[],'Mo':[],'Tu':[],'We':[],'Th':[],'Fr':[],'Sa':[]}

for train_nos in running_days:
    day_lst=running_days[train_nos]
    for i in day_lst:
        trains_for_day[i].append(train_nos)

    
def get_train_name (train_no):
    
    #Write your code here
    if train_no in train_names:
        return train_names[train_no]
    return "Invalid Train Number"

def get_trains_for_day(day_of_run):
    #Write your code here
    
    if day_of_run not in trains_for_day:
        return "Invalid Day"
    
    return trains_for_day[day_of_run]

def get_total_fare(train_no,passenger_dict):
    
    #Write your code here
    if train_no not in train_names:
        return -1
    total_amount=0
    total_amount+= sleeper_fare[train_no]*passenger_dict["sleeper"]
    total_amount+= ac_fare[train_no]*passenger_dict["ac"]
    return total_amount

n=int(input())
l=[]
for i in range(n): 
    q=input().split()
    if(q[0]=='1'):   
        l.append(get_train_name(int(q[1])))
    elif(q[0]=='2'):
        l.append(get_trains_for_day(q[1]))
    elif(q[0]=='3'):
        l.append(get_total_fare(int(q[1]),{"sleeper":int(q[2]), "ac":int(q[3])}))
for i in l:
    if(type(i)==type([])):
        print(*i)
    else:
        print(i)
