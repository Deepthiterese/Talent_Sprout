from django.shortcuts import render
from signUp.models import CustomUser
from services.models import Service, Service_page
from profiles.models import UserProfile
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from admin_customization.models import HeroSection, WorkStep, ContactInfo
from profiles.models import UserProfile 


@login_required
def layout_View(request):
    try:
        user_profile = UserProfile.objects.get(user=request.user)
        profile_image_url = user_profile.profile_image.url if user_profile.profile_image else None
    except UserProfile.DoesNotExist:
        profile_image_url=None 

    user_online = request.user.is_online()

    return render(request, 'main/Layout.html', {
        'profile_image_url': profile_image_url,
        'user_online': user_online,
    })

def home_view(request):
    try:
        # Fetch only users with 'candidate' role
        users = (
        UserProfile.objects.filter(user__role=CustomUser.CANDIDATE)
    .   select_related('user')
        .order_by('-level')
            )

        # Transform users into a list of dictionaries for easy use in the template
        user_data = [
             {
                 'id': user.user.id,
                 'candidate_id': user.id,
                 'first_name': user.user.first_name,
                 'last_name': user.user.last_name,
                 'profile_image': user.profile_image.url if user.profile_image else None,
                 'level': user.level if user.level else "Not Assigned",
             }
                for user in users
                    ]

        
        # Fetch all services for display and pagination
        services = Service.objects.all().order_by('id')
        paginator = Paginator(services, 6)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        # Fetch other required data
        service_pages = Service_page.objects.all()
        hero_section = HeroSection.objects.first()
        work_steps = WorkStep.objects.all()
        contact_info = ContactInfo.objects.first()

        # Render data to the template
        return render(request, 'main/Index.html', {
            'users': user_data,
            'services': services,
            'page_obj': page_obj,
            'hero_section': hero_section,
            'work_steps': work_steps,
            'contact_info': contact_info,
            'service_pages': service_pages,
        })
    except Exception as e:
        # Log the error to debug
        print(f"Error in home_view: {e}")
        return render(request, 'main/Index.html', {
            'error': f"An unexpected error occurred: {str(e)}"
        })


def custom_404(request, exception):
    return render(request, '404.html', status=404)