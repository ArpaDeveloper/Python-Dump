#Placeholder list of student records
tuple1=("456","Arpa","Systems","1")
tuple2=("234","Eeli","Java","5")
tuple3=("456","Arpa","Java","3")
tuple4=("234","Eeli","Systems","5")
tuple5=("344","Cristi","Java","2")
student_list = [tuple1,tuple2,tuple3,tuple4,tuple5]


def main():
    while True:
        print("""===== Student Grade Management System =====
1. Add student record
2. Display all records
3. Delete a record (by student ID and course ID)
4. Display records sorted by course ID and score (descending)
5. Query records by student ID
0. Exit
""")
        
        choice = input("Please select an option (0-5):")
        if(choice == "1"):
            new_ID = input("Please give student ID name:")
            new_student = input("Please give student name:")
            new_course = input("Please give course ID name:")
            new_grade = input("Please give grade name:")
            new_tuple = (new_ID, new_student, new_course, new_grade)
            student_list.append(new_tuple)
            continue

        elif(choice == "2"):
            i = 0
            while i < len(student_list):
                test_tuple = student_list[i]
                print("Student_ID:"+test_tuple[0],"Student_name:"+test_tuple[1],"Course ID:"+test_tuple[2],"Grade:"+test_tuple[3])
                i+=1
                
        elif(choice == "3"):
            delete_studentid = input("Give student_id to delete:")
            delete_courseid = input("Give course_id to delete:")
            j = 0
            while j < len(student_list):
                test_tuple2 = student_list[j]
                if(test_tuple2[0] == delete_studentid and test_tuple2[2] == delete_courseid):
                    student_list.remove(student_list[j])
                else:
                    j+=1

        elif(choice == "4"):
            student_list.sort(key=lambda x: (x[2], -int(x[3]))) 
            k = 0
            while k < len(student_list):
                test_tuple3 = student_list[k]
                print("Student_ID:"+test_tuple[0],"Student_name:"+test_tuple[1],"Course ID:"+test_tuple[2],"Grade:"+test_tuple[3])
                k+=1

        elif(choice == "5"):
            query_studentid = input("Give student_id to query:")
            l = 0
            while l < len(student_list):
                test_tuple4 = student_list[l]
                if(test_tuple4[0] == query_studentid):
                    print("Student_ID:"+test_tuple4[0],"Student_name:"+test_tuple4[1],"Course ID:"+test_tuple4[2],"Grade:"+test_tuple4[3])
                
                l+=1

        elif(choice == "0"):
            print("Thank you!")
            break
        else:
            print("Wrong input!")
            continue

if __name__ == "__main__":
    main()
