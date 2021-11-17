db.define_table('contacts', 
    Field('contact_id', notNull = True, unique=True),
    Field('name', notNull = True),
    Field('home_address', notNull = True),
    Field('home_city', notNull = True),
    Field('home_state', notNull = True),
    Field('home_zip', notNull = True),
    Field('company_id', notNull = True),
    Field('title', notNull = True),
    Field('office_phone'),
    Field('cell_phone'),
    Field('location_id', notNull = True),
    Field('email', notNull = True),
    Field('contact_type_id', notNull = True),
    format='%(name)s'
)

db.define_table('lead_source',
    Field('lead_source_id', notnull=True),
    Field('description', notnull=True),
    format='%(name)s'
)


   