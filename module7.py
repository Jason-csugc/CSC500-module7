'''Module 7: Critical Think Assignment'''

import sys

courseList = ['CSC101', 'CSC102', 'CSC103', 'NET110', 'COM241']
roomList = ['3004', '4501', '6755', '1244', '1411']
instrctorList = ['Haynes', 'Alvarado', 'Rich', 'Burke', 'Lee']
timesList = ['8:00 a.m.', '9:00 a.m.', '10:00 a.m.', '11:00 a.m.', '1:00 p.m.']

courseRoomDict = dict(zip(courseList, roomList))
courseInstructorDict = dict(zip(courseList, instrctorList))
courseTimeDict = dict(zip(courseList, timesList))

courseInput = ''

while courseInput != 'q':
    print(courseInput)
    courseInput = input("Enter course number: (q to exit)")
    if courseInput == 'q':
        sys.exit()
    elif courseInput in courseList:
        room = courseRoomDict[courseInput]
        instructor = courseInstructorDict[courseInput]
        time = courseTimeDict[courseInput]
        print('Course: ' + courseInput)
        print('    Room: ' + room)
        print('    Instructor: ' + instructor)
        print('    Time: ' + time)
    else:
        print("Course entered not found.")
