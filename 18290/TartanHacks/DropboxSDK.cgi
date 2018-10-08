# Include the Dropbox SDK libraries
from dropbox import client, rest, session
import webbrowser
import os

def thumbnail(c_lient, filepath):
    pic = c_lient.thumbnail(filepath, size = 'medium', format = '.jpg')
    return pic


def get_args():
    a = open('jpg_l.txt')
    l = a.read()
    l = l.split(', ')
    a.close()
    b = open('txt_l.txt')
    k = b.read()
    k = k.split(', ')
    b.close()
    return l, k

def extension_parsing(ld, lf):
    jpg_l = []
    txt_l = []
    anon = []
    for i in xrange(0, len(lf) - 1):
        root, extension = os.path.splitext(lf[i])
        if (extension == '.JPEG') or (extension == '.PNG'):
            jpg_l += [lf[i]]
        elif (extension == '.txt') or (extension == '.rtf'):
            txt_l += [lf[i]]
        else:
            anon += [lf[i]]
    return jpg_l, txt_l, anon
                
def dirdirdir(c_lient, metadata):
    ldir = []
    lfile = []
    for d in metadata['contents']:
        if d['is_dir']:
            ldir += [d['path']]
            metad = c_lient.metadata(d['path'])
            (tempdir, tempfile) = dirdirdir(c_lient, metad)
            ldir = ldir + tempdir
            lfile = lfile + tempfile
        else:
            lfile += [d['path']]
    return (ldir, lfile)


def dropboxAuthentication():
    # Get your app key and secret from the Dropbox developer website
    APP_KEY = '55mttye1vckcymk'
    APP_SECRET = '75inb8137sdffsl'

    # ACCESS_TYPE should be 'dropbox' or 'app_folder' as configured for your app
    ACCESS_TYPE = 'dropbox'

    sess = session.DropboxSession(APP_KEY, APP_SECRET, ACCESS_TYPE)

    request_token = sess.obtain_request_token()

    url = sess.build_authorize_url(request_token, 'http://www.contrib.andrew.cmu.edu/~pwei/TartanHacks/')

    # Make the user sign in and authorize this token

    webbrowser.open_new(url)

    raw_input()

    # This will fail if the user didn't visit the above URL and hit 'Allow'

    access_token = sess.obtain_access_token(request_token)
    
    c_lient = client.DropboxClient(sess)
    metad = c_lient.metadata("/")

    (ld, lf) = dirdirdir(c_lient, metad)
    (jpg_l, txt_l, anon) = extension_parsing(ld, lf)

    z = ', '.join(jpg_l)
    
    a = ', '.join(lf)

    b = ', '.join(txt_l)

    c = ', '.join(ld)

    f = open('data.txt', 'w')
    f.write(c)
    f.close()

#    g = open('files.txt', 'w')
#    g.write(a)
#    g.close()

    h = open('jpg_l.txt', 'w')
    h.write(z)
    h.close()

    k = open('txt_l.txt', 'w')
    k.write(b)
    k.close()

#    l = open('anon.csv', 'w')
#    l.writelines(anon)
#    l.close()
    jpgs, txts = get_args()
    pic = thumbnail(c_lient, jpgs[0])
    print pic

dropboxAuthentication()

def get_info(c_lient, filepath):
    metad = c_lient.metadata(filepath)
    content = metad['contents']
    size = content['size']
    filename = content['path']
    return (filename, size)



#l, k = get_args()

