# CNBC Plex Channel Plug-in
# Revised:
    
DEVELOPMENT = True
if DEVELOPMENT:
    ICON = 'icon-dev.png'
    NAME = 'CNBC-Unstable'
    PREFIX = '/video/cnbc-unstable'
    HTTP.CacheTime = 0
else:
    ICON = 'icon-default.png'
    NAME = 'CNBC'
    PREFIX = '/video/cnbc'

ART = 'art-default.jpg'

VIDEO_TYPES = [
    {'type': 'Top', 'title': 'Top Video'},
    {'type': 'Latest', 'title': 'Latest Video'},
    {'type': 'US', 'title': 'US Video'},
    {'type': 'Asia', 'title': 'Asia Video'},
    {'type': 'Europe', 'title': 'Europe Video'},
    {'type': 'CEO', 'title': 'CEO Interviews'},
    {'type': 'Analyst', 'title': 'Analyst Interviews'},
    {'type': 'Full', 'title': 'Full Episodes'}
]

####################################################################################################
def Start(title=NAME):
    ObjectContainer.art = R(ART)
    ObjectContainer.title1 = NAME
    DirectoryObject.thumb = R(ICON)
    NextPageObject.thumb = R(ICON)
    VideoClipObject.thumb = R(ICON)

####################################################################################################
@handler(PREFIX, NAME, art=R(ART), thumb=R(ICON))
def MainMenu():
    oc = ObjectContainer(title2=NAME)

    for item in VIDEO_TYPES:
        oc.add(
            DirectoryObject(
                key = Callback(VideoDir, vtitle=item['title'], vtype=item['type']),
                title = item['title']
            )
        )

    if len(oc) < 1:
        return ObjectContainer(header='Empty', message='There are no Videos to list')
    else:
        return oc

####################################################################################################
@route(PREFIX + '/videodir')
def VideoDir(vtitle, vtype):
    oc = ObjectContainer(title2=vtitle)


    currUrl = 'http://video.cnbc.com/gallery/?video=3000578438'

    oc.add(
        VideoClipObject(
            url = currUrl,
            title = vtitle,
##            summary = 'Source:  %s' % (currUrl),
            thumb = R(ICON)
        )
    )


    if len(oc) < 1:
        return ObjectContainer(header='Empty', message='There are no Videos to list')
    else:
        return oc

####################################################################################################
