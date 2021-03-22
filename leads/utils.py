from django.conf import settings

def outreach_links(employee_id):

    if settings.DEBUG == True:
        url = 'localhost:8000/leads/contact-us/'
    else:
        url = 'yaaconnect.com/leads/contact-us/'

    outreach_platforms = ['Facebook', 'Instagram', 'Craiglist', 'Google']

    links_dict = {}

    for p in outreach_platforms:
        p = p.lower().replace(' ', '_')
        links_dict[p] = url + p + '/' + str(employee_id)

    return links_dict