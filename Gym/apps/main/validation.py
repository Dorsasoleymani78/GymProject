 
from django.core.exceptions import ValidationError
 
from django.core.validators import RegexValidator

def validate_name(value):
    list1=['@','_','&','*','%','$','#','!','(',')'] 
    if len(value)>=20:
        raise ValidationError('the name is out og range..')
    elif value in list1:
            raise ValidationError('The name must contain the letters of the alphabet')
    return value
    

def validate_Address(value):
    list1=['@','_','&','*','%','$','#','!','(',')'] 
    if len(value)<=10:
        raise ValidationError('the address is so short..')
    elif value in list1:
            raise ValidationError('The addres must contain the letters of the alphabet')
    return value
        


def validate_phoneNumber(value):
    message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."
        
    if  RegexValidator(regex=r'^(\+\d{1,2}\s)?\(?\d{3}\)?[\s.-]?\d{3}[\s.-]?\d{4}$')!=value:
        raise ValidationError(message)
    return value
 
 
def validate_Capacity(value):
        val=int(value)
        if val<=10:
           raise ValidationError('ظرفیت نمی تواند کمتر از 10 باشد')
        elif val>=40:
            raise ValidationError('ظرفیت نمی تواند بیشتر از 40 باشد')
        return value
     