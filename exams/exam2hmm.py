# exam2hmm.py
# Noah Brackenbury
# CS 322, Fall 2015

import sys

def main():
    exam2hmm = hmm(sys.argv[1])
    print("a)  P(baseball|religion) = " + str((exam2hmm.getA("baseball", "religion")/exam2hmm.getTopicCounts("baseball"))))
    print("b)  P(windows|windows) = " + str((exam2hmm.getA("windows", "windows")/exam2hmm.getTopicCounts("windows"))))
    print("c)  P(god|medicine) = " + str((exam2hmm.getB("god", "medicine")/exam2hmm.getTopicCounts("medicine"))))
    print("d)  P(religion|baseball) = " + str((exam2hmm.getB("religion", "baseball")/exam2hmm.getTopicCounts("religion"))))
    problist = []
    probdict = {}
    l = 0
    topics = ["religion", "baseball", "windows", "cars", "guns", "medicine"]
    for i in topics:
        for j in topics:
            problist.append(((exam2hmm.getA(i,j) / exam2hmm.getTopicCounts(i)) * (exam2hmm.getB("com", i) / exam2hmm.getCounts("com")) * (exam2hmm.getB("re", j) / exam2hmm.getCounts("re"))))
            probdict[problist[l]] = (i, j)
            l += 1
    problist = sorted(problist, key=float, reverse=True)
    print("e)  The probabilities for the hidden states of 'com re' are as follows:")
    for k in range(0,36):
        print(probdict[problist[k]])
        print(str(problist[k]))
    
    
class hmm:
    def __init__(self, topicsfile):
        self.text = open(topicsfile).read()
        self.a = {}
        self.b = {}
        self.lines = self.text.splitlines()
        self.counts = {}
        self.topicCounts = {}
        
        prevTopic = 'windows'
        for line in self.lines:
            topic = line.split()[0]
            word = line.split()[1]

            if word in self.counts:
                self.counts[word] += 1
            else:
                self.counts[word] = 1

            if topic in self.topicCounts:
                self.topicCounts[topic] += 1
            else:
                self.topicCounts[topic] = 1

            if prevTopic in self.a:
                if topic in self.a[prevTopic]:
                    self.a[prevTopic][topic] += 1
                else:
                    self.a[prevTopic][topic] = 1
            else:
                self.a[prevTopic] = {}
                self.a[prevTopic][topic] = 1
            if word in self.b:
                if topic in self.b[word]:
                    self.b[word][topic] += 1
                else:
                    self.b[word][topic] = 1
            else:
                self.b[word] = {}
                self.b[word][topic] = 1
            prevTopic = topic
        
    def getCounts(self, word):
        if word in self.counts:
            return self.counts[word]
        else: 
            return 0
        
    def getTopicCounts(self, topic):
        if topic in self.topicCounts:
            return self.topicCounts[topic]
        else: 
            return 0
        
    def getA(self, topic1, topic2):
        if topic1 in self.a:
            if topic2 in self.a[topic1]:
                return self.a[topic1][topic2]
            else:
                return 0
        else:
            return 0
        
    def getB(self, word, topic):
        if word in self.b:
            if topic in self.b[word]:
                return self.b[word][topic]
            else:
                return 0
        else:
            return 0
        


if __name__ == '__main__':
    main()