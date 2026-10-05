correct_username = "admin"
correct_password = "1234"

username = input("enter username:")
password = input("enter password:")


if username == correct_username and password == correct_password:
  print("Login successful!")
else:
  print("invalid username or password.")