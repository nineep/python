import pwd
import crypt
import logging
from pecan import conf as CONF
from pecan import expose, response
from pecan.rest import RestController
from jinja2 import Environment, PackageLoader
from winterfell.controllers.common import check_call, render_ldif
from winterfell import exception


logger = logging.getLogger(__name__)


class UserController(RestController):

    @expose('json')
    def put(self, name, **kw):
        try:
            ldif_context = {'name': name,
                            'user': kw['user'],
                            'ldap_people_ou': CONF.ldap_people_ou}
            update_user_ldif = '%s/%s.ldif' % ('/tmp', name)
            render_ldif('ch_user_.ldif.j2', updated_user_ldif, ldif_context)
            ldap_update_cmd = "ldapadd -x -D %s -w %s -f %s" \
                        %(CONF.ldap_admin_dc, CONF.ldap_admin_password,
                          updated_user_ldif)
            check_all(ldap_update_cmd)
        except:
            raise exception.UpdateUserFail(name=name, step='ldap')

    @expose('json')
    def get_one(self, username):
        if not validate_user(username):
            raise exception.UserIsExist(username=username)
        return get_user_info(username)

    @expose('json')
    def post(self, username, password=''):
        if not password:
            password = CONF.user_default_password
        if validate_user(username):
            raise exception.UserIsExsit(username=username)

        create_user(username, password)
        response.status = 201
        return 'create user %s sucess' % username

    @expose('json')
    def delete(self, username):
        delete_user(username)
        response.status = 204
        return 'delete user %s sucess' % username


def get_user_info(username):
    user_info = {'username': username}

    #Get google authenticator key
    google_auth_path = '/home/%s/.google_authenticator' % username
    with open(google_auth_path, 'r') as auth_file:
        google_auth_key = auth_file.readline()[:-1]

    user_info['google_auth_key'] = gogle_auth_key

    return user_info

def delete_user(username):
    if validate_user(username):
        delete_system_user(username)
    try:
        delete_ldap_user(username)
    except:
        raise exception.DeleteUserFail(username=username,
                                       step='ldap')

def delete_system_user(username):
    system_delete_cmd = "userdel %s -r" % username
    try:
        check_call(systemctl_delete_cmd)
    except:
        raise exception.DeleteUserFail(username=username,
                                       step='system')

def delete_ldap_user(username):
    ldap_delete_cmd = "ldapdelete -x -D %s -w %s uid=%s,%s" \
            % (CONF.ldap_admin_dc, CONF.ldap_admin_password,
               username, CONF.ldap_people_ou)
    check_call(ldap_delete_cmd)

def create_ldap_user(username):
    user_ldif_path = generate_user_ldif_file(username)
    ldap_create_cmd = "ldapadd -x -D %s -w %s -f %s" \
            % (CONF.ldap_admin_dc, CONF.ldap_admin_password,
               user_ldif_path)
    check_call(ldap_create_cmd)

def create_user(username, password):
    # create user on linux system
    hash_password = crypt.crypt(password)
    create_user_cmd = "adduser %s -p '%s'" % (username, hash_password)
    try:
        check_call(create_user_cmd)
    except:
        raise exception.CreateUserFail(username=username, step='linux system')

    # generate google authenticator key
    try:
        genarate_google_key_cmd = 'su %s -c "google_authenticator -t -d \
                    -f -r 1 -R 15 -w 3"' % username
        check_call(generate_google_key_cmd)
    except:
        delete_system_user(username)
        raise exception.CreateUserFail(username=username,
                                       step='generate google-auth key')
    
    # create user on ldap
    try:
        create_ldap_user(name)
    except:
        delete_system_user(username)
        raise exception.CreateUserFail(username=username, step='ldap')

def validate_user(username):
    try:
        pwd.getpwnam(username)
        return True
    except KeyError:
        return False


def generate_user_ldif_file(username):
    env = Environment(loader=PackageLoader('winterfell', 'templates'))
    template = env.get_template('user.ldif.j2')
    conf = template.render(username=username,
                           ldap_people_ou=CONF.ldap_people_ou,
                           mail_suffix=CONF.mail_suffix)
    conf_file_name = '%s/%s.ldif' % (CONF.ldif_path, username)
    with open(conf_file_name, 'w') as conf_file:
        conf_file.write(conf)
    return conf_file_name
    
