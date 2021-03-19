from django.conf import settings

def outreach_links():

    if settings.DEBUG == True:
        url = 'localhost:8000'
    else:
        url = 'yaaconnect.com'

    outreach_platforms = ['Facebook', 'Instagram', 'Craiglist', 'Google']

    links_dict = {}

    for p in outreach_platforms:
        p = p.lower().replace(' ', '_')
        links_dict[p] = url + '/' + p

    return links_dict