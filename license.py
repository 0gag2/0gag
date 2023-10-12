import urllib2, urllib, xbmcgui, xbmcplugin, xbmc, re, sys, os, xbmcaddon
import urlresolver
import urllib , urllib2 , datetime, base64 , xbmcplugin , xbmcgui , xbmcaddon , xbmcvfs , traceback , cookielib
import re
import os
from BeautifulSoup import BeautifulStoneSoup, BeautifulSoup, BeautifulSOAP
from addon.common.addon import Addon
from resources.lib import pinoytvlive
import requests

s = requests.session() 
User_Agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.89 Safari/537.36'
addon_id='plugin.video.Still-Kicking'
selfAddon = xbmcaddon.Addon(id=addon_id)
addon = Addon(addon_id, sys.argv)
addon_name = selfAddon.getAddonInfo('name')
ADDON      = xbmcaddon.Addon()
ADDON_PATH = ADDON.getAddonInfo('path')
ICON = ADDON.getAddonInfo('icon')
FANART = ADDON.getAddonInfo('fanart')
PATH = 'Astig Replay'
VERSION = ADDON.getAddonInfo('version')
ART = ADDON_PATH + "/resources/icons/"
dialog = xbmcgui.Dialog()

def MainDir():
    xbmcgui.Dialog().ok("[B][COLOR yellow]Wag mo IBENTA!!![/COLOR][/B]","[B][COLOR yellow]LIBRE ITO![/COLOR][/B]", "[B][COLOR red]by:[/COLOR][/B] [B][COLOR deepskyblue]ASTIG PINOY[/COLOR][/B]")
    addDir('[B][COLOR yellow]PINOY REPLAYS[/COLOR][/B]','url',3,ART + 'ofw pinoy.png',FANART,'')
    addDir('[B][COLOR red]PINOY Movies[/COLOR][/B]','url',103,ART + 'pelikula.png',FANART,'')
    addDir('[B][COLOR pink]PINOY TV[/COLOR][/B]','https://pastebin.com/raw/MCtvzsSt',200,ART + 'pinoy tv.png',FANART,'')
    addDir('[B][COLOR white]PINOY FM Radio[/COLOR][/B]','http://pastebin.com/raw/knX5wLLw',200,ART + 'Pinoy-Music00.jpg',FANART,'')
    addDir('[B][COLOR limegreen]VideOke[/COLOR][/B]','url',104,ART + 'Videoke 12x2 Vip Dual.jpg',FANART,'')
    addDir('[B][COLOR violet]OPM Session[/COLOR][/B]','url',105,ART + 'Tower-of-Doom-300px.png',FANART,'')
#    addDir('[B][COLOR deepskyblue]PBA REPLAYS[/COLOR][/B]','http://pbafullreplay.blogspot.com/',90,ART + 'pba.png',FANART,'')
    setView('addons', 'cat-view')

def OPM():
    itemurl = "plugin://plugin.video.youtube/user/WishFM1075official/"
    listitem = xbmcgui.ListItem( "[B][COLOR yellow]WISH 107.5[/COLOR][/B]", iconImage="DefaultVideo.png", thumbnailImage='http://coolmac.files.wordpress.com/2014/12/wish.png' )
    listitem.setProperty('IsPlayable', 'true')
    xbmcplugin.addDirectoryItem( handle=int(sys.argv[1]), url=itemurl, listitem=listitem, isFolder=True)
    
    itemurl = "plugin://plugin.video.youtube/user/TOWERofDOOM/"
    listitem = xbmcgui.ListItem( "[B][COLOR yellow]TOWER OF DOOM[/COLOR][/B]", iconImage="DefaultVideo.png", thumbnailImage='http://yt3.ggpht.com/a/AGF-l789l-YbAVkqqYOqi61TPDtmcRlA4Vs36N6Vbw=s288-mo-c-c0xffffffff-rj-k-no' )
    listitem.setProperty('IsPlayable', 'true')
    xbmcplugin.addDirectoryItem( handle=int(sys.argv[1]), url=itemurl, listitem=listitem, isFolder=True)
    
    itemurl = "plugin://plugin.video.youtube/user/RadioRepublicPH/"
    listitem = xbmcgui.ListItem( "[B][COLOR yellow]RadioRepulicPH[/COLOR][/B]", iconImage="DefaultVideo.png", thumbnailImage='http://yt3.ggpht.com/a/AGF-l7-eNm2hiYiDOAktIFuU-VsuS9bWhRWa0tiJ9w=s288-mo-c-c0xffffffff-rj-k-no' )
    listitem.setProperty('IsPlayable', 'true')
    xbmcplugin.addDirectoryItem( handle=int(sys.argv[1]), url=itemurl, listitem=listitem, isFolder=True)
    
    itemurl = "plugin://plugin.video.youtube/playlist/PLxIGRNqt1BBj5GmwMFoLBg4CzrDpQxglw/"
    listitem = xbmcgui.ListItem( "[B][COLOR yellow]Rappler Live Jam[/COLOR][/B]", iconImage="DefaultVideo.png", thumbnailImage='http://yt3.ggpht.com/a/AGF-l7_Pkhmcs8fUpKGGiuA8HvbOtJNVrsCBeKJk7g=s900-mo-c-c0xffffffff-rj-k-no' )
    listitem.setProperty('IsPlayable', 'true')
    xbmcplugin.addDirectoryItem( handle=int(sys.argv[1]), url=itemurl, listitem=listitem, isFolder=True)
	
def Teleserye_Cat():
    addDir('[B][COLOR white]SEARCH TITLE[/COLOR][/B]','url',1,ART + 'search.jpg',FANART,'')
    addDir('[B][COLOR yellow]PINOY FLIX[/COLOR][/B]','https://pinoysflix.su/',111,ART + 'icon3.png',FANART,'')
    addDir('[B][COLOR yellow]PiNOY HD FLIX[/COLOR][/B]','https://pinoyhdflix.su/',111,ART + 'icon9.png',FANART,'')
    addDir('[B][COLOR yellow]PINOYs TV CHANNEL[/COLOR][/B]','https://pinoyhqteleserye.su/',111,ART + 'icon4.png',FANART,'')
    addDir('[B][COLOR yellow]PINOY TAMBAYAN HD[/COLOR][/B]','https://pinoytambayans.su/',110,ART + 'icon2.png',FANART,'')
    addDir('[B][COLOR yellow]FANTASERYE[/COLOR][/B]','https://fantaserye.su/',60,ART + 'icon5.png',FANART,'')
    addDir('[B][COLOR yellow]PiNOY FLIX TV[/COLOR][/B]','https://pinoysflixtv.su/',111,ART + 'icon7.png',FANART,'')
    setView('addons', 'cat-view')
	
def Search():
    keyb = xbmc.Keyboard('','[B][COLOR yellow]Search[/COLOR][/B]')
    keyb.doModal()
    if (keyb.isConfirmed()):
            search = keyb.getText().replace(' ','+')
            url = 'https://pinoytambayans.su/?s=' + search
            pinoysflix_content(url)
		
###############  TELESERYE  ###############

###### https://pinoytambayans.su ######

def test_content(url):
    OPEN = Open_Url(url)
    Regex = re.compile('<div class="featured-thumbnail">.+?img width="203" height="150" src="(.+?)".+?<header>.+?href="(.+?)" title="(.+?)"',re.DOTALL).findall(OPEN)
    for icon,url,name in Regex:
        name = name.replace('&#8217;','\'').replace('&#8211;','-').replace('&#39;','\'').replace('&#038;','&').replace('Full Episode in HD','').replace('Full Episode In HD','').replace('Full Episode HD','').replace('&nbsp;',' ')
        addDir('[B][COLOR yellow]%s[/COLOR][/B]' %name,url,113,icon,icon,'')
    np = re.compile('rel="next" href="(.+?)"',re.DOTALL).findall(OPEN)
    for url in np:
        addDir('[B][COLOR lime]Next Page >>>[/COLOR][/B]',url,110,ART + 'page.jpg',FANART,'')
    setView('episodes', 'epi-view')

def test_links(name,url):
    OPEN = Open_Url(url)
    if 'Part' in OPEN:
		Regex = re.compile("file: '(.+?)'.+?image:",re.DOTALL).findall(OPEN)
		for url in Regex:
			addDir(name + ' - Full Video',url,77,iconimage,iconimage,name)
    else:
		Regex = re.compile("file: '(.+?)'.+?image:",re.DOTALL).findall(OPEN)
		for url in Regex:
			addDir(name + ' - Full Video',url,77,iconimage,iconimage,name)
    Regex2 = re.compile('IFRAME SRC="(.+?)"',re.DOTALL).findall(OPEN)
    i=1
    for url in Regex2:
		if len(Regex2)>1:
			name2= name + ' -  '+ str(i)
			i=i+1
			addDir('%s' %name2,url,77,iconimage,iconimage,name)
		else:
			addDir(name,url,77,iconimage,iconimage,name)
		# name2= name + ' - Part '+ str(i)
		# i=i+1
		# addDir('%s' %name2,url,77,iconimage,iconimage,name)
    altlinks = re.compile('iframe width="100%" height="400" src="(.+?)"',re.DOTALL).findall(OPEN)
    i=1
    for url in altlinks:
		if len(altlinks)>1:
			name2 = 'SERVER '+ str(i)
			i=i+1
			addDir('[COLOR deepskyblue][B]%s[/B][/COLOR]' %name2,url,77,iconimage,iconimage,name)
		else:
			addDir(name,url,77,iconimage,iconimage,name)
    altlinks2 = re.compile('iframe src="(.+?)"',re.DOTALL).findall(OPEN)
    i=1
    for url in altlinks2:
		if len(altlinks2)>1:
			name2 = 'SERVER ' + str(i) + ' - ' + name
			i=i+1
			addDir('[B][COLOR deepskyblue]%s[/COLOR]' %name2,url,77,iconimage,iconimage,name)
		else:
			addDir(name,url,77,iconimage,iconimage,name)
    altlinks3 = re.compile('<iframe loading="lazy" src="(.+?)"',re.DOTALL).findall(OPEN)
    i=1
    for url in altlinks3:
		if len(altlinks3)>1:
			name2 = 'Video Link '+ str(i)
			i=i+1
			addDir('[COLOR deepskyblue][B]%s[/B][/COLOR]' %name2,url,77,iconimage,iconimage,name)
		else:
			addDir(name,url,77,iconimage,iconimage,name)
    linkView()
    
#### https://fantaserye.su/ ####

def absgma_content(url):
    OPEN = Open_Url(url)
    Regex = re.compile('div class="recent-item tie_video".+?img width="310" height="165" src="(.+?)".+?h3 class="post-box-title".+?href="(.+?)" rel="bookmark".+?(.+?)</a></h3>',re.DOTALL).findall(OPEN)
    for icon,url,name in Regex:
#    for url,icon,name in Regex:
        name = name.replace('&#8217;','\'').replace('&#8211;','-').replace('&#39;','\'').replace('&#038;','&').replace('Full Episode in HD','').replace('Full Episode In HD','').replace('Full Episode HD','').replace('&nbsp;',' ')
        addDir('[B][COLOR yellow]%s[/COLOR][/B]' %name,url,61,icon,icon,'')
 #   np = re.compile('link rel="next" href="(.+?)"',re.DOTALL).findall(OPEN)
    np = re.compile('<div class="pagination">.+?href="(.+?)"',re.DOTALL).findall(OPEN)
    for url in np:
        addDir('[B][COLOR lime]Next Page >>>[/COLOR][/B]',url,60,ART + 'page.jpg',FANART,'')
    setView('episodes', 'epi-view')

def absgma_links(name,url):
    OPEN = Open_Url(url)
    if 'Part' in OPEN:
		Regex = re.compile("file: '(.+?)'.+?Part 1</",re.DOTALL).findall(OPEN)
		for url in Regex:
			addDir(name + ' - Full Video',url,77,iconimage,iconimage,name)
    else:
		Regex = re.compile("file: '(.+?)'.+?image:",re.DOTALL).findall(OPEN)
		for url in Regex:
			addDir(name + ' - Full Video',url,77,iconimage,iconimage,name)
    Regex2 = re.compile('iframe src"(.+?)"',re.DOTALL).findall(OPEN)
    i=1
    for url in Regex2:
		if len(Regex2)>1:
			name2= name + ' - Part '+ str(i)
			i=i+1
			addDir('[COLOR deepskyblue][B]%s[/B][/COLOR]' %name2,url,77,iconimage,iconimage,name)
		else:
		#	addDir(name + ' - Full Video',url,77,iconimage,iconimage,name)
		 name2= 'Video Link '+ str(i)
		 i=i+1
		 addDir('%s' %name2,url,77,iconimage,iconimage,name)
    altlinks = re.compile('iframe src="(.+?)"',re.DOTALL).findall(OPEN)
    i=1
    for url in altlinks:
		if len(altlinks)>1:
			name2 = 'Video Link '+ str(i)
			i=i+1
			addDir('[COLOR deepskyblue][B]%s[/B][/COLOR]' %name2,url,77,iconimage,iconimage,name)
		else:
			addDir(name,url,77,iconimage,iconimage,name)
    linkView()

def OFWpinoy_content(url):
    OPEN = Open_Url(url)
    Regex = re.compile('img data-original="(.+?)".+?div data-movie-id="(.+?)" class="ml-item".+?href="(.+?)" old title="(.+?)" title=""',re.DOTALL).findall(OPEN)
    for icon,url,name in Regex:
        name = name.replace('&#8217;','\'').replace('&#8211;','-').replace('&#39;','\'').replace('&#038;','&').replace('Full Episode in HD','').replace('Full Episode In HD','').replace('Full Episode HD','').replace('&nbsp;',' ')
        addDir('[B][COLOR yellow]%s[/COLOR][/B]' %name,url,112,icon,icon,'')
    np = re.compile('rel="next" href="(.+?)"',re.DOTALL).findall(OPEN)
    for url in np:
        addDir('[B][COLOR lime]Next Page >>>[/COLOR][/B]',url,111,ART + 'page.jpg',FANART,'')
    setView('episodes', 'epi-view')

def OFWpinoy_links(name,url):
    OPEN = Open_Url(url)
    if 'Part' in OPEN:
		Regex = re.compile("file: '(.+?)'.+?Part 1</",re.DOTALL).findall(OPEN)
		for url in Regex:
			addDir(name + ' - Full Video',url,77,iconimage,iconimage,name)
    else:
		Regex = re.compile("file: '(.+?)'.+?image:",re.DOTALL).findall(OPEN)
		for url in Regex:
			addDir(name + ' - Full Video',url,77,iconimage,iconimage,name)
    Regex2 = re.compile('iframe src="(.+?)"',re.DOTALL).findall(OPEN)
    i=1
    for url in Regex2:
		if len(Regex2)>1:
			name2= name + ' - Part '+ str(i)
			i=i+1
			addDir('%s' %name2,url,77,iconimage,iconimage,name)
		else:
			addDir(name + ' - Full Video',url,77,iconimage,iconimage,name)
		# name2= name + ' - Part '+ str(i)
		# i=i+1
		# addDir('%s' %name2,url,77,iconimage,iconimage,name)
    altlinks = re.compile('iframe width="100%" height="400" src="(.+?)"',re.DOTALL).findall(OPEN)
    i=1
    for url in altlinks:
		if len(altlinks)>1:
			name2 = 'Video Link '+ str(i)
			i=i+1
			addDir('[COLOR deepskyblue][B]%s[/B][/COLOR]' %name2,url,77,iconimage,iconimage,name)
		else:
			addDir(name,url,77,iconimage,iconimage,name)
    altlinks2 = re.compile('<IFRAME SRC="(.+?)"',re.DOTALL).findall(OPEN)
    i=1
    for url in altlinks2:
		if len(altlinks2)>1:
			name2 = 'Video Link '+ str(i)
			i=i+1
			addDir('[COLOR deepskyblue][B]%s[/B][/COLOR]' %name2,url,77,iconimage,iconimage,name)
		else:
			addDir(name,url,77,iconimage,iconimage,name)
    altlinks3 = re.compile('<iframe loading="lazy" src="(.+?)"',re.DOTALL).findall(OPEN)
    i=1
    for url in altlinks3:
		if len(altlinks3)>1:
			name2 = 'Video Link '+ str(i)
			i=i+1
			addDir('[COLOR deepskyblue][B]%s[/B][/COLOR]' %name2,url,77,iconimage,iconimage,name)
		else:
			addDir(name,url,77,iconimage,iconimage,name)
    linkView()

#### http://ofwpinoyteleserye.su/ ####

def ofwpinoyteleserye_content(url):
    OPEN = Open_Url(url)
    Regex = re.compile('div class="featured-thumbnail".+?img width="203" height="150" src="(.+?)".+?h2 class="title front-view-title".+?a href="(.+?)" title="(.+?)"',re.DOTALL).findall(OPEN)
    for icon,url,name in Regex:
        name = name.replace('&#8217;','\'').replace('&#8211;','-').replace('&#39;','\'').replace('&#038;','&').replace('Full Episode in HD','').replace('Full Episode In HD','').replace('Full Episode HD','').replace('&nbsp;',' ')
        addDir('[B][COLOR yellow]%s[/COLOR][/B]' %name,url,107,icon,icon,'')
    np = re.compile('rel="next" href="(.+?)"',re.DOTALL).findall(OPEN)
    for url in np:
        addDir('[B][COLOR lime]Next Page >>>[/COLOR][/B]',url,106,ART + 'page.jpg',FANART,'')
    setView('episodes', 'epi-view')

def ofwpinoyteleserye_links(name,url):
    OPEN = Open_Url(url)
    if 'Part' in OPEN:
		Regex = re.compile("file: '(.+?)'.+?Part 1</",re.DOTALL).findall(OPEN)
		for url in Regex:
			addDir(name + ' - Full Video',url,77,iconimage,iconimage,name)
    else:
		Regex = re.compile("file: '(.+?)'.+?image:",re.DOTALL).findall(OPEN)
		for url in Regex:
			addDir(name + ' - Full Video',url,77,iconimage,iconimage,name)
    Regex2 = re.compile('iframe loading="lazy" src="(.+?)"',re.DOTALL).findall(OPEN)
    i=1
    for url in Regex2:
		if len(Regex2)>1:
			name2= name + ' - Part '+ str(i)
			i=i+1
			addDir('%s' %name2,url,77,iconimage,iconimage,name)
		else:
			addDir(name + ' - Full Video',url,77,iconimage,iconimage,name)
		# name2= name + ' - Part '+ str(i)
		# i=i+1
		# addDir('%s' %name2,url,77,iconimage,iconimage,name)
    altlinks = re.compile('iframe src="(.+?)"',re.DOTALL).findall(OPEN)
    i=1
    for url in altlinks:
		if len(altlinks)>1:
			name2 = 'Video Link '+ str(i)
			i=i+1
			addDir('[COLOR deepskyblue][B]%s[/B][/COLOR]' %name2,url,77,iconimage,iconimage,name)
		else:
			addDir(name,url,77,iconimage,iconimage,name)
    linkView()

#### http://pinoytambayan.su/ ####

def pinoytambayan_content(url):
    OPEN = Open_Url(url)
    Regex = re.compile('div class="featured-thumbnail".+?img width="203" height="150" src="(.+?)".+?<header>.+?href="(.+?)" title="(.+?)"',re.DOTALL).findall(OPEN)
    for icon,url,name in Regex:
        name = name.replace('&#8217;','\'').replace('&#8211;','-').replace('&#39;','\'').replace('&#038;','&').replace('Full Episode in HD','').replace('Full Episode In HD','').replace('Full Episode HD','').replace('&nbsp;',' ')
        addDir('[B][COLOR yellow]%s[/COLOR][/B]' %name,url,76,icon,icon,'')
    np = re.compile('rel="next" href="(.+?)"',re.DOTALL).findall(OPEN)
    for url in np:
        addDir('[B][COLOR lime]Next Page >>>[/COLOR][/B]',url,75,ART + 'page.jpg',FANART,'')
    setView('episodes', 'epi-view')

def pinoytambayan_links(name,url):
    OPEN = Open_Url(url)
    if 'Part' in OPEN:
		Regex = re.compile("file: '(.+?)'.+?Part 1</",re.DOTALL).findall(OPEN)
		for url in Regex:
			addDir(name + ' - Full Video',url,77,iconimage,iconimage,name)
    else:
		Regex = re.compile("file: '(.+?)'.+?image:",re.DOTALL).findall(OPEN)
		for url in Regex:
			addDir(name + ' - Full Video',url,77,iconimage,iconimage,name)
    Regex2 = re.compile('<iframe src="(.+?)"',re.DOTALL).findall(OPEN)
    i=1
    for url in Regex2:
		if len(Regex2)>1:
			name2= name + ' - Part '+ str(i)
			i=i+1
			addDir('%s' %name2,url,77,iconimage,iconimage,name)
		else:
			addDir(name + ' - Full Video',url,77,iconimage,iconimage,name)
		# name2= name + ' - Part '+ str(i)
		# i=i+1
		# addDir('%s' %name2,url,77,iconimage,iconimage,name)
    altlinks = re.compile('<iframe loading="lazy" src="(.+?)"',re.DOTALL).findall(OPEN)
    i=1
    for url in altlinks:
		if len(altlinks)>1:
			name2 = 'Video Link '+ str(i)
			i=i+1
			addDir('[COLOR deepskyblue][B]%s[/B][/COLOR]' %name2,url,77,iconimage,iconimage,name)
		else:
			addDir(name,url,77,iconimage,iconimage,name)
    linkView()
	
def pinoystambayan_resolve(url):
	if 'vkspeed.com' in url:
		stream_url = urlresolver.resolve(url)
	elif urlresolver.HostedMediaFile(url).valid_url():
		stream_url = urlresolver.resolve(url)
	else:
		stream_url = url
	liz = xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=iconimage)
	liz.setInfo(type="Video", infoLabels={"Title": description})
	liz.setProperty("IsPlayable","true")
	liz.setPath(stream_url)
	xbmcplugin.setResolvedUrl(int(sys.argv[1]), True, liz)

#### http://pinoyhdflix.su/ ####

def pinoyhdflix_content(url):
    OPEN = Open_Url(url)
    Regex = re.compile('div class="featured-thumbnail".+?<noscript>.+?img width="203" height="150" src="(.+?)".+?href="(.+?)" title="(.+?)"</noscript></div></a>',re.DOTALL).findall(OPEN)
    for icon,url,name in Regex:
        name = name.replace('&#8217;','\'').replace('&#8211;','-').replace('&#39;','\'').replace('&#038;','&').replace('Full Episode in HD','').replace('Full Episode In HD','').replace('Full Episode HD','').replace('&nbsp;',' ')
        addDir('[B][COLOR yellow]%s[/COLOR][/B]' %name,url,79,icon,icon,'')
    np = re.compile('link rel="next" href="(.+?)"',re.DOTALL).findall(OPEN)
    for url in np:
        addDir('[B][COLOR lime]Next Page >>>[/COLOR][/B]',url,82,ART + 'page.jpg',FANART,'')
    setView('episodes', 'epi-view')
    
def pinoyhdflix_links(name,url):
    OPEN = Open_Url(url)
    if 'Part' in OPEN:
		Regex = re.compile("file: '(.+?)'.+?Part 1</",re.DOTALL).findall(OPEN)
		for url in Regex:
			addDir(name + ' - Full Video',url,77,iconimage,iconimage,name)
    else:
		Regex = re.compile("file: '(.+?)'.+?image:",re.DOTALL).findall(OPEN)
		for url in Regex:
			addDir(name + ' - Full Video',url,77,iconimage,iconimage,name)
    Regex2 = re.compile('iframe loading="lazy" src="(.+?)"',re.DOTALL).findall(OPEN)
    i=1
    for url in Regex2:
		if len(Regex2)>1:
			name2= name + ' - Part '+ str(i)
			i=i+1
			addDir('%s' %name2,url,77,iconimage,iconimage,name)
		else:
		#	addDir(name + ' - Full Video',url,77,iconimage,iconimage,name)
		 name2= 'Video Link '+ str(i)
		 i=i+1
		 addDir('%s' %name2,url,77,iconimage,iconimage,name)
    altlinks = re.compile('<iframe src="(.+?)">',re.DOTALL).findall(OPEN)
    i=1
    for url in altlinks:
		if len(altlinks)>1:
			name2 = 'Video Link '+ str(i)
			i=i+1
			addDir('[COLOR deepskyblue][B]%s[/B][/COLOR]' %name2,url,77,iconimage,iconimage,name)
		else:
			addDir(name,url,77,iconimage,iconimage,name)
    altlinks2 = re.compile('<IFRAME SRC="(.+?)">',re.DOTALL).findall(OPEN)
    i=1
    for url in altlinks2:
		if len(altlinks2)>1:
			name2 = 'Video Link '+ str(i)
			i=i+1
			addDir('[COLOR deepskyblue][B]%s[/B][/COLOR]' %name2,url,77,iconimage,iconimage,name)
		else:
			addDir(name,url,77,iconimage,iconimage,name)
    altlinks3 = re.compile('<iframe width="100%" height="400" src="(.+?)">',re.DOTALL).findall(OPEN)
    i=1
    for url in altlinks3:
		if len(altlinks3)>1:
			name2 = 'Video Link '+ str(i)
			i=i+1
			addDir('[COLOR deepskyblue][B]%s[/B][/COLOR]' %name2,url,77,iconimage,iconimage,name)
		else:
			addDir(name,url,77,iconimage,iconimage,name)
    linkView()
    
#### https://pinoysflix.su/ ####

def pinoysflix_content(url):
    OPEN = Open_Url(url)
    Regex = re.compile('div class="featured-thumbnail".+?img width="203" height="150" src="(.+?)".+?<header>.+?href="(.+?)" title="(.+?)"',re.DOTALL).findall(OPEN)
    for icon,url,name in Regex:
        name = name.replace('&#8217;','\'').replace('&#8211;','-').replace('&#39;','\'').replace('&#038;','&').replace('Full Episode in HD','').replace('Full Episode In HD','').replace('Full Episode HD','').replace('&nbsp;',' ')
        addDir('[B][COLOR yellow]%s[/COLOR][/B]' %name,url,112,icon,icon,'')
    np = re.compile('rel="next" href="(.+?)"',re.DOTALL).findall(OPEN)
    for url in np:
        addDir('[B][COLOR lime]Next Page >>>[/COLOR][/B]',url,111,ART + 'page.jpg',FANART,'')
    setView('episodes', 'epi-view')

def pinoysflix_links(name,url):
    OPEN = Open_Url(url)
    if 'Part' in OPEN:
		Regex = re.compile("file: '(.+?)'.+?Part 1</",re.DOTALL).findall(OPEN)
		for url in Regex:
			addDir(name + ' - Full Video',url,77,iconimage,iconimage,name)
    else:
		Regex = re.compile("file: '(.+?)'.+?image:",re.DOTALL).findall(OPEN)
		for url in Regex:
			addDir(name + ' - Full Video',url,77,iconimage,iconimage,name)
    Regex2 = re.compile('IFRAME SRC="(.+?)"',re.DOTALL).findall(OPEN)
    i=1
    for url in Regex2:
		if len(Regex2)>1:
			name2= name + ' - Part '+ str(i)
			i=i+1
			addDir('%s' %name2,url,77,iconimage,iconimage,name)
		else:
			addDir(name + ' - Full Video',url,77,iconimage,iconimage,name)
		# name2= name + ' - Part '+ str(i)
		# i=i+1
		# addDir('%s' %name2,url,77,iconimage,iconimage,name)
    altlinks = re.compile('iframe width="100%" height="400" src="(.+?)"',re.DOTALL).findall(OPEN)
    i=1
    for url in altlinks:
		if len(altlinks)>1:
			name2 = 'Video Link '+ str(i)
			i=i+1
			addDir('[COLOR deepskyblue][B]%s[/B][/COLOR]' %name2,url,77,iconimage,iconimage,name)
		else:
			addDir(name,url,77,iconimage,iconimage,name)
    altlinks2 = re.compile('<iframe src="(.+?)"',re.DOTALL).findall(OPEN)
    i=1
    for url in altlinks2:
		if len(altlinks2)>1:
			name2 = 'Video Link '+ str(i)
			i=i+1
			addDir('[COLOR deepskyblue][B]%s[/B][/COLOR]' %name2,url,77,iconimage,iconimage,name)
		else:
			addDir(name,url,77,iconimage,iconimage,name)
    altlinks3 = re.compile('<iframe loading="lazy" src="(.+?)"',re.DOTALL).findall(OPEN)
    i=1
    for url in altlinks3:
		if len(altlinks3)>1:
			name2 = 'Video Link '+ str(i)
			i=i+1
			addDir('[COLOR deepskyblue][B]%s[/B][/COLOR]' %name2,url,77,iconimage,iconimage,name)
		else:
			addDir(name,url,77,iconimage,iconimage,name)
    linkView()

#### https://hdpinoyteleserye.su/ ####

def pinoyhdflix_content(url):
    OPEN = Open_Url(url)
    Regex = re.compile('div class="featured-thumbnail".+?img width="203" height="150" src="(.+?)".+?<header>.+?href="(.+?)" title="(.+?)"',re.DOTALL).findall(OPEN)
    for icon,url,name in Regex:
        name = name.replace('&#8217;','\'').replace('&#8211;','-').replace('&#39;','\'').replace('&#038;','&').replace('Full Episode in HD','').replace('Full Episode In HD','').replace('Full Episode HD','').replace('&nbsp;',' ')
        addDir('[B][COLOR yellow]%s[/COLOR][/B]' %name,url,79,icon,icon,'')
    np = re.compile('rel="next" href="(.+?)"',re.DOTALL).findall(OPEN)
    for url in np:
        addDir('[B][COLOR lime]Next Page >>>[/COLOR][/B]',url,82,ART + 'page.jpg',FANART,'')
    setView('episodes', 'epi-view')

def pinoyhdflix_links(name,url):
    OPEN = Open_Url(url)
    if 'Part' in OPEN:
		Regex = re.compile("file: '(.+?)'.+?Part 1</",re.DOTALL).findall(OPEN)
		for url in Regex:
			addDir(name + ' - Full Video',url,77,iconimage,iconimage,name)
    else:
		Regex = re.compile("file: '(.+?)'.+?image:",re.DOTALL).findall(OPEN)
		for url in Regex:
			addDir(name + ' - Full Video',url,77,iconimage,iconimage,name)
    Regex2 = re.compile('<iframe loading="lazy" src="(.+?)"',re.DOTALL).findall(OPEN)
    i=1
    for url in Regex2:
		if len(Regex2)>1:
			name2= name + ' - Part '+ str(i)
			i=i+1
			addDir('%s' %name2,url,77,iconimage,iconimage,name)
		else:
			addDir(name + ' - Full Video',url,77,iconimage,iconimage,name)
		# name2= name + ' - Part '+ str(i)
		# i=i+1
		# addDir('%s' %name2,url,77,iconimage,iconimage,name)
    altlinks = re.compile('<IFRAME SRC="(.+?)"',re.DOTALL).findall(OPEN)
    i=1
    for url in altlinks:
		if len(altlinks)>1:
			name2 = 'Video Link '+ str(i)
			i=i+1
			addDir('[COLOR deepskyblue][B]%s[/B][/COLOR]' %name2,url,77,iconimage,iconimage,name)
		else:
			addDir(name,url,77,iconimage,iconimage,name)
    linkView()

###############  PINOY MOVIES  ###############

def Pelikula_Cat():

    addDir('[COLOR yellow][B]Pinoy Movies[/B][/COLOR]','url',10,ART + 'PBO.png',FANART,'')
    
    itemurl = "plugin://plugin.video.youtube/channel/UC69I8egELqWywoX5wrh2KxQ/playlists/"
    listitem = xbmcgui.ListItem( "[B][COLOR yellow]Regal Movies[/COLOR][/B]", iconImage="DefaultVideo.png", thumbnailImage='http://upload.wikimedia.org/wikipedia/en/1/15/Regal_Films2018.png' )
    listitem.setProperty('IsPlayable', 'true')
    xbmcplugin.addDirectoryItem( handle=int(sys.argv[1]), url=itemurl, listitem=listitem, isFolder=True)

    itemurl = "plugin://plugin.video.youtube/playlist/PLalQNACgOUSexat_rVzqFdZkshVxbL4WO/"
    listitem = xbmcgui.ListItem( "[B][COLOR yellow]Star Cinema[/COLOR][/B]", iconImage="DefaultVideo.png", thumbnailImage='http://pbs.twimg.com/media/EBKhO_PXsAA5AEY.jpg' )
    listitem.setProperty('IsPlayable', 'true')
    xbmcplugin.addDirectoryItem( handle=int(sys.argv[1]), url=itemurl, listitem=listitem, isFolder=True)
    
    itemurl = "plugin://plugin.video.youtube/playlist/PL909iyocC7rTUR3wjyYqJVzyENv06n0wD/"
    listitem = xbmcgui.ListItem( "[B][COLOR yellow]Viva Films[/COLOR][/B]", iconImage="DefaultVideo.png", thumbnailImage='http://upload.wikimedia.org/wikipedia/en/7/75/Viva_Films.jpg' )
    listitem.setProperty('IsPlayable', 'true')
    xbmcplugin.addDirectoryItem( handle=int(sys.argv[1]), url=itemurl, listitem=listitem, isFolder=True)
    
    itemurl = "plugin://plugin.video.youtube/channel/UCfrVJqr001Y6cd8Drx_mmQg/playlists/"
    listitem = xbmcgui.ListItem( "[B][COLOR yellow]Taga Love[/COLOR][/B]", iconImage="DefaultVideo.png", thumbnailImage='https://yt3.ggpht.com/WNI77Rd6kqmY8jPdVwHRyp3Qv_vToZOcafiUVxge0OVCSjK0JSIVTvljODgLH0bddiJ812M8adY=s900-c-k-c0x00ffffff-no-rj' )
    listitem.setProperty('IsPlayable', 'true')
    xbmcplugin.addDirectoryItem( handle=int(sys.argv[1]), url=itemurl, listitem=listitem, isFolder=True)
    setView('episodes', 'epi-view')
	
#### pinoymoviepedia.org ####

def moviepedia_cat():
    addDir('Search','url',6,ART + 'search.jpg',FANART,'')
    addDir('Pinoy Movies','https://pinoymoviepedia.ru/',11,ART + 'PBO.png',FANART,'')
    addDir('Digitally Restored','https://pinoymoviepedia.ru/genre/digitally-restored/',11,ART + 'Restore-Logo-7.png',FANART,'')
    addDir('Genre','url',13,ART + 'genre.jpg',FANART,'')
    addDir('Year','url',14,ART + 'Year.png',FANART,'')
    setView('episodes', 'epi-view')
    
def moviepedia_genre():
    addDir('Action','https://pinoymoviepedia.ru/genre/action/',11,ART + '',FANART,'')
    addDir('Romance','https://pinoymoviepedia.ru/genre/romance/',11,ART + '',FANART,'')
    addDir('Comedy','https://pinoymoviepedia.ru/genre/comedy/',11,ART + '',FANART,'')
    addDir('Drama','https://pinoymoviepedia.ru/genre/drama/',11,ART + '',FANART,'')
    addDir('Horror','https://pinoymoviepedia.ru/genre/horror/',11,ART + '',FANART,'')
    addDir('Rated-R','https://pinoymoviepedia.ru/genre/pinay-sexy-movies/',11,ART + '',FANART,'')

def moviepedia_year():
    addDir('2023','https://pinoymoviepedia.ru/release/2023/',11,ART + '',FANART,'')
    addDir('2022','https://pinoymoviepedia.ru/release/2022/',11,ART + '',FANART,'')
    addDir('2021','https://pinoymoviepedia.ru/release/2020/',11,ART + '',FANART,'')
    addDir('2020','https://pinoymoviepedia.ru/release/2020/',11,ART + '',FANART,'')
    addDir('2019','https://pinoymoviepedia.ru/release/2019/',11,ART + '',FANART,'')
    addDir('2018','https://pinoymoviepedia.ru/release/2018/',11,ART + '',FANART,'')
    addDir('2017','https://pinoymoviepedia.ru/release/2017/',11,ART + '',FANART,'')
    addDir('2016','https://pinoymoviepedia.ru/release/2016/',11,ART + '',FANART,'')
    addDir('2015','https://pinoymoviepedia.ru/release/2015/',11,ART + '',FANART,'')
    addDir('2014','https://pinoymoviepedia.ru/release/2014/',11,ART + '',FANART,'')
    addDir('2013','https://pinoymoviepedia.ru/release/2013/',11,ART + '',FANART,'')
    addDir('2012','https://pinoymoviepedia.ru/release/2012/',11,ART + '',FANART,'')
    addDir('2011','https://pinoymoviepedia.ru/release/2011/',11,ART + '',FANART,'')
    addDir('2010','https://pinoymoviepedia.ru/release/2010/',11,ART + '',FANART,'')
    addDir('2009','https://pinoymoviepedia.ru/release/2009/',11,ART + '',FANART,'')
    addDir('2008','https://pinoymoviepedia.ru/release/2008/',11,ART + '',FANART,'')
    addDir('2007','https://pinoymoviepedia.ru/release/2007/',11,ART + '',FANART,'')
    addDir('2006','https://pinoymoviepedia.ru/release/2006/',11,ART + '',FANART,'')
    addDir('2005','https://pinoymoviepedia.ru/release/2005/',11,ART + '',FANART,'')
    addDir('2004','https://pinoymoviepedia.ru/release/2004/',11,ART + '',FANART,'')
    addDir('2003','https://pinoymoviepedia.ru/release/2003/',11,ART + '',FANART,'')
    addDir('2002','https://pinoymoviepedia.ru/release/2002/',11,ART + '',FANART,'')
    addDir('2001','https://pinoymoviepedia.ru/release/2001/',11,ART + '',FANART,'')
    addDir('2000','https://pinoymoviepedia.ru/release/2000/',11,ART + '',FANART,'')
    addDir('1999','https://pinoymoviepedia.ru/release/1999/',11,ART + '',FANART,'')
    addDir('1998','https://pinoymoviepedia.ru/release/1998/',11,ART + '',FANART,'')
    addDir('1997','https://pinoymoviepedia.ru/release/1997/',11,ART + '',FANART,'')
    addDir('1996','https://pinoymoviepedia.ru/release/1996/',11,ART + '',FANART,'')
    addDir('1995','https://pinoymoviepedia.ru/release/1995/',11,ART + '',FANART,'')
    addDir('1994','https://pinoymoviepedia.ru/release/1994/',11,ART + '',FANART,'')
    addDir('1993','https://pinoymoviepedia.ru/release/1993/',11,ART + '',FANART,'')
    addDir('1992','https://pinoymoviepedia.ru/release/1992/',11,ART + '',FANART,'')
    addDir('1991','https://pinoymoviepedia.ru/release/1991/',11,ART + '',FANART,'')
    addDir('1990','https://pinoymoviepedia.ru/release/1990/',11,ART + '',FANART,'')
    
def moviepedia_content(url):
    OPEN = Open_Url(url)
    Regex = re.compile('div class="poster.+?img src="(.+?)" alt="(.+?)".+?href="(.+?)"',re.DOTALL).findall(OPEN)
    for icon,name,url in Regex:
        name = name.replace('&#8217;','\'').replace('&#8211;','-').replace('&#39;','\'').replace('&#038;','&')
        icon = icon.replace('-210x142','').replace('-199x142','')
        addDir('%s' %name,url,12,icon,FANART,'')
    np = re.compile('div class="pagination".+?href="(.+?)"',re.DOTALL).findall(OPEN)
    for url in np:
        addDir('[B][COLOR lime]Next Page >>>[/COLOR][/B]',url,11,ART + 'pagemov.jpg',FANART,'')
    setView('movies', 'mov-view')
    
def moviepedia_links(name,url):
    OPEN = Open_Url(url)
    Links = re.compile('iframe class="metaframe rptss" src="(.+?)"',re.DOTALL).findall(OPEN)
    i=1
    for url in Links:
        url = url.replace('https://bluray7.com/links/?','')
        if urlresolver.HostedMediaFile(url).valid_url():
			try:
				name2 = url.split('//')[1].replace('www.','')
				name2 = name2.split('/')[0].split('.')[0].title()
			except:pass
			addDir(name2,url,100,iconimage,iconimage,name)
        elif len(Links)>1:		
			name1= 'Movie Link '+ str(i)
			i=i+1
			addDir('%s' %name1,url,100,iconimage,iconimage,name)
    linkView()
    
########VIDEOKE########
def VideOke_Cat():
    itemurl = "plugin://plugin.video.youtube/channel/UCj8MrQPTFj08bCg_G0WLFVg/playlists/"
    listitem = xbmcgui.ListItem( "[B][COLOR yellow]SARI-SARI[/COLOR][/B]", iconImage="DefaultVideo.png", thumbnailImage='http://sites.google.com/site/berklynelectronic/_/rsrc/1443968756855/videoke-machine/cabinet-dual-keypad-button/Videoke%2012x2%20Vip%20Dual.jpg' )
    listitem.setProperty('IsPlayable', 'true')
    xbmcplugin.addDirectoryItem( handle=int(sys.argv[1]), url=itemurl, listitem=listitem, isFolder=True)

    itemurl = "plugin://plugin.video.youtube/playlist/PLyMJQPx95_IBLDQfJbVOD56S5KFcTh-HW/"
    listitem = xbmcgui.ListItem( "[B][COLOR yellow]LATEST OPM SONGS[/COLOR][/B]", iconImage="DefaultVideo.png", thumbnailImage='http://sites.google.com/site/berklynelectronic/_/rsrc/1443968756855/videoke-machine/cabinet-dual-keypad-button/Videoke%2012x2%20Vip%20Dual.jpg' )
    listitem.setProperty('IsPlayable', 'true')
    xbmcplugin.addDirectoryItem( handle=int(sys.argv[1]), url=itemurl, listitem=listitem, isFolder=True)

    itemurl = "plugin://plugin.video.youtube/channel/UCCNirCgrJmpONpinbBOiFog/playlists/"
    listitem = xbmcgui.ListItem( "[B][COLOR yellow]OPM ALL TIME FAVORITES[/COLOR][/B]", iconImage="DefaultVideo.png", thumbnailImage='http://sites.google.com/site/berklynelectronic/_/rsrc/1443968756855/videoke-machine/cabinet-dual-keypad-button/Videoke%2012x2%20Vip%20Dual.jpg' )
    listitem.setProperty('IsPlayable', 'true')
    xbmcplugin.addDirectoryItem( handle=int(sys.argv[1]), url=itemurl, listitem=listitem, isFolder=True)

################# Pinoy Movies Search ################## 

def MovieSearchAll():
    keyb = xbmc.Keyboard('', 'Search')
    keyb.doModal()
    if (keyb.isConfirmed()):
		search = keyb.getText().replace(' ','+')
		if search == '':
			exit()
		else:		
			OPEN = Open_Url('https://pastebin.com/raw/YM3HWX86')
			Regex = re.compile('<item title=.+?<link>(.+?)</link>',re.DOTALL).findall(OPEN)
			for searchurl in Regex:
				try:
					if 'pinoymoviepedia' in searchurl:
						url = searchurl + '/?s=' + search
						OPEN = Open_Url(url)
						Regex = re.compile('class="image".+?src="(.+?)".+?alt="(.+?)".+?href="(.+?)".+?class="contenido"><p>(.+?)</p>',re.DOTALL).findall(OPEN)
						for icon,name,url,description in Regex:
							name = name.replace('&#8217;','\'').replace('&#8211;','-').replace('&#39;','\'').replace('&#038;','&').replace('&#8230;','...')
							description = description.replace('&#8217;','\'').replace('&#8211;','-').replace('&#39;','\'').replace('&#038;','&').replace('<strong>','').replace('</strong>','').replace('&rsquo;','\'').replace('&lsquo;','\'').replace('&ldquo;','\"').replace('&rdquo;','\"').replace('&#8230;','...')
							icon = icon.replace('-185x278','').replace('-150x150','')
							addDir('%s' %name + ' - [COLOR aqua]PinoyMoviePedia[/COLOR]',url,12,icon,FANART,description)
					elif 'fullpinoymovies' in searchurl:
						url = searchurl + '/?s=' + search
						OPEN = Open_Url(url)
						Regex = re.compile('class="item".+?href="(.+?)".+?src="(.+?)" alt="(.+?)".+?class="ttx"> (.+?)<div class="degradado">',re.DOTALL).findall(OPEN)
						for url,icon,name,description in Regex:
							name = name.replace('&#8217;','\'').replace('&#8211;','-').replace('&#038;','&')
							description = description.replace('&#8217;','\'').replace('&#8211;','-').replace('&#038;','&').replace('&#124;','|').replace('\\n','; ')
							addDir('%s' %name + ' - [COLOR cornflowerblue]Full Pinoy Movies[/COLOR]',url,28,icon,FANART,description)						
				except:
					pass				
		setView('movies', 'mov-view')
    else: exit()
	
################################### 
 
def RESOLVE(url):
    try:
#        if 'speedvid.net' in url:
        if 'speedvid.net' in url:
            OPEN = Open_Url(url)
            link = re.compile('primary\|8777\|.+?primary\|(.+?)\|(.+?)\|.+?image\|mp4\|(.+?)\|',re.DOTALL).findall(OPEN)
            for port,server,hash in link:
                url = 'http://'+ server +'.speedvid.net:'+port+'/'+hash+'/v.mp4'
            stream_url=url
        elif 'watchpinoymoviesonline.info' in url:
            OPEN = Open_Url(url)
            url = re.compile('<iframe src="(.+?)"',re.DOTALL).findall(OPEN)[0]
            stream_url = urlresolver.resolve(url)
        elif 'pinoyhdflix.su' in url:
            OPEN = Open_Url(url)
            url = re.compile('<iframe loading="lazy" src="(.+?)"',re.DOTALL).findall(OPEN)[0]
            stream_url = urlresolver.resolve(url)
        elif 'https://ofwteleserye.net/' in url:
            OPEN = Open_Url(url)
            url = re.compile('<iframe src="(.+?)"',re.DOTALL).findall(OPEN)[0]
            stream_url = urlresolver.resolve(url)
        elif 'pinoymovieshub' in url:
            OPEN = Open_Url(url)
            url = re.compile('class="boton reloading".+?href="(.+?)"',re.DOTALL).findall(OPEN)[0]
            stream_url = urlresolver.resolve(url)
        elif 'pinoymovie.stream' in url:
            OPEN = Open_Url(url)
            Regex = re.compile("<iframe src='(.+?)'",re.DOTALL).findall(OPEN)
            for url in Regex:
				if 'http' not in url:
					url = 'http:' + url
				OPEN = Open_Url(url)
				url = re.compile('<source src="(.+?)"',re.DOTALL).findall(OPEN)[0]
				stream_url = url
        elif 'linkshare.tv' in url:
            OPEN = Open_Url(url)
            url = re.compile('<source src="(.+?)"',re.DOTALL).findall(OPEN)[0]
            stream_url = url
        elif 'relaxpinas' in url:
            OPEN = Open_Url(url)
            Regex = re.compile('var playlis(.+?)];',re.DOTALL).findall(OPEN)
            url = re.compile("'(.+?)'").findall(str(Regex))[0]
            stream_url = url			
        elif 'freepinoytvshows' in url:
            OPEN = Open_Url(url)
            url = re.compile('source: "(.+?)"',re.DOTALL).findall(OPEN)[0]
            stream_url = url
        elif 'vidio.com' in url:
            stream_url = url
        elif 'nodefiles.com' in url:
            stream_url = url
        elif 'streamable.com' in url:
            stream_url = url
        elif 'bit.ly' in url:
            OPEN = Open_Url(url)
            url = re.compile('"og:url" content="(.+?)"',re.DOTALL).findall(OPEN)[0]
            stream_url = urlresolver.resolve(url)
        elif 'archive' in url:
            OPEN = Open_Url(url)
            url = re.compile('"og:video" content="(.+?)"',re.DOTALL).findall(OPEN)[0]
            stream_url = url
        else:
			if urlresolver.HostedMediaFile(url).valid_url():
				stream_url = urlresolver.resolve(url)
			else:
				stream_url = url
        liz = xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=iconimage)
        liz.setInfo(type="Video", infoLabels={"Title": description})
        liz.setProperty("IsPlayable","true")
        liz.setPath(stream_url)
        xbmcplugin.setResolvedUrl(int(sys.argv[1]), True, liz)
    except:
        xbmc.executebuiltin("XBMC.Notification([COLOR cornflowerblue]Sorry[/COLOR],[COLOR red]Link is not available[/COLOR] ,3000)") 
        
def getSources():
        if os.path.exists(favorites) == True:
            addDir('Favorites','url',4,os.path.join(home, 'resources', 'favorite.png'),FANART,'','','','')
        if addon.getSetting("browse_xml_database") == "true":
            addDir('XML Database','http://xbmcplus.xb.funpic.de/www-data/filesystem/',15,icon,FANART,'','','','')
        if addon.getSetting("browse_community") == "true":
            addDir('Community Files','community_files',16,icon,FANART,'','','','')
        if os.path.exists(history) == True:
            addDir('Search History','history',25,os.path.join(home, 'resources', 'favorite.png'),FANART,'','','','')
        if addon.getSetting("searchyt") == "true":
            addDir('Search:Youtube','youtube',25,icon,FANART,'','','','')
        if addon.getSetting("searchDM") == "true":
            addDir('Search:dailymotion','dmotion',25,icon,FANART,'','','','')
        if addon.getSetting("PulsarM") == "true":
            addDir('Pulsar:IMDB','IMDBidplay',27,icon,FANART,'','','','')            
        if os.path.exists(source_file)==True:
            sources = json.loads(open(source_file,"r").read())
            #print 'sources',sources
            if len(sources) > 1:
                for i in sources:
                    ## for pre 1.0.8 sources
                    if isinstance(i, list):
                        addDir(i[0].encode('utf-8'),i[1].encode('utf-8'),1,icon,FANART,'','','','','source')
                    else:
                        thumb = icon
                        fanart = FANART
                        desc = ''
                        date = ''
                        credits = ''
                        genre = ''
                        if i.has_key('thumbnail'):
                            thumb = i['thumbnail']
                        if i.has_key('fanart'):
                            fanart = i['fanart']
                        if i.has_key('description'):
                            desc = i['description']
                        if i.has_key('date'):
                            date = i['date']
                        if i.has_key('genre'):
                            genre = i['genre']
                        if i.has_key('credits'):
                            credits = i['credits']
                        addDir(i['title'].encode('utf-8'),i['url'].encode('utf-8'),1,thumb,fanart,desc,genre,date,credits,'source')

            else:
                if len(sources) == 1:
                    if isinstance(sources[0], list):
                        getData(sources[0][1].encode('utf-8'),FANART)
                    else:
                        getData(sources[0]['url'], sources[0]['fanart'])


def addSource(url=None):
        if url is None:
            if not addon.getSetting("new_file_source") == "":
               source_url = addon.getSetting('new_file_source').decode('utf-8')
            elif not addon.getSetting("new_url_source") == "":
               source_url = addon.getSetting('new_url_source').decode('utf-8')
        else:
            source_url = url
        if source_url == '' or source_url is None:
            return
        addon_log('Adding New Source: '+source_url.encode('utf-8'))

        media_info = None
        #print 'source_url',source_url
        data = getSoup(source_url)
        print 'source_url',source_url
        if isinstance(data,BeautifulSOAP):
            if data.find('channels_info'):
                media_info = data.channels_info
            elif data.find('items_info'):
                media_info = data.items_info
        if media_info:
            source_media = {}
            source_media['url'] = source_url
            try: source_media['title'] = media_info.title.string
            except: pass
            try: source_media['thumbnail'] = media_info.thumbnail.string
            except: pass
            try: source_media['fanart'] = media_info.fanart.string
            except: pass
            try: source_media['genre'] = media_info.genre.string
            except: pass
            try: source_media['description'] = media_info.description.string
            except: pass
            try: source_media['date'] = media_info.date.string
            except: pass
            try: source_media['credits'] = media_info.credits.string
            except: pass
        else:
            if '/' in source_url:
                nameStr = source_url.split('/')[-1].split('.')[0]
            if '\\' in source_url:
                nameStr = source_url.split('\\')[-1].split('.')[0]
            if '%' in nameStr:
                nameStr = urllib.unquote_plus(nameStr)
            keyboard = xbmc.Keyboard(nameStr,'Displayed Name, Rename?')
            keyboard.doModal()
            if (keyboard.isConfirmed() == False):
                return
            newStr = keyboard.getText()
            if len(newStr) == 0:
                return
            source_media = {}
            source_media['title'] = newStr
            source_media['url'] = source_url
            source_media['fanart'] = fanart

        if os.path.exists(source_file)==False:
            source_list = []
            source_list.append(source_media)
            b = open(source_file,"w")
            b.write(json.dumps(source_list))
            b.close()
        else:
            sources = json.loads(open(source_file,"r").read())
            sources.append(source_media)
            b = open(source_file,"w")
            b.write(json.dumps(sources))
            b.close()
        addon.setSetting('new_url_source', "")
        addon.setSetting('new_file_source', "")
        xbmc.executebuiltin("XBMC.Notification(New source added.,5000,"+icon+")")
        if not url is None:
            if 'xbmcplus.xb.funpic.de' in url:
                xbmc.executebuiltin("XBMC.Container.Update(%s?mode=14,replace)" %sys.argv[0])
            elif 'community-links' in url:
                xbmc.executebuiltin("XBMC.Container.Update(%s?mode=10,replace)" %sys.argv[0])
        else: addon.openSettings()
	

def rmSource(name):
        sources = json.loads(open(source_file,"r").read())
        for index in range(len(sources)):
            if isinstance(sources[index], list):
                if sources[index][0] == name:
                    del sources[index]
                    b = open(source_file,"w")
                    b.write(json.dumps(sources))
                    b.close()
                    break
            else:
                if sources[index]['title'] == name:
                    del sources[index]
                    b = open(source_file,"w")
                    b.write(json.dumps(sources))
                    b.close()
                    break
        xbmc.executebuiltin("XBMC.Container.Refresh")

def Passkey():
	kb =xbmc.Keyboard ('', 'heading', True)
	kb.setHeading('Enter Password') # optional
	kb.setHiddenInput(True) # optional
	kb.doModal()
	if (kb.isConfirmed()):
		text = kb.getText()
		if addon.get_setting('password')==text:
			return xpinoymovies_cat()
		else:
			dialog = xbmcgui.Dialog()
			ok = dialog.ok('Attention!', ' \n                          You entered a wrong password.\n                                       Please Try Again!')
			return exit()
	else: exit()
	
		
def get_params():
	param=[]
	paramstring=sys.argv[2]
	if len(paramstring)>=2:
		params=sys.argv[2]
		cleanedparams=params.replace('?','')
		if (params[len(params)-1]=='/'):
			params=params[0:len(params)-2]
		pairsofparams=cleanedparams.split('&')
		param={}
		for i in range(len(pairsofparams)):
			splitparams={}
			splitparams=pairsofparams[i].split('=')
			if (len(splitparams))==2:
				param[splitparams[0]]=splitparams[1]
	return param

def Open_Url(url):
    headers = {}
    headers['User-Agent'] = User_Agent
    link = s.get(url, headers=headers).text
    link = link.encode('ascii', 'ignore')
    return link

    
    
def addDir(name,url,mode,iconimage,fanart,description):
	u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&iconimage="+urllib.quote_plus(iconimage)+"&description="+urllib.quote_plus(description)
	ok=True
	liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
	liz.setInfo( type="Video", infoLabels={"Title": name,"Plot":description})
	liz.setProperty('fanart_image', fanart)
	if mode==100 or mode==24 or mode==67 or mode==77 or mode==88 or mode==101 or mode==102:
		liz.setProperty("IsPlayable","true")
		ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=False)
	else:
		ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
	return ok

def setView(content, viewType):
	if content:
		xbmcplugin.setContent(int(sys.argv[1]), content)
	if addon.get_setting('auto-view') == 'true':
		xbmc.executebuiltin("Container.SetViewMode(%s)" % addon.get_setting(viewType) )
		
def linkView():
	xbmcplugin.setContent(int(sys.argv[1]), 'files')
    
params=get_params()
url=None
name=None
mode=None
iconimage=None
description=None
playlist=None
regexs=None

try:
	url=urllib.unquote_plus(params["url"])
except:
	pass
try:
	name=urllib.unquote_plus(params["name"])
except:
	pass
try:
	iconimage=urllib.unquote_plus(params["iconimage"])
except:
	pass
try:
	mode=int(params["mode"])
except:
	pass
try:
	description=urllib.unquote_plus(params["description"])
except:
	pass
try:
    playlist=eval(urllib.unquote_plus(params["playlist"]).replace('|',','))
except:
    pass
try:
    regexs=params["regexs"]
except:
    pass

if mode==None or url==None or len(url)<1 : MainDir()
elif mode == 1 : Search()
elif mode == 2 : year_3()
elif mode == 3 : Teleserye_Cat()
elif mode == 5 : Genre()
elif mode == 6 : MovieSearchAll()

elif mode==8:
    addon_log("rmSource")
    rmSource(name)

elif mode == 10 : moviepedia_cat()
elif mode == 11 : moviepedia_content(url)
elif mode == 12 : moviepedia_links(name,url)
elif mode == 13 : moviepedia_genre()
elif mode == 14 : moviepedia_year()
elif mode == 20 : watchpinoy_cat()
elif mode == 21 : watchpinoy_content(url)
elif mode == 22 : watchpinoy_genre(url)
elif mode == 23 : watchpinoy_live(url)
elif mode == 24 : watchpinoylive_resolve(url)
elif mode == 27 : fullpinoymovies_content(url)
elif mode == 28 : fullpinoymovies_links(name,url)
elif mode == 30 : pinoymoviestream_content(url)
elif mode == 31 : pinoymoviestream_links(name,url)
elif mode == 33 : pinoymovieshub_cat()
elif mode == 34 : pinoymovieshub_all_content(url)
elif mode == 35 : pinoymovieshub_latest_content(url)
elif mode == 36 : pinoymovieshub_tagdub_content(url)
elif mode == 37 : pinoymovieshub_links(name,url)
elif mode == 38 : pinoymovieshub_genres(url)
elif mode == 39 : pinoymovieshub_search()
elif mode == 40 : pinoymovieshubsearch_content(url)
elif mode == 41 : pinoymovieshub_genres_content(url)
elif mode == 45 : hdts_cat()
elif mode == 46 : hdts_content(url)
elif mode == 47 : hdts_links(name,url)
elif mode == 48 : absgma_search()
elif mode == 60 : absgma_content(url)
elif mode == 61 : absgma_links(name,url)
elif mode == 65 : lambingan_content(url)
elif mode == 66 : lambingan_links(name,url)
elif mode == 67 : lambingan_resolve(url)
elif mode == 68 : teleseryereplay_content(url)
elif mode == 69 : teleseryereplay_links(name,url)
elif mode == 75 : pinoytambayan_content(url)
elif mode == 76 : pinoystambayan_links(name,url)
elif mode == 77 : pinoystambayan_resolve(url)
elif mode == 78 : pinoyflix_content(url)
elif mode == 79 : pinoyhdflix_links(name,url)
elif mode == 82 : pinoyhdflix_content(url)
elif mode == 80 : teleseryetambayan_content(url)
elif mode == 81 : teleseryetambayan_links(name,url)
elif mode == 83 : pinoytvws_content(url)
elif mode == 84 : ofwpinoy_links(name,url)
elif mode == 86 : magtvnaph_content(url)
elif mode == 87 : magtvnaph_links(name,url)
elif mode == 90 : pbareplay_content(url)
elif mode == 91 : pbareplay_links(name,url)
elif mode == 96 : pinoytv_content(url)
elif mode == 97 : pinoytv_links(url)
elif mode == 98 : pinoytv_resolve(url)
elif mode == 99 : pinoyradio_content(url)
elif mode == 100: RESOLVE(url)
elif mode == 101: pbareplay_resolve(url)
elif mode == 103: Pelikula_Cat()
elif mode == 104: VideOke_Cat()
elif mode == 105: OPM()
elif mode == 106: ofwpinoyteleserye_content(url)
elif mode == 107: ofwpinoyteleserye_links(name,url)
elif mode == 108: OFWpinoy_content(url)
elif mode == 109: OFWpinoy_links(name,url)
elif mode == 110: test_content(url)
elif mode == 113: test_links(name,url)
elif mode == 111: pinoysflix_content(url)
elif mode == 112: pinoysflix_links(name,url)

elif mode == 200: pinoytvlive.getData(url,FANART)
elif mode == 201: pinoytvlive.getChannelItems(name,url,FANART)
elif mode == 202: pinoytvlive.getSubChannelItems(name,url,FANART)
elif mode == 203: pinoytvlive.play_playlist(name,playlist)
elif mode == 204: pinoytvlive.getRegexParsed(regexs,url) 
elif mode == 205:
    g_ignoreSetResolved=['plugin.video.f4mTester','plugin.video.SportsDevil','script.module.flash','plugin.video.youtube']
    if not any(x in url for x in g_ignoreSetResolved):
        item = xbmcgui.ListItem(path=url)
        xbmcplugin.setResolvedUrl(int(sys.argv[1]), True, item)
    else:
        xbmc.executebuiltin('XBMC.RunPlugin('+url+')')

xbmcplugin.endOfDirectory(int(sys.argv[1]))
