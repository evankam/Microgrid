for i in range (0,10):
    pullData1 = open("sampleData.txt","a+")
    pullData1.write( str(i)+',' +str(i) +"\n")
    pullData1.close()
