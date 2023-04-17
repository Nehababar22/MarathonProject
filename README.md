# MarathonProject

1] Extend User Model -

      Added below fields in User Model(All fields should be mandatory)
      • date_of_birth
      • phone_number
      • street
      • city
      • state
      • country
      
2] Created User CRUD API - 
 
       1. Create/POST API - 
          • Should be accessible by anyone
          • User should receive an email verification link along with success message.
          • Activate User account API
          • After clicking on activation link, user account should be activated and user should receive success message.
          
       2. Read/GET API - 
          • User should only read his own details, write a permission which only return logged-in user details.
          • Should only return logged-in user detail.
         
       3. Update/PUT/PATCH API - 
          • User should able to update only his details.
          • If user try to update any other user details, display error message.
         
       4. DELETE API
          • User should able to delete only his account.
          • If user try to delete any other user account, display error message.
          
3]  Unit Test Case for CRUD API.

4] Created a Custom Login API - 

      1. Implemented Token Based Authentication
      2. Implemented Successful Login API should return
          • Token Key
          • User Id
          • Date of Birth
        
5] Created a Logout API using Rest-auth library - 

      1. Successful Logout API should delete the existing token key.
    
6] Created a Forgot Password API - 

      1. Forgot Password API should accept email/username.
      2. It should check whether user exist with provided email/username.
      3. If user doesn’t exist show error message.
      4. If user exist send a password reset link.
      
7] Created a Reset Password API - 

      1. After clicking on password reset link user should be able to pass - 
              1. UUID
              2. Token
              3. Password_1
              4. Password_2
      2. Add validation for password_1 and password_2
      3. Once user confirm the password change show the success message and user should be able to Login with the new password.
      
8] Created a Set Password API - 

      1. Logged-in user should be able to reset his password
      2. User can reset his password providing the old_password
      3. User should be able to pass - 
              1. old_password
              2. Password_1
              3. Password_2
      4. Add validation for password_1 and password_2
      5. Once user confirm the password change show the success message and from the next login session user should be able to Login with the new password only.
