""" WaitingLineBase class with Job class"""
class WaitingLineBase:
    class _Job:
        """Lightweight composite to store priority queue items."""
        __slots__ = '_priority', '_name', '_lenght', '_waiting_time'

        def __init__(self, p, n, l, wt=0): #initialize a job
            self._priority = p
            self._name = n
            self._lenght = l
            self._waiting_time = wt

        def __lt__(self, other): #"less then":compare other jobs based on priority, waiting time and length
            if self._priority < other._priority:
                return True
            elif self._priority == other._priority:
                if self._lenght >= other._lenght:
                    return True
                elif self._lenght == other._lenght:
                    if self._waiting_time >= other._waiting_time:
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                return False

        def __repr__(self): #output of job structure
            return "Priority="+str(self._priority) +" Name="+ self._name+" Lenght="+ str(self._lenght)+" Waiting time="+ str(self._waiting_time)

#------------------------------ public behaviors ------------------------------
    def is_empty(self):                  # concrete method assuming abstract len
        """Return True if the priority queue is empty."""
        return len(self) == 0

    def __len__(self):
        """Return the number of jobs in the priority queue."""
        raise NotImplementedError('deve essere implementato dalla sottoclasse.')

    def add(self, priority, name, lenght, waiting_time):
        """Add a new job in the priority queue."""
        raise NotImplementedError('deve essere implementato dalla sottoclasse.')

    def min(self):
        """Return but do not remove the job with highest priority (minimum value of priority).

        Raise Empty exception if empty.
        """
        raise NotImplementedError('deve essere implementato dalla sottoclasse.')

    def remove_min(self):
        """Remove and return the job with minimum highest priority (minimum value of priority).

        Raise Empty exception if empty.
        """
        raise NotImplementedError('deve essere implementato dalla sottoclasse.')
