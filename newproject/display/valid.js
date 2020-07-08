 import authenticate from django.contrib.auth;
 import forms from django;
function validationForm(request){
    var  name=document.myform.name.value;
    var  password=document.myform.password.value;
    if (Name && Password){
        user = authenticate(Name=Name, Password=Password)
        print(user)
        if ( !user){
            print('this user does not exists')
        }
            
        // else if (not user.check_password(Password):
        //     raise forms.ValidationError('this user does exists but password is wrong')
        // elif not user.is_active:
        //     raise forms.ValidationError('this user is already active')
        // else:
        //     return render(request, 'temp.html')
            
    }

}



  