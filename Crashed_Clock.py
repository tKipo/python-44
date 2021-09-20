Number = int(input())
Hours = Number // 3600
Minutes = (Number - Hours * 3600) // 60
Seconds = Number - Hours * 3600 - Minutes * 60
print(Hours % 24, ":", Minutes, ":", Seconds)
<<<<<<< HEAD
print("Good news everyone?!")
#check out
=======
print("Good news everyone")
>>>>>>> parent of aab2804 (Update Crashed_Clock.py)
