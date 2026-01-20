class chatbook:
  
  __user_id = 1

  def __init__(self):
    self.id = chatbook.__user_id
    chatbook.__user_id += 1 
    # self.__lucky = 'lucky'          ##use of encapsulation
    self.username = ''
    self.password = ''
    self.loggedin = False 
  
  @staticmethod
  def get_id():
    return chatbook.__user_id
  
  @staticmethod
  def set_id(val):
   chatbook.__user_id = val






















    # self.menu()

#   def menu(self):
#     user_input = input("""Welcome to chatbook , how would you like to proceed ?
#                        1. Press 1 to signup
#                        2. Press 2 to signin
#                        3. Press 3 to write a post
#                        4. Press 4 to message a friend
#                        5. Press any other key to exist
#                        ----> """)
#     if user_input == '1':
#       self.signup()
#     elif user_input == '2':
#       self.signin()
#     elif user_input == '3':
#       self.my_post() 
#     elif user_input == '4':
#       self.message()
#     else:
#       exit()

#   def signup(self):
#     email = input("enter your email here --> ")
#     password = input('set your password here -->')
#     self.username = email
#     self.password = password 
#     print('You have signed up successfully')
#     print('\n')
#     self.menu()

#   def signin(self):
#     if self.username =='' and self.password =='':
#        print('please signup by entering 1 in the main menu')
#     else :
#        username = input('enter your email/username here ->')
#        password = input('enter your passkey here ->')
#        if self.username == username and self.password == password:
#          print('you have signed in successfully !!')
#          self.loggedin = True
       
#        else :
#          print('please input correct credentials')

#     print('\n')
#     self.menu()     

#   def my_post(self):
#     if self.loggedin == True :
#       txt = input('enter your message here ->')
#       print(f'following content has been posted -> {txt}')
    
#     else :
#       print('you need to sigin first to post something.....')
  
#   def message(self):
#     if self.loggedin == True :
#       txt = input('enter your message here -> ')
#       frnd = input('whom to send message -> ')
#       print(f'your message has been sent to your friend {frnd}')

#     else :
#       print('you need to signin first .....')
#     print('\n')
#     self.menu()
  
    
        
    