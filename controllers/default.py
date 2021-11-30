# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------
# This is a sample controller
# this file is released under public domain and you can use without limitations
# -------------------------------------------------------------------------




# ---- example index page ----
def index():
    return dict(message=T('Welcome to LIMCO Technologies!'))
def crm_start():
    response.view="default/crm_start.html"
    return locals()
def reports():
    response.view="default/reports.html"
    return locals()

def companies():
    companies = SQLFORM.grid(db.companies)
    return locals()

def contacts():
    contacts = SQLFORM.grid(db.contacts)
    
    return locals()

def sic():
    sics = SQLFORM.grid(db.sic)
    return locals()

def locations():
    locations = SQLFORM.grid(db.locations)
    return locals()

def activities():
    activities = SQLFORM.grid(db.activities)
    return locals()

def companylocations():
    companyLocations = SQLFORM.grid(db.companies_to_locations)
    return locals()

def orders():
    orders = SQLFORM.grid(db.orders)
    return locals()



#-----------------------------------------------------

@auth.requires_login()
def company_create():
    form = SQLFORM(db.companies)
    if form.process().accepted:
        response.flash = 'Company created'
        redirect(URL('companies'))
    elif form.errors:
        response.flash = 'Form has errors'
    else:
        response.flash = 'Please fill the form'
        return locals()

@auth.requires_login()
def contact_create():
    contact_create = SQLFORM(db.contacts) 
    if contact_create.process().accepted:
        response.flash = 'Contact Created'
        redirect(URL('contacts'))
    elif contact_create.errors:
        response.flash = 'Contact not created'
    return locals()

@auth.requires_login()
def sic_create():
    form = SQLFORM(db.sic)
    if form.process().accepted:
        response.flash = 'SIC created'
        redirect(URL('sic'))
    elif form.errors:
        response.flash = 'Form has errors'
    else:
        response.flash = 'Please fill the form'
        return locals()

@auth.requires_login()
def location_create():
    form = SQLFORM(db.locations)
    if form.process().accepted:
        response.flash = 'Location created'
        redirect(URL('locations'))
    elif form.errors:
        response.flash = 'Form has errors'
    else:
        response.flash = 'Please fill the form'
        return locals()

@auth.requires_login()
def activities_create():
    form = SQLFORM(db.activity)
    if form.process().accepted:
        response.flash = 'Activity created'
        redirect(URL('activities'))
    elif form.errors:
        response.flash = 'Form has errors'
    else:
        response.flash = 'Please fill the form'
        return locals()

@auth.requires_login()
def companies_to_locations_create():
    form = SQLFORM(db.companies_to_locations)
    if form.process().accepted:
        response.flash = 'Company to Location created'
        redirect(URL('companies_to_locations'))
    elif form.errors:
        response.flash = 'Company to Location not created'
    return locals()
    
@auth.requires_login()
def company_edit():
    company = db.company(request.args(0)) or redirect(URL('companies'))
    form  = SQLFORM(db.company, company, deletable=True, showid=False)
    if form.process().accepted:
        response.flash = 'Company Edited'
        redirect(URL('companies'))
    elif form.errors:
        response.flash = 'Company not edited'
   
    return locals()


@auth.requires_login()
def contact_edit():
    contact = db.contacts(request.args(0)) or redirect(URL('contacts'))
    form = SQLFORM(db.contacts, contact, deletable=True)
    if form.process().accepted:
        response.flash = 'Contact Edited'
        redirect(URL('contacts'))
    elif form.errors:
        response.flash = 'Contact not edited'
    return locals()

@auth.requires_login()
def sic_edit():
    sic = db.sic(request.args(0)) or redirect(URL('sic'))
    form = SQLFORM(db.sic, sic, deletable=True)
    if form.process().accepted:
        response.flash = 'SIC Edited'
        redirect(URL('sic'))
    elif form.errors:
        response.flash = 'SIC not edited'
    return locals()

@auth.requires_login()
def locations_edit():
    location = db.locations(request.args(0)) or redirect(URL('locations'))
    form = SQLFORM(db.locations, location, deletable=True)
    if form.process().accepted:
        response.flash = 'Location Edited'
        redirect(URL('locations'))
    elif form.errors:
        response.flash = 'Location not edited'
    return locals()

@auth.requires_login()
def activities_edit():
    activity = db.activity(request.args(0)) or redirect(URL('activities'))
    form = SQLFORM(db.activity, activity, deletable=True)
    if form.process().accepted:
        response.flash = 'Activity Edited'
        redirect(URL('activities'))
    elif form.errors:
        response.flash = 'Activity not edited'
    return locals()

@auth.requires_login()
def companies_to_locations_edit():
    company_to_location = db.companies_to_locations(request.args(0)) or redirect(URL('companies_to_locations'))
    form = SQLFORM(db.companies_to_locations, company_to_location, deletable=True)
    if form.process().accepted:
        response.flash = 'Company to Location Edited'
        redirect(URL('companies_to_locations'))
    elif form.errors:
        response.flash = 'Company to Location not edited'
    return locals()



def user():
    return dict(form = auth())

# ---- API (example) -----
@auth.requires_login()
def api_get_user_email():
    if not request.env.request_method == 'GET': raise HTTP(403)
    return response.json({'status':'success', 'email':auth.user.email})

# ---- Smart Grid (example) -----
@auth.requires_membership('admin') # can only be accessed by members of admin groupd
def grid():
    response.view = 'generic.html' # use a generic view
    tablename = request.args(0)
    if not tablename in db.tables: raise HTTP(403)
    grid = SQLFORM.smartgrid(db[tablename], args=[tablename], deletable=False, editable=False)
    return dict(grid=grid)

# ---- Embedded wiki (example) ----
def wiki():
    auth.wikimenu() # add the wiki to the menu
    return auth.wiki() 

# ---- Action for login/register/etc (required for auth) -----
def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    http://..../[app]/default/user/bulk_register
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    also notice there is http://..../[app]/appadmin/manage/auth to allow administrator to manage users
    """
    return dict(form=auth())

# ---- action to server uploaded static content (required) ---
@cache.action()
def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)
