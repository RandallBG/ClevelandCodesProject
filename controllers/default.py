# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------
# This is a sample controller
# this file is released under public domain and you can use without limitations
# -------------------------------------------------------------------------


from gluon.tools import Crud
crud = Crud(db)

# ---- example index page ----
def index():
    response.flash = T("Hello World")
<<<<<<< HEAD
    return dict(message=T('Welcome to LIMCO Technologies!'))
=======
    return dict(message=T('Welcome to Limco Technologies!'))
>>>>>>> bbd8fdd0193c242fb8d4f35786cf27463179e83a

# def index():
#     response.view="index.html"
#     return locals()

def companies():
    companies = db(db.company).select(orderby = db.company.name)
    #response.view="companies.html"
    return locals()

def contacts():
    contacts = db(db.contacts).select(orderby = db.contacts.name)
    #response.view="contacts.html"
    return locals()


# def contacts():
#     company = db.company(request.args(0)) or redirect(URL('companies'))
#     contacts = db(db.contact.company == company.id).select(orderby = db.contact.name)
#     return locals()

@auth.requires_login()
def company_create():
    form = crud.create(db.company, next = 'companies')
    return locals()

@auth.requires_login()
# def contact_create():
#     form = crud.create(db.contacts, next='people')

@auth.requires_login()
def company_edit():
    company = db.company(request.args(0)) or redirect(URL('companies'))
    form = crud.update(db.company, company, next='companies')
    return locals()

@auth.requires_login()
def contact_create():
    # db.contacts.company.default = request.args(0)
    form = crud.create(db.contacts, next = 'contacts')
    return locals()

@auth.requires_login()
def contact_edit():
    contact = db.contacts(request.args(0)) or redirect(URL('contacts'))
    form = crud.update(db.contacts, contact, next = 'contacts')
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
