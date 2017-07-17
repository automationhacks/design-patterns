import weakref


class Link(object):

    def __init__(self, ref, text, image_path=None):
        self.ref = ref
        if image_path:
            self.image = browser_image(image_path)
        else:
            self.image = None
        self.text = text

    def __str__(self):
        if not self.image:
            return "<Link (%s)>" % self.text
        else:
            return "<Link (%s,%s)>" % (self.text, str(self.image))


class browser_image(object):
    _resources = weakref.WeakValueDictionary()

    def __new__(cls, location):
        image = browser_image._resources.get(location, None)
        if not image:
            image = object.__new__(cls)
            browser_image._resources[location] = image
            image.__init(location)
        return image

    def __init(self, location):
        self.location = location
        # self.content = load picture into memory

    def __str__(self,):
        return "<BrowserImage(%s)>" % self.location

icon = Link("www.pythonunlocked.com",
            "python unlocked book",
            "http://pythonunlocked.com/media/logo.png")
footer_icon = Link("www.pythonunlocked.com/#bottom",
                   "unlocked series python book",
                   "http://pythonunlocked.com/media/logo.png")
twitter_top_header_icon = Link("www.twitter.com/pythonunlocked",
                               "python unlocked twitter link",
                               "http://pythonunlocked.com/media/logo.png")

print(icon,)
print(footer_icon,)
print(twitter_top_header_icon,)