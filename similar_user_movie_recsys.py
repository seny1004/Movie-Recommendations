import pickle

with open('critics.pkl','rb') as f:
    critics=pickle.load(f)

def sim_distance(data, name1, name2):
    sum=0
    for i in data[name1]:
        if i in data[name2]:
            sum+=pow(data[name1][i]-data[name2][i],2)

    result=0
    if sum!=0:
        result=1 / (1 + sqrt(sum))
    return result

def top_match(data,name, index=10,sim_function=sim_distance):
    li=[]
    for i in data:
        if name!=i:
            li.append([sim_function(data,name,i),i])
    li.sort()
    li.reverse()
    user=[]
    for i in li[:index]:
        num=0
        for j in i:
            num+=1
            if num==2:
                user.append(j)

    return user

def Similar_User_Movie_recSys(data,user):
    movie=[]
    for u in user:
        for j in data.keys():
            if u==j:
                for k in data[u]:
                    movie.append(k)
    movie=set(movie)
    return movie


print(Similar_User_Movie_recSys(critics,top_match(critics,20)))
