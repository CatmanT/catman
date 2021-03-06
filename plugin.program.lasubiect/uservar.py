import os, xbmc, xbmcaddon

#########################################################
### User Edit Variables #################################
#########################################################
ADDON_ID       = xbmcaddon.Addon().getAddonInfo('id')
ADDONTITLE     = 'La subiect Wizard'
EXCLUDES       = [ADDON_ID, 'repository.polux', 'plugin.program.lasubiect']
# Text File with build info in it.
BUILDFILE      = 'http://text1.cf/paste.php?raw&id=4'
# How often you would list it to check for build updates in days
# 0 being every startup of kodi
UPDATECHECK    = 0
# Text File with apk info in it.
APKFILE        = 'http://text1.cf/paste.php?raw&id=5'
# Text File with Youtube Videos urls.  Leave as 'http://' to ignore
YOUTUBETITLE   = 'YOUTUBE Videos'
YOUTUBEFILE    = 'http://text1.cf/paste.php?raw&id=6'
# Text File for addon installer.  Leave as 'http://' to ignore
ADDONFILE      = 'http://text1.cf/paste.php?raw&id=7'
# Text File for advanced settings.  Leave as 'http://' to ignore
ADVANCEDFILE   = 'http://'

# Dont need to edit just here for icons stored locally
PATH           = xbmcaddon.Addon().getAddonInfo('path')
ART            = os.path.join(PATH, 'resources', 'art')

#########################################################
### THEMING MENU ITEMS ##################################
#########################################################
# If you want to use locally stored icons the place them in the Resources/Art/
# folder of the wizard then use os.path.join(ART, 'imagename.png')
# do not place quotes around os.path.join
# Example:  ICONMAINT     = os.path.join(ART, 'mainticon.png')
#           ICONSETTINGS  = 'http://aftermathwizard.net/repo/wizard/settings.png'
# Leave as http:// for default icon
ICONBUILDS     = 'https://image.prntscr.com/image/8CjGVO1RQ2qeJxeuJV1Pzg.png'
ICONMAINT      = 'https://image.prntscr.com/image/0A6t-ucbQaSjRccNF3dGIA.png'
ICONAPK        = 'https://image.prntscr.com/image/qIvuMwwDThefiKZ-4H0lSQ.png'
ICONADDONS     = 'https://image.prntscr.com/image/52jnUF3DSauQCxCWzuit-A.png'
ICONYOUTUBE    = 'https://image.prntscr.com/image/v_45F2_HS3mgyWrP94e2-w.png'
ICONSAVE       = 'https://image.prntscr.com/image/JQ-PAEwYRGG_9NgZ2ECnXw.png'
ICONTRAKT      = 'http://'
ICONREAL       = 'http://'
ICONLOGIN      = 'http://'
ICONCONTACT    = 'https://image.prntscr.com/image/1tTGR5ENT8y8V7BdQDj8PQ.png'
ICONSETTINGS   = 'https://image.prntscr.com/image/DVwjIgV2SqueUO4Bc1Fdcw.png'
# Hide the ====== seperators 'Yes' or 'No'
HIDESPACERS    = 'No'
# Character used in seperator
SPACER         = '*'

# You can edit these however you want, just make sure that you have a %s in each of the
# THEME's so it grabs the text from the menu item
COLOR1         = 'white'
COLOR2         = 'white'
# Primary menu items   / %s is the menu item and is required
THEME1         = '[COLOR '+COLOR1+'][B][I]([COLOR '+COLOR2+']La Subiect[/COLOR])[/B][/COLOR] [COLOR '+COLOR2+']%s[/COLOR][/I]'
# Build Names          / %s is the menu item and is required
THEME2         = '[COLOR '+COLOR2+']%s[/COLOR]'
# Alternate items      / %s is the menu item and is required
THEME3         = '[COLOR '+COLOR1+']%s[/COLOR]'
# Current Build Header / %s is the menu item and is required
THEME4         = '[COLOR '+COLOR1+']Current Build:[/COLOR] [COLOR '+COLOR2+']%s[/COLOR]'
# Current Theme Header / %s is the menu item and is required
THEME5         = '[COLOR '+COLOR1+']Current Theme:[/COLOR] [COLOR '+COLOR2+']%s[/COLOR]'

# Message for Contact Page
# Enable 'Contact' menu item 'Yes' hide or 'No' dont hide
HIDECONTACT    = 'Yes'
# You can add \n to do line breaks
CONTACT        = 'Thank you for choosing La Subiect WIZARD\r\n\r\nContact me'
#Images used for the contact window.  http:// for default icon and fanart
CONTACTICON    = 'https://image.prntscr.com/image/1tTGR5ENT8y8V7BdQDj8PQ.png'
CONTACTFANART  = 'http://www.publicdomainpictures.net/pictures/50000/velka/ces-another-heaven.jpg'
#########################################################

#########################################################
### AUTO UPDATE #########################################
########## FOR THOSE WITH NO REPO #######################
# Enable Auto Update 'Yes' or 'No'
AUTOUPDATE     = 'No'
# Url to wizard version
WIZARDFILE     = ''
#########################################################

#########################################################
### AUTO INSTALL ########################################
########## REPO IF NOT INSTALLED ########################
# Enable Auto Install 'Yes' or 'No'
AUTOINSTALL    = 'Yes'
# Addon ID for the repository
REPOID         = 'repository.polux'
# Url to Addons.xml file in your repo folder(this is so we can get the latest version)
REPOADDONXML   = 'https://0ro.000webhostapp.com/polux/_repo/addons.xml'
# Url to folder zip is located in
REPOZIPURL     = 'https://0ro.000webhostapp.com/polux/_repo/repository.polux/'
#########################################################

#########################################################
### NOTIFICATION WINDOW##################################
#########################################################
# Enable Notification screen Yes or No
ENABLE         = 'No'
# Url to notification file
NOTIFICATION   = ''
# Use either 'Text' or 'Image'
HEADERTYPE     = ''
HEADERMESSAGE  = ''
# url to image if using Image 424x180
HEADERIMAGE    = ''
# Background for Notification Window
BACKGROUND     = ''
#########################################################