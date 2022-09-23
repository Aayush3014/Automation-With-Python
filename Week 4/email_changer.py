def email_changer(email,old_domain,new_domain):
    if "@" + old_domain in email:
        index1 = email.index("@"+old_domain)
        new_email = email[:index1]+"@"+new_domain
        return new_email
    return email