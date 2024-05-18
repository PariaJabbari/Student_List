from os import system
from collections import namedtuple
from time import sleep

Student = namedtuple("Student", ("name", "family_name", "age",
                     "gender", "national_code", "student_code"))

student_list = [
    Student("meisam", "ilka", 20, "Male", "2222222", "2222222"),
    Student("parsa", "bokaei", 23, "Male", "3333333", "3333333"),
    Student("mehrsa", "bokaei", 30, "Female", "4444444", "4444444"),
    Student("hadis", "taheri", 45, "Female", "5555555", "5555555"),
    Student("meisam", "negari", 14, "Male", "6666666", "6666666")
]


while True:

    # region get choice
    while True:
        print(
            "1. [A]dd student",
            "\n2. [S]how students",
            "\n3. [R]emove Student",
            "\n4. [F]ind student",
            "\n5. [E]xit"
        )
        choice = input(
            "What do you want to do in student list? \U0001F469\n\U0001F449")
        system("cls")

        if choice in ("1", "2", "3", "4", "5", "A", "S", "R", "F", "E"):
            break

        print("You did not choose one of the tasks. \U0001F612")
        # endregion

    match choice:

        case "1" | "A":

            # region get answer
            while True:
                system("cls")

                answer = input(
                    "Are you sure you want to add student(s) to the student list? 1. Yes or 2. No \n\U0001F449")
                system("cls")

                match answer:
                    case "Yes" | "yes" | "1":

                        # region get name
                        while True:
                            name = input(
                                "Enter the student's name.\n\U0001F449")
                            system("cls")

                            if name != "":
                                break

                            print("The name field cannot remain empty. \U0001F621")
                        # endregion

                        # region get family name
                        while True:
                            family_name = input(
                                "Enter the student's family name.\n\U0001F449")
                            system("cls")

                            if family_name != "":
                                break

                            print(
                                "The family name field cannot remain empty. \U0001F621")
                        # endregion

                        # region get age
                        while True:
                            age = int(
                                input("Enter the student's age.\n\U0001F449"))
                            system("Cls")

                            if age in range(1, 121):
                                break

                            print(
                                "You entered the student's age incorrectly. \U0001F621")
                        # endregion

                        # region get gender
                        while True:
                            gender = input(
                                "Enter the student's gender.\n\U0001F449")
                            system("cls")

                            if gender in ("Female", "Male", "Other"):
                                break

                            print(
                                "The gender you enter should be Female, Male, or Other. \U0001F621")
                        # endregion

                        # region get national code
                        while True:
                            n_code = input(
                                "Enter the student's national code.\n\U0001F449")
                            system("cls")

                            if n_code == "":
                                print(
                                    "You cannot left the national code field empty. \U0001F621")
                                continue

                            for student in student_list:
                                if student.national_code == n_code:
                                    print(
                                        n_code, "is already registered in the system as a student's national code. \U0001F9D0")
                                    break
                            else:
                                break
                        # endregion

                        # region get student code
                        while True:
                            std_code = input(
                                "Enter the student's student code.\n\U0001F449")
                            system("cls")

                            if std_code == "":
                                print(
                                    "You cannot left the student code field empty. \U0001F621")
                                continue

                            for student in student_list:
                                if student.student_code == std_code:
                                    print(
                                        std_code, "is already registered in the system as a student's student code. \U0001F9D0")
                                    break
                            else:
                                break
                        # endregion

                        student = Student(
                            name=name,
                            family_name=family_name,
                            age=age,
                            gender=gender,
                            national_code=n_code,
                            student_code=std_code
                        )
                        student_list.append(student)

                        # region showing the added student to the user
                        see_student = input(
                            "Do you want to see the profile of the student you entered? 1. Yes or 2. No\n\U0001F449")
                        system("cls")

                        if see_student in ("Yes", "yes", "1"):
                            print(*Student._fields, sep="\t")
                            print(
                                "-------------------------------------------------------------------------")
                            print(*student, sep="\t")
                            print(
                                "-------------------------------------------------------------------------")
                        # endregion
                    case "No" | "no" | "2":
                        break
                    case _:
                        print(
                            "You did not choose one of the options. Wait 3 seconds. \U0001F621")
                        sleep(3)
                        continue
            # endregion

                if input("Do you want to add another student? 1. Yes or 2. No\n\U0001F449") not in ("Yes", "yes", "1"):
                    system("cls")
                    break

        case "2" | "S":

            # region get answer about which column the user want to see
            answer = input(
                "Do you want to see all columns? 1. Yes or 2. No\n\U0001F449")
            system("cls")

            if answer in ("Yes", "yes", "1"):
                display_fields = Student._fields

            else:
                display_fields = []

                for field in (Student._fields):
                    while True:
                        print("Do you want to see the", field,
                              "column? 1. Yes or 2. No\n\U0001F447")
                        answer_ = input()
                        system("cls")

                        match answer_:
                            case "Yes" | "yes" | "1":
                                display_fields.append(field)
                                break
                            case "No" | "no" | "2":
                                break
                            case _:
                                print(
                                    "You did not choose one of the options. \U0001F624")
            # endregion

            # region showing students' profile
            print("Row", *display_fields, sep="\t")
            print(
                "---------------------------------------------------------------------------------")

            for id_, student in enumerate(student_list, 1):
                print(id_, end="\t")
                for field in display_fields:
                    print(getattr(student, field), end="\t")

                print()

            print(
                "---------------------------------------------------------------------------------")
            # endregion

        case "3" | "R":
            while True:
                system("cls")

                # region show student list
                print("Row", *Student._fields, sep="\t")
                print(
                    "-------------------------------------------------------------------------------")

                for id_, student in enumerate(student_list, 1):
                    print(id_, *student, sep="\t")

                print(
                    "-------------------------------------------------------------------------------")
                # endregion

                # region get which option the user want to remove a student according to
                remove_option = input(
                    "Which one do you want to remove a student according to?\
                        \n1. [N]ame\n2. [F]amily name\n3. [A]ge\n4. [G]ender\
                        \n5. [NA]tional Code\n6. [S]tudent Code\n7. [E]xit\n\U0001F449")
                system("cls")

                if remove_option not in ("1", "2", "3", "4", "5", "6", "7", "N", "F", "A", "G", "NA", "S", "E"):
                    print(
                        "You did not choose one of the options. Wait 3 seconds. \U0001F624")
                    sleep(3)
                    continue

                match remove_option:
                    case "1" | "N":
                        field = "name"
                    case "2" | "F":
                        field = "family_name"
                    case "3" | "A":
                        field = "age"
                    case "4" | "G":
                        field = "gender"
                    case "5" | "NA":
                        field = "national_code"
                    case "6" | "S":
                        field = "student_code"
                    case _:
                        break
                # endregion

                # region get value of the option the user chose
                if remove_option in ("3", "A"):
                    val = int(
                        input("Enter the value of the option you chose.\n\U0001F449"))
                    system("cls")
                else:
                    val = input(
                        "Enter the value of the option you chose.\n\U0001F449")
                    system("cls")
                # endregion

                check_exists = False

                for student in student_list[:]:
                    if getattr(student, field) == val:

                        print(*student)
                        remove_confirm = input(
                            "Are you sure you want to remove this student? 1. Yes or 2. No\n\U0001F449")
                        system("cls")

                        if remove_confirm in ("Yes", "yes", "1"):
                            student_list.remove(student)
                            print(
                                "The student is deleted successfully from the student list. \U0001F929")
                        else:
                            print(
                                "The student remained in the student list. \U0001F642")

                        check_exists = True

                if not check_exists:
                    print("The value you entered (", val,
                          ") does not exist in any student. \U0001F612")

                if input("Do you want to remove another student? 1. Yes or 2. No\n\U0001F449") not in ("Yes", "yes", "1"):
                    system("cls")
                    break

        case "4" | "F":
            while True:
                system("cls")

                # region get the option the user want to find a student according to
                find_option = input(
                    "Which one do you want to search a student according to?\
                        \n1. [N]ame\n2. [F]amily name\n3. [A]ge\n4. [G]ender\
                        \n5. [NA]tional Code\n6. [S]tudent Code\n7. [E]xit\n\U0001F449")
                system("cls")

                if find_option not in ("1", "2", "3", "4", "5", "6", "7", "N", "F", "A", "G", "NA", "S", "E"):
                    print(
                        "You did not choose one of the options. Wait 3 seconds. \U0001F62D")
                    sleep(3)
                    continue

                match find_option:

                    case "1" | "N":
                        field = "name"
                    case "2" | "F":
                        field = "family_name"
                    case "3" | "A":
                        field = "age"
                    case "4" | "G":
                        field = "gender"
                    case "5" | "NA":
                        field = "national_code"
                    case "6" | "S":
                        field = "student_code"
                    case _:
                        break
                # endregion

                # region get the value of the option the user chose
                if find_option in ("3", "A"):
                    val = int(
                        input("Enter the value of the option you chose.\n\U0001F449"))
                    system("cls")
                else:
                    val = input(
                        "Enter the value of the option you chose.\n\U0001F449")
                    system("cls")
                # endregion

                # region show the student the user searched
                print("Row", *Student._fields, sep="\t")
                print(
                    "-------------------------------------------------------------------------")

                check_exists = False
                count = 1

                for student in student_list:
                    if getattr(student, field) == val:
                        print(count, *student, sep="\t")
                        count += 1
                        check_exists = True

                if not check_exists:
                    print("The value you entered(", val,
                          ") does not exist in any student. \U0001F62D")

                print(
                    "-------------------------------------------------------------------------")
                # endregion

                if input("Do you want to search another student? 1. Yes or 2. No\n\U0001F449") not in ("Yes", "yes", "1"):
                    system("cls")
                    break

        case _:
            break
