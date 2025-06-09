from django.shortcuts import render
from .models import Post, Invite, Friendship
from django.contrib.auth.models import User
from django.core.mail import send_mail
from logging import getLogger



def index(request):

    if request.method == 'POST':
        # senha = request.POST['reset-password']
        # user = User.objects.get(id=request.user.id)
        # user.set_password(senha)
        # user.save()

        send_mail(
            subject='Teste SENAI',
            message='Email de teste',
            recipient_list=['wcaio41@gmail.com'],
            from_email='wcaio41@gmail.com'
        )

        return render(request, 'pages/index.html')

        

    else:
        return render(request, 'pages/index.html')


# def envio_de_convites(request):
#     pass

#     meus_convites = Invite.objects.filter(reciever_id=request.user)

#     meus_convites.status = "APROVED" 
    
    # Friendship.objects.create(
    #     sender=meus_convites.sender.
    # )

# def alterar_status(request, id):
#     meus_convites = Invite.objects.filter(id=id)


