class Person:
    #setting name and email to private
    __name = ''
    __email = ''

    #constructor
    def __init__(self,__name,__email):
        self.__name = __name
        self.__email = __email

    #set name
    def set_name(self, __name):
        self.__name = __name
    #get name
    def get_name(self):
        return self.__name

    #set email
    def set_email(self, __email):
        self.__email = __email
    #get email
    def get_email(self):
        return self.__email

    def sentenceString(self):
        return '{} is a programmer. You can contact him at {}'.format(self.__name,self.__email)

user_info = Person('Juma','jay@me.com')

print(user_info.sentenceString())
