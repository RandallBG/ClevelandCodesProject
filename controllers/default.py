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


def crm_start():
    response.view = "default/crm_start.html"
    return locals()


def our_team():
    response.view = "default/our_team.html"
    return locals()


def products():
    response.view = "default/products.html"
    return locals()


def scheduled_events():
    events = SQLFORM.grid(db.activities.activity_date >= datetime.date.today())
    return locals()


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
    activities = db(db.activities).select()
    jsonActivities = json(db(db.activities).select())
    activityType = db(db.activity_type).select()
    jsonActivityType = json(db(db.activity_type).select())
    contacts = db(db.contacts).select()
    jsonContacts = json(db(db.contacts).select())

    response.view = "default/dashboard.html"
    return locals()


def reports():
    response.view = "default/reports.html"
    return locals()


def companies():
    companies = SQLFORM.grid(db.companies)
    return locals()


def contacts():
    contacts = SQLFORM.grid(db.contacts)
    return locals()


def employees():
    employees = SQLFORM.grid(db.employees)
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
    else:
        response.flash = 'Please fill the form'
    return locals()


@auth.requires_login()
def contact_create():
    states = db(db.states).select(orderby=db.states.state_name)
    companies = db(db.companies).select(orderby=db.companies.company_name)
    contactType = db(db.contact_type).select(
        orderby=db.contact_type.description)
    form = SQLFORM(db.contacts)
    if form.process(session=None, formname='test').accepted:
        response.flash = 'form accepted'
        redirect(URL('contacts'))
    elif form.errors:
        response.flash = form.errors
    else:
        response.flash = 'please fill the form'
    # Note: no form instance is passed to the view
    return locals()


@auth.requires_login()
def employee_create():
    states = db(db.states).select(orderby=db.states.state_name)
    form = SQLFORM(db.employees)
    if form.process(session=None, formname="employeeCreate").accepted:
        response.flash = 'Employee created'
        redirect(URL('employees'))
    elif form.errors:
        response.flash = form.errors
    else:
        response.flash = 'Please fill the form'
    return locals()


@auth.requires_login()
def order_create():
    employees = db(db.employees).select(orderby=db.employees.employee_name)
    customers = db(db.contacts).select(orderby=db.contacts.name)
    form = SQLFORM(db.orders)
    if form.process(session=None, formname="createOrder").accepted:
        response.flash = 'Order created'
        redirect(URL('orders'))
    elif form.errors:
        response.flash = form.errors
    else:
        response.flash = 'Please fill the form'
    return locals()


@auth.requires_login()
def sic_create():
    form = SQLFORM(db.sic)
    if form.process(session=None, formname="sicCreate").accepted:
        response.flash = 'SIC created'
        redirect(URL('sic'))
    elif form.errors:
        response.flash = Form.errors
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
    employees = db(db.employees).select(orderby=db.employees.employee_name)
    contacts = db(db.contacts).select(orderby=db.contacts.name)
    form = SQLFORM(db.activities)
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
def orders_create():
    form = SQLFORM(db.orders)
    if form.process().accepted:
        response.flash = 'Order created'
        redirect(URL('orders'))
    elif form.errors:
        response.flash = 'Order not created'
    return locals()


def contact_type_create():
    form = SQLFORM(db.contact_type)
    if form.process(session=None, formname="contactTypeCreate").accepted:
        response.flash = 'Contact Type created'
        redirect(URL('contact_type'))
    elif form.errors:
        response.flash = form.errors
    else:
        response.flash = 'Please fill the form'
    return locals()


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
