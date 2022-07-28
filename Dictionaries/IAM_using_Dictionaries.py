#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
# [SCRIPT DESCRIPTION]
# Simple Python Dictionary based Identity and Access Management System to create, modify, delete and verify a user 
# @author   : Aditya Saxena
# @version  : 1.0
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#


#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
# [Step 1] - Create a Python Dictionary to hold default users
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
dictionary_object = {
    "user1"     : "password1",
    "user2"     : "password2"
}
# [inline test statement] print(dictionary_object)

#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
# [Step 2] - Create a while loop to execute the IAM Script.
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
# defining a local variable to create a while loop
int_continue = 1
print('[Main Menu] Please login to perform an action!')
username = input("[Main Menu] Please enter your username : ")
password = input("[Main Menu] Please enter your password : ")

while (int_continue == 1):
    try: 
        # [Step] - Authenticate the user before any action can be processed.
        
        if (username != '' and password !=''):
            if(username in dictionary_object):
                try:
                    # [Step] - Prompting the user to select an action that he would like to perform            
                    action = int(input("[Main Menu] What are you trying to do today? (1 = List all users, 2 = Create, 3 = Update, 4 = Delete) : "))
                    action_string = ''
                    if  action == 1:
                        action_string = 'List all Users'
                    elif action == 2:
                        action_string = 'Create'
                    elif action == 3:
                        action_string = 'Update'
                    elif action == 4:
                        action_string = 'Delete'

                    # [Step] - Validate if the action selected by the user is a valid action
                    if (action == 1 or action == 2 or action == 3 or action == 4):
                        print('[Action Menu] Selected Action is : ' + action_string)
                        # [Case 1] - creating a script to list all the users
                        if (action == 1):
                            try:
                                #print(dictionary_object.keys())
                                print(dictionary_object)
                            except:
                                print('[C1][Error] - The system encountered an exception! ')
                        # [Case 2] Creating a script to add a new user to the dictionary
                        elif (action == 2):
                            try:
                                new_username = str(input('[C2] Please enter a new username : '))
                                new_password = str(input('[C2] Please enter a new password : '))
                                if new_username in dictionary_object :
                                    print ('[C2][Error] - the following user already exists in the system. Please try again with a different username! Thank You! ')
                                else :
                                    dictionary_object[new_username] = [new_password]
                                    # [inline test statement] print(dictionary_object)
                                    print('[C2][Success] - The user has been added successfully!')
                            except:
                                print('[C2][Error] - The system encountered an exception!')
                        # [Case 3] -  Creating a script to update the password of the existing user
                        elif (action == 3):
                            try:
                                new_password = input('[C3] Please input a new password for the user : ')
                                dictionary_object[username] = new_password
                            except:
                                print('[C3][Error] - The system encountered an exception')
                        # [Case 4] -  Creating a script to delete a user
                        elif (action == 4):
                            try:
                                delete_username = input('[C4] Please input a valid usename : ')
                                if(delete_username in dictionary_object and delete_username != username):
                                    delete_response = input('Do you really want to delete the user(y/n) : ')
                                    if (delete_response == 'y'):
                                        dictionary_object.pop(delete_username)
                                        print('[C4][Success] - The user has been successfully removed from the Dictionary ')
                                    elif (delete_response == 'n'):
                                        print('[C4][Notification] - Delete attempted terminated by end-user. Returning to main menu! ')
                                    elif (delete_response != 'y' or delete_response != 'n') :
                                        print('[C4][Error] - This is not a valid input. Please try again. ')
                                else:
                                    print('[C4][Error] The user does not exist in the dictionary / cannot delete the logged in user ')
                            except:
                                print('[C4][Error] - The system encountered an exception. The user could not be removed. ')        
                    else:
                        print('[Action Menu][Error] This is not a valid action! ')
                except:
                    print("[Main Menu][Exception] - Could not understand your input. Please try again. Thank You! ") 
            else:
                print('[User Authentication][Error] The user does not exist in the Dictionary. ')
        else:
            print('[Main Menu][Error] The username and password cannot be blank. ')
    except:
        print('[Main Menu][Error] The system encountered an exception. ')
    finally:
        if(username in dictionary_object):
            input_continue = input("[Main Menu] Would you like to continue? (y/n) : ")
            try:
                if (input_continue == 'y'):
                    int_continue = 1
                elif (input_continue == 'n'):
                    int_continue = 0
                    break
                else :
                    print('[Main Menu][Error] This is not a valid response! ')
            except:
                print('[Main Menu][Error] - The system encountered an exception. Please try again.')
        else:
            print('[Main Menu] Please login to perform an action!')
            username = input("[Main Menu] Please enter your username : ")
            password = input("[Main Menu] Please enter your password : ")



