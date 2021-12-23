"""Main of the exercise"""
from heap.adaptable_waiting_line import AdaptableHeapWaitingLine

if __name__ == "__main__":
    waiting_line = AdaptableHeapWaitingLine() #Definition of the object Waiting Line
    time_slice = 0
    print("Insert some information for the first job:") #Insertion of the first job
    while(True):
        name = input("Insert the name of the new job: ")
        priority = input("Insert the priority of the new job. Choose a value between -20 and 19: ")
        lenght = input("Insert the length of the new job. Choose a value between 1 and 100: ")
        if ((int(priority)>=-20 and int(priority)<=19) and (int(lenght)>=1 and int(lenght)<=100)):
            waiting_line.add(int(priority),name,int(lenght))
            break
        else:
            print("Impossible to add this job. Try Again.") #ERROR

    #print("time slice="+ str(time_slice))
    #print("Current Waiting Line:"+waiting_line._data.__repr__())

    if not waiting_line.is_empty():
        scheduler=waiting_line.remove_min() #job from the waiting line goes to execution
        print("Add new job "+ scheduler[1] + " with priority "+ str(scheduler[0]) + " and lenght "+ str(scheduler[2])) #job added to execute
    time_slice += 1
    while(True):
        if not scheduler is None: #execution of a job
            if int(scheduler[2])>0:
                scheduler[2] = int(scheduler[2]) -1
        for i in range(0,len(waiting_line._data)):
            waiting_line._data[i]._waiting_time+=1
        if time_slice == 5: #invoking of reset() method
            waiting_line.reset()
            time_slice=0
        choice=input("Do you insert a job or not? y/n ")
        if choice == "y":
            print("Insert some information:") #Insertion of a new job
            name = input("Insert the name of the new job: ")
            priority = input("Insert the priority of the new job. Choose a value between -20 and 19: ")
            lenght = input("Insert the length of the new job. Choose a value between 1 and 100: ")
            if ((int(priority)>=-20 and int(priority)<=19) and (int(lenght)>=1 and int(lenght)<=100)):
                waiting_line.add(int(priority),name,int(lenght))
            else:
                print("Impossible to add this process")

        #print("time slice="+ str(time_slice))
        #print("Current Waiting Line:"+waiting_line._data.__repr__())

        if not waiting_line.is_empty() and scheduler[2]==0:
            scheduler=waiting_line.remove_min()
            print("Add new job "+ scheduler[1] + " with priority "+ str(scheduler[0]) + " and lenght "+ str(scheduler[2])) #job added to execute
        elif waiting_line.is_empty() and scheduler[2]==0:
            print('No new job in this slice') #there is any jobs in the waiting line, so there isn't any job to execute
        else:
            print("Current job:"+ scheduler[1] + " with priority "+ str(scheduler[0]) + " and lenght "+ str(scheduler[2])) #current job

        time_slice += 1
