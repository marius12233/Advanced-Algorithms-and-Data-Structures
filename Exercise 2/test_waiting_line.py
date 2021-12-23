import unittest
from heap.adaptable_waiting_line import AdaptableHeapWaitingLine

class Test_Waiting_Line(unittest.TestCase):
    def setup(): #test the declaration of an AdaptableHeapWaitingLine object
        waiting_line= AdaptableHeapWaitingLine()

    def test_add(self): #test if there are the same number of jobs that are included in the waiting line
        waiting_line= AdaptableHeapWaitingLine()
        a1=waiting_line.add(3,'p1',3)
        a2=waiting_line.add(-1,'p2',6)
        a3=waiting_line.add(-11,'p3',5)
        a4=waiting_line.add(5,'p4',4)

        #print("Lenght of waiting line is "+ str(len(waiting_line)))
        self.assertEqual(len(waiting_line),4)

    def test_remove_min(self): #test if the scheduler take the job with the minimum priority correctly
        waiting_line= AdaptableHeapWaitingLine()
        a1=waiting_line.add(3,'p1',3)
        a2=waiting_line.add(-1,'p2',6)
        a3=waiting_line.add(-11,'p3',5)
        a4=waiting_line.add(5,'p4',4)

        if not waiting_line.is_empty():
            scheduler=waiting_line.remove_min()
            self.assertEqual(a3._priority,scheduler[0])
            scheduler=waiting_line.remove_min()
            self.assertEqual(a2._priority,scheduler[0])
            scheduler=waiting_line.remove_min()
            self.assertEqual(a1._priority,scheduler[0])
            scheduler=waiting_line.remove_min()
            self.assertEqual(a4._priority,scheduler[0])

    def test_scheduling(self): #example of scheduling
        waiting_line= AdaptableHeapWaitingLine()
        time_slice=0
        i=0
        a=[None]*5
        jobs=[[-11,'p1',5],[-1,'p2',3],[-1,'p3',4],[-1,'p4',3]]
        for i in range(0,4):
            a[i]=waiting_line.add(jobs[i][0],jobs[i][1],jobs[i][2])
            time_slice +=1
            for i in range(0,len(waiting_line._data)):
                waiting_line._data[i]._waiting_time+=1

        #print(waiting_line._data.__repr__())

        if not waiting_line.is_empty():
            scheduler=waiting_line.remove_min()
            self.assertEqual(a[0]._priority,scheduler[0])
            #print("Add new job "+ scheduler[1] + " with priority "+ str(scheduler[0]) + " and lenght "+ str(scheduler[2]))

            scheduler=waiting_line.remove_min()
            self.assertEqual(a[2]._priority,scheduler[0])
            #print("Add new job "+ scheduler[1] + " with priority "+ str(scheduler[0]) + " and lenght "+ str(scheduler[2]))

            scheduler=waiting_line.remove_min()
            self.assertEqual(a[1]._priority,scheduler[0])
            #print("Add new job "+ scheduler[1] + " with priority "+ str(scheduler[0]) + " and lenght "+ str(scheduler[2]))

            scheduler=waiting_line.remove_min()
            self.assertEqual(a[3]._priority,scheduler[0])
            #print("Add new job "+ scheduler[1] + " with priority "+ str(scheduler[0]) + " and lenght "+ str(scheduler[2]))

def main(self):
        self.setup()
        self.test_add()
        self.test_remove_min()
        self.test_scheduling()

unittest.main()
