from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name = "index"),

   

    path('register_page/', register_page, name = "register_page"),
    path('register/', register, name = "register"),

    path('login_page/', login_page, name='login_page'),
    path('login/', login, name='login'),

  
   
    # SEND OTP, OTP PAGE, VERIFIY OTP AND FUNCTIOALITY
    path('otp_page/', otp_page, name='otp_page'), 

    path('verify_otp/<str:verify_for>/',verify_otp, name='otp_verify'),
    path('profile_page/', profile_page, name='profile_page'),  
    path('profile_update/', profile_update, name='profile_update'),
   
    path('department_profile', department_profile, name='department_profile'),
    
    path('citizen_profile/', citizen_profile, name = "citizen_profile"),
    path('citizen_connect/', citizen_connect, name = "citizen_connect"),

   
    path('complaint/', complaint, name = "complaint"),

    path("signout/", signout, name="signout"),

    path('complaint_view/', complaint_view, name = 'complaint_view'),

    path('officer_list/',officer_list, name = 'officer_list'),
    
    path('traffic_education/',traffic_education, name = 'traffic_education'),
    path('public_interface/',public_interface, name = 'public_interface'),
    path('emergency_dailing/', emergency_dailing, name= 'emergency_dailing'),
    path('community_policing/',community_policing, name= 'community_policing'),
    path('do_dont/',do_dont, name = 'do_dont'),
    
    path('citizen_rights/',citizen_rights, name = 'citizen_rights'),
    path('women_rights/',women_rights, name = 'women_rights'),
    path('children_rights/',children_rights, name = 'children_rights'),
    path('arrest_rights/',arrest_rights, name = 'arrest_rights'),
    path('prisoner_rights/',prisoner_rights, name = 'prisoner_rights'),
    path('duties_rights/',duties_rights, name = 'duties_rights'),

    path('contact_us/', contact_us, name = 'contact_us'),

    path('history/', history, name = "history"),
    path('ourgoal/',ourgoal, name = 'ourgoal'),
    path('hierarchy/', hierarchy, name = 'hierarchy'),

    path('who_is_who/', who_is_who, name = "who_is_who"),
    path('children_safety/', children_safety, name = "children_safety"),
    path('women_safety/', women_safety, name = "women_safety"),
    path('senior_citizen_safety/', senior_citizen_safety, name = "senior_citizen_safety"),
    path('road_safety/', road_safety, name = "road_safety"),
    path('vehicale_safety/', vehicale_safety, name = "vehicale_safety"),
    path('mobile_safety/', mobile_safety, name = "mobile_safety"),
    path('internet_safety/', internet_safety, name = "internet_safety"),
   
    path('e_fir_page/', e_fir_page, name = "e_fir_page"),
    path('fir_view/', fir_view, name = "fir_view"),

    path('lost_parson/', lost_parson, name = "lost_parson"),
    path('lost_parsons_view/', lost_parsons_view, name = "lost_parsons_view"),

    path('report/', report, name = "report"),
    path('report_veiw/', report_view, name = "report_view"),

    path('police_varification/', police_varification, name = "police_varification"),
    path('police_verification_view/', police_verification_view, name = "police_verification_view"),

    path('accident/', accident, name = "accident"),
    path('accident_view/', accident_view, name = "accident_view"),

    path('passport_status/', passport_status, name = "passport_status"),
    path('passport_status_view/', passport_status_view, name = "passport_status_view"),

    path('go_message/', go_message, name = "go_message"),
    path('cm_message/', cm_message, name = "cm_message"),



]