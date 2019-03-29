from winterfell import hooks

# Server specific configurations
server = {
    'port': '9091',
    'host': '0.0.0.0'
}


# Pecan Application configurations
app = {
    'root': 'winterfell.controllers.root.RootController',
    'modules': ['winterfell'],
    'static_root': '%(confdir)s/public',
    'template_path': '%confdir)s/winterfell/templates',
    'debug': True,
    'errors': {
        404: '/error/404',
        '__force_dict__': True
    }
}

user_default_password = ''
mail_suffix = ''

ldif_path = '/root/ldap'

fatal_exception_format_errors = False

ldap_server_url = ''
ldap_admin_dc = ''
ldap_admin_password = ''
ldap_people_ou = ''
ldap_group_ou = ''

admin_token = ''
