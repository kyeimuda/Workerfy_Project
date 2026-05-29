from django.shortcuts import render, redirect
from .forms import TradespersonOnboardingForm, ProfileEditPageform, CertificateForm, PortfolioForm, JobPostForm
from django.contrib.auth.decorators import login_required
from MainWorkerfy.models import TradespersonProfile, City, Area, TradeCategory, TradeSpecialty, TradeSkillTag, Region, Certificate, PortfolioItem, JobPost, JobPostAttachment\
, Notification, ClientProfile
from django.contrib.auth import get_user_model
from django.contrib import messages
import json
from .validators import validate_user_role
from django.core.exceptions import ValidationError
import datetime


User = get_user_model()

# Create your views here.

def forms(request):
    """
    This view renders the forms page.
    """
    if request.method == 'POST':
        # Handle form submission logic here if needed
        pass

    # Render the forms template
    form = TradespersonOnboardingForm()

    return render(request, 'main/forms.html', {'form': form})


# This view handels the work page
@login_required
def More_Page(request):
     return render(request, 'main/TradespeopleMorePage.html')

# This view handels the work page
@login_required
def Notifications_Page(request):
     return render(request, 'main/TradespeopleNotificationsPage.html')

# This view handels the work page
@login_required
def Discover_Page(request):
     return render(request, 'main/TradespeopleDiscoverPage.html')

# This view handels the work page
@login_required
def Profile_Page(request):
     user = TradespersonProfile.objects.filter(user = request.user).first()
     return render(request, 'main/TradespeopleProfilePage.html', {'user': user})

# This view handels the Profile page
@login_required
def Work_Page(request):
     return render(request, 'main/TradespeopleWorkPage.html')

# This view handles the Discover page
@login_required
def Main_page(request):
    print(request.user.id)
    user = User.objects.get(id=request.user.id)
    Tradespeople = TradespersonProfile.objects.all()
    print(user.user_type)

    if user.user_type == "Tradesperson":
        context = {
            'User': user,
            'Tradespeople': Tradespeople,
            'user': user.tradesperson_profile,
            'Jobposts': JobPost.objects.all().order_by('-created_at'),
            'TradesType': TradeCategory.objects.all(),
            'portfolio_items': PortfolioItem.objects.filter(tradesperson=user.tradesperson_profile).order_by('-created_at').all(),
        }
        return render(request, 'main/mainPageTradesperson.html', context)

    elif user.user_type == "Client":
        context = {
            'Client': Tradespeople, # Note: Verify if this should be ClientProfile objects instead
            'user': user.client,
            'Jobposts': JobPost.objects.all().order_by('-created_at'),
            'TradesType': TradeCategory.objects.all()
        }
        return render(request, 'main/mainPageClient.html', context)
    
    messages.error(request, 'User does not have a valid role. Must be Tradesperson, Client, or Admin')
    return redirect('Onboardings')


@login_required
def TradespersonProfileEdit(request):
    def safe_capitalize(val):
        return val.capitalize() if isinstance(val, str) and val else ""

    if request.method == "POST":
        print(request.POST)
        form = ProfileEditPageform(request.POST, request.FILES)
        certForm = CertificateForm(request.POST, request.FILES)
        portfolioForm = PortfolioForm(request.POST, request.FILES)

        if form.is_valid() and certForm.is_valid() and portfolioForm.is_valid():
            print(form.cleaned_data)

        return render(request, 'main/TradespeopleProfilePage.html')



    else:
        print(request.user)
        trades_profile = TradespersonProfile.objects.get(user = request.user)

        context = {
            'form': ProfileEditPageform(user=trades_profile),
            'user': trades_profile,
        }
        print(context['user'].first_name, context)

    return render(request, 'main/TradespersonProfileEdit.html', context)

@login_required
def job_Post_Page(request):
    if request.method == "POST":
        jobPostForm = JobPostForm(request.POST, request.FILES)
        jobAttachments = request.FILES.getlist('imageUpload')

        print(jobAttachments)

        if jobPostForm.is_valid():


            Job = JobPost(user = request.user)
            print(jobPostForm.cleaned_data)

            for key, value in jobPostForm.cleaned_data.items():
                if key == "required_skills":
                    value = value.split(",")
                    if value[-1] == "":
                        value.pop()
                    
                elif key == "requirements":
                    value = value.split(",,")
                    if value[-1] == "":
                        value.pop()

                print(key, value)
                setattr(Job, key, value)

            Job.save()  # Save the Job instance before adding attachments

            for attachment in jobAttachments:
                jobAttachment = JobPostAttachment(job_post=Job, file=attachment)
                jobAttachment.save()
                

            return redirect('jobPostPage')
        else:
            print(jobPostForm.errors)
            return render(request, 'main/jobPostpage.html', {"form":jobPostForm, "errors": jobPostForm.errors})
    else:
        form=JobPostForm()
        user = TradespersonProfile.objects.get(user = request.user)
        return render(request, 'main/jobPostpage.html', {"form":form, "user":user})
    
@login_required
def jobPostDetailsPage(request, id):
    job = JobPost.objects.get(id=id)
    JobPostAttachments = JobPostAttachment.objects.filter(job_post=job)

    print(JobPostAttachments)

    user = User.objects.get(id=request.user.id)
    if user.user_type == "Tradesperson":
        user_profile = TradespersonProfile.objects.get(user=user)
    elif user.user_type == "Client":
        user_profile = ClientProfile.objects.get(user=user)

    for attachment in JobPostAttachments:
        print(attachment.file.url)

    context = {
        'job': job,
        'attachments': JobPostAttachments,
        'user': user_profile
    }
    return render(request, 'main/jobPostDetails.html', context)

# This view handels the adding certificates for tradespeople
@login_required
def add_Certificate_Page(request):
    if request.method == "POST":
        certForm = CertificateForm(request.POST, request.FILES)

        if certForm.is_valid():
            user = TradespersonProfile.objects.get(user = request.user)
            Cert = Certificate(tradesperson = user)

            for key, value in certForm.cleaned_data.items():
                 print(key,value)
                 setattr(Cert, key, value)

            Cert.save()

            return redirect('Profile_Page')
        else:
            print(certForm.errors)
            return render(request, 'main/certificateAddPage.html', {"form":certForm, "errors": certForm.errors})
    form = CertificateForm()
    return render(request, 'main/certificateAddPage.html', {"form": form})

# This view handels the adding postfolio items for tradespeople
@login_required
def add_Portfolio_Item_Page(request):
    if request.method == "POST":
        portfolioForm = PortfolioForm(request.POST, request.FILES)

        if portfolioForm.is_valid():
            user = TradespersonProfile.objects.get(user=request.user)
            item = PortfolioItem(tradesperson=user)

            for key, value in portfolioForm.cleaned_data.items():
                print(key, value)
                setattr(item, key, value)

            item.save()

            return redirect('MainPage')
        else:
            print(portfolioForm.errors)
            return render(request, 'main/portfolioaddPage.html', {"portfolioForm": portfolioForm, "errors": portfolioForm.errors})
    
    portfolioForm = PortfolioForm()
    return render(request, 'main/portfolioaddPage.html', {"portfolioForm": portfolioForm})

@login_required
def tradesperson_View_Page(request, id):
    tradesperson = TradespersonProfile.objects.get(user=request.user)

    context = {
        'user': tradesperson,     
    }

    return render(request, 'main/tradespersonViewPage.html', context)


@login_required
def notification_Page(request, id):
        notification = Notification.objects.get(id=id)
        notification.is_read = True
        notification.save()

        context = {
            'notification': notification
        }
        
        return render(request, 'main/notificationPage.html', context)
