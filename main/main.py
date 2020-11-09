from password_generator import generate_password

if __name__ == '__main__':
    length_of_password = input("Length of password (between 4 and 20 characters): ")
    print(generate_password(int(length_of_password)))
