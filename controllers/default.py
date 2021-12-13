# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------
# This is a sample controller
# this file is released under public domain and you can use without limitations
# -------------------------------------------------------------------------
import datetime
from gluon.serializers import json


# ---- example index page ----
def index():
    return dict(message=T('Welcome to LIMCO Technologies!'))

@auth.requires_login()
def crm_start():
    response.view = "default/crm_start.html"
    return locals()


def our_team():
    response.view = "default/our_team.html"
    return locals()


def products():
    response.view = "default/products.html"
    return locals()

def about():
    response.view="default/about.html"
    return locals()

def products():
    response.view="default/products.html"
    return locals()

def specs1():
    response.view="default/specs1.html"
    return locals()

def specs2():
    response.view="default/specs2.html"
    return locals()

def specs3():
    response.view="default/specs3.html"
    return locals()

def lists():
    response.view="default/lists.html"
    return locals()



def scheduled_events():
    events = SQLFORM.grid(db.activities.activity_date >= datetime.date.today())
    return locals()

def leads():
    leads = SQLFORM.grid(db.leads)
    return locals()

@auth.requires_login()
def dashboard():

    # store upcoming activities, the activity types table, and the contacts table in three seperate variables
    # not sure if declaring all the variables and just returning locals is bad practice but for now it works.
    # activities = db(db.activities.activity_date >= datetime.date.today()).select(orderby= db.activities.activity_date)
    try:
        assoc_emp_id = db(db.employees.employee_account_number == auth.user.id).select().first().id
    except:
        assoc_emp_id = 0
    
    authAccount = db(db.auth_user.id == auth.user_id).select()

    #send the activities and Json activities of the logged in user
    activities = db(db.activities.account_manager == assoc_emp_id).select()
    jsonActivities = json(db(db.activities).select())

    #send the leads associated with the employee account of the logged in user
    leads = db(db.leads.account_manager == assoc_emp_id).select()
    leadType = db(db.lead_source).select()

    #send the activity type variables as python and json
    activityType= db(db.activity_type).select()
    jsonActivityType = json(db(db.activity_type).select())
    
    # send the contact variables as python and json
    contacts = db(db.contacts).select()
    jsonContacts = json(db(db.contacts).select())


    response.view = "default/dashboard.html"
    return locals()


def reports():
    response.view = "default/reports.html"
    return locals()

def rand_thing():
    thing = SQLFORM.smartgrid(db.contacts ,linked_tables=['companies', 'locations'])
    return locals()

def companies():
    companies = SQLFORM.grid(db.companies)
    return locals()


def contacts():
    contacts = SQLFORM.grid(db.contacts)
    return locals()


def employees():
    employees = SQLFORM.grid(db.employees, fields=[db.employees.first_name, db.employees.last_name, db.employees.employee_title, db.employees.employee_account_number, db.employees.picture, db.employees.employee_phone, db.employees.employee_email, db.employees.employee_address, db.employees.employee_city, db.employees.employee_state, db.employees.employee_zip,  db.employees.employee_notes, db.employees.employee_hire_date])
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

def history():
    history = SQLFORM.grid(db.activities.activity_date < datetime.date.today())
    return locals()

# -----------------------------------------------------

@auth.requires_login()
def company_create():
    sics = db(db.sic).select(orderby=db.sic.sic_id)
    form = SQLFORM(db.companies)
    if form.process(session=None, formname="companyCreate").accepted:
        response.flash = 'Company created'
        redirect(URL('companies'))
    elif form.errors:
        response.flash = form.errors
    return locals()


@auth.requires_login()
def contact_create():
    locations=db(db.locations).select()
    states = db(db.states).select(orderby=db.states.state_name)
    companies = db(db.companies).select(orderby=db.companies.company_name)
    contactType = db(db.contact_type).select(
        orderby=db.contact_type.description)
    form = SQLFORM(db.contacts)
    if form.process(session=None, formname='test').accepted:
        response.flash = 'form accepted'
        #redirect(URL('contact_create'))
    elif form.errors:
        response.flash = form.errors
    
    # Note: no form instance is passed to the view
    return locals()

def activity_type_create():
    form = SQLFORM(db.activity_type)
    if form.process(session=None, formname="activity_type_create").accepted:
        response.flash = 'Activity Type created'
    elif form.errors:
        response.flash = form.errors
    return locals()

@auth.requires_login()
def employee_create():
    authAccounts = db(db.auth_user).select(orderby=db.auth_user.id)
    states = db(db.states).select(orderby=db.states.state_name)
    form = SQLFORM(db.employees)
    if form.process(session=None, formname="employeeCreate").accepted:
        response.flash = 'Employee created'
        #redirect(URL('employees'))
    elif form.errors:
        response.flash = form.errors
    return locals()


@auth.requires_login()
def order_create():
    employees = db(db.employees).select(orderby=db.employees.last_name)
    contacts = db(db.contacts).select(orderby=db.contacts.last_name)
    form = SQLFORM(db.orders)
    if form.process(session=None, formname="createOrder").accepted:
        response.flash = 'Order created'
        #redirect(URL('orders'))
    elif form.errors:
        response.flash = form.errors
    return locals()


@auth.requires_login()
def sic_create():
    form = SQLFORM(db.sic)
    if form.process(session=None, formname="sicCreate").accepted:
        response.flash = 'SIC created'
        #redirect(URL('sic'))
    elif form.errors:
        response.flash = Form.errors
    return locals()


@auth.requires_login()
def location_create():
    states = db(db.states).select(orderby=db.states.state_name)
    companies = db(db.companies).select(orderby=db.companies.company_name)
    form = SQLFORM(db.locations)
    if form.process().accepted:
        response.flash = 'Location created'
        #redirect(URL('locations'))
    elif form.errors:
        response.flash = 'Form has errors'
    
    return locals()

def lead_create():
    states = db(db.states).select(orderby=db.states.state_name)
    employees = db(db.employees).select(orderby=db.employees.last_name)
    form = SQLFORM(db.leads)
    if form.process().accepted:
        response.flash = 'Lead created'
        #redirect(URL('leads'))
    elif form.errors:
        response.flash = 'Form has errors'
    
    return locals()


@auth.requires_login()
def activities_create():
    employees = db(db.employees).select(orderby=db.employees.last_name)
    contacts = db(db.contacts).select(orderby=db.contacts.last_name)
    activityType = db(db.activity_type).select()
    form = SQLFORM(db.activities)
    if form.process(session=None, formname="activitiesCreate").accepted:
        response.flash = 'Activity created'
        #redirect(URL('activities'))
    elif form.errors:
        response.flash = form.errors
    return locals()



def contact_type_create():
    form = SQLFORM(db.contact_type)
    if form.process(session=None, formname="contactTypeCreate").accepted:
        response.flash = 'Contact Type created'
        #redirect(URL('contact_type'))
    elif form.errors:
        response.flash = Form.errors
    else:
        response.flash = 'Please fill the form'
    return locals()
#------------------------------------------------------------------------------------------------------------------

@auth.requires_login()
def company_edit():
    company = db.company(request.args(0)) or redirect(URL('companies'))
    form = SQLFORM(db.company, company, deletable=True, showid=False)
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
    company_to_location = db.companies_to_locations(
        request.args(0)) or redirect(URL('companies_to_locations'))
    form = SQLFORM(db.companies_to_locations,
                   company_to_location, deletable=True)
    if form.process().accepted:
        response.flash = 'Company to Location Edited'
        redirect(URL('companies_to_locations'))
    elif form.errors:
        response.flash = 'Company to Location not edited'
    return locals()


@auth.requires_login()
def orders_edit():
    order = db.orders(request.args(0)) or redirect(URL('orders'))
    form = SQLFORM(db.orders, order, deletable=True)
    if form.process().accepted:
        response.flash = 'Order Edited'
        redirect(URL('orders'))
    elif form.errors:
        response.flash = 'Order not edited'
    return locals()


def user():
    return dict(form=auth())

# ---- API (example) -----


@auth.requires_login()
def api_get_user_email():
    if not request.env.request_method == 'GET':
        raise HTTP(403)
    return response.json({'status': 'success', 'email': auth.user.email})

# ---- Smart Grid (example) -----


# can only be accessed by members of admin groupd
@auth.requires_membership('admin')
def grid():
    response.view = 'generic.html'  # use a generic view
    tablename = request.args(0)
    if not tablename in db.tables:
        raise HTTP(403)
    grid = SQLFORM.smartgrid(db[tablename], args=[
                             tablename], deletable=False, editable=False)
    return dict(grid=grid)

# ---- Embedded wiki (example) ----


def wiki():
    auth.wikimenu()  # add the wiki to the menu
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
