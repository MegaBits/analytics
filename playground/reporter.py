import sys
import time
import datetime
import analysis
import sorter2

def analyticsReport():
  
  #Figure out how to programatically generate this given the current date (aka - "yesterday was the last dat of the period I want to inspect")
  startOfLastPeriod = [13,10,2014]
  startDate = [20,10,2014]
  endDate = [27,10,2014]

  

  print("Reports for " + str('/'.join([str(i) for i in startDate])) + " to " + str('/'.join([str(i) for i in endDate])) + " (exclusive)")
  print("========\n")
  print("User acquisition")
  print(analysis.userAcquisition(sorter2.records, startDate, endDate))
  print("\n========\n")
  print("User retention")
  print(analysis.userRetention(sorter2.records, startOfLastPeriod, startDate, endDate))
  print("\n========\n")
  print("Overworld Interactions Per Day (mean)")
  print(analysis.meanOverworldInteractionsPerDay(sorter2.sortedRecords['locationInteraction'], startDate, endDate))
  print("\n========\n")

