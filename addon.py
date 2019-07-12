from xbmcswift2 import Plugin, xbmcgui
from resources.lib import jimmydoreshow

plugin = Plugin()

URL = "https://thejimmydoreshow.libsyn.com/rss"
URL2 = "https://comedyandeverythingelse.libsyn.com/rss"

@plugin.route('/')
def main_menu():
    """
    main menu 
    """
    items = [
        {
            'label': plugin.get_string(30000), 
            'path': plugin.url_for('all_episodes'),
            'thumbnail': "https://ssl-static.libsyn.com/p/assets/b/0/4/3/b043eaa3e36ed529/JDPodThumb1.jpg"},
   {
            'label': plugin.get_string(30001), 
            'path': plugin.url_for('all_episodes1'),
            'thumbnail': "https://ssl-static.libsyn.com/p/assets/b/0/4/3/b043eaa3e36ed529/JDPodThumb1.jpg"},
   {
            'label': plugin.get_string(30001), 
            'path': plugin.url_for('all_comedy'),
            'thumbnail': "https://ssl-static.libsyn.com/p/assets/7/9/5/3/7953b2f961f84fe3/caee-for-podcast.jpg"},

    ]

    return items


@plugin.route('/all_episodes/')
def all_episodes():
    """
    contains playable podcasts listed as just-in
    """
    soup = jimmydoreshow.get_soup(URL)
    
    playable_podcast = jimmydoreshow.get_playable_podcast(soup)
    
    items = jimmydoreshow.compile_playable_podcast(playable_podcast)

    return items


@plugin.route('/all_episodes1/')
def all_episodes1():
    """
    contains playable podcasts listed as just-in
    """
    soup = jimmydoreshow.get_soup(URL)
    
    playable_podcast1 = jimmydoreshow.get_playable_podcast1(soup)
    
    items = jimmydoreshow.compile_playable_podcast1(playable_podcast1)

    return items


@plugin.route('/all_comedy/')
def all_comedy():
    """
    contains playable podcasts listed as just-in
    """
    soup2 = jimmydoreshow.get_soup(URL2)
    
    playable_comedy = jimmydoreshow.get_playable_comedy(soup2)
    
    items = jimmydoreshow.compile_playable_comedy(playable_comedy)

    return items


if __name__ == '__main__':
    plugin.run()
