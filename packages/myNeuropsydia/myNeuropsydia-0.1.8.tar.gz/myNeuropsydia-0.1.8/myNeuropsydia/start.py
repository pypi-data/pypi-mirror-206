# -*- coding: utf-8 -*-



from .path import *
from .core import *
from .image import *
from .write import *
from .miscellaneous import *
import sys




def start(open_window=True):
    
    """
    Initialize all the components of Neuropsydia. Always at the beginning of a neuropsydia script.

    Parameters
    ----------
    open_window = bool
        should it open the pygame's window or close it immediatly (useful when using neuropsydia for something else than experiments, e.g., statistics)

    Returns
    ----------
    None

    Example
    ----------
    >>> import neuropsydia as n
    >>> n.start()
    >>> n.close()

    Authors
    ----------
    Dominique Makowski

    Dependencies
    ----------
    - pygame 1.9.2
    """
    
    
    global Font
    Font = Font_Cache_Init()  #Create the font object that will update itself with the different loaded fonts
    
    time = Time()
    
    pygame.init()
    
    pygame.display.set_icon(pygame.image.load(Path.logo() + 'icon.png'))
    screen = pygame.display.set_mode((0,0), pygame.SRCALPHA | pygame.FULLSCREEN | pygame.DOUBLEBUF | pygame.HWSURFACE)

    pygame.display.set_caption('Neuropsydia')
    screen_width, screen_height = screen.get_size()
    
    global_ = dict({'time': time,
                    'font': Font,
                    'screen': screen,
                    'screen_width': screen_width,
                    'screen_height': screen_height})
    
    pygame.mouse.set_visible(False)
    pygame.event.set_blocked(pygame.KEYDOWN)
     
    newpage("black", auto_refresh=False)
    pygame.event.set_allowed(pygame.KEYDOWN)
    
    for event in pygame.event.get():
        print(event)
    time_out = False
    loop = True
    local_time = Time()
    time_max = 1
    while loop and local_time.get(reset=False) < time_max:
        for event in pygame.event.get():
            print(event)

    refresh()
    
    if open_window == False:
        pygame.event.set_allowed(pygame.KEYDOWN)
        pygame.mouse.set_visible(True)
        pygame.quit()

    else:
        newpage("black", auto_refresh=False)
        write('Initialisation...', global_,
              size=0.8, y=-9, color="lightblue")
        refresh()

        preloaded = {}
        preloaded = preload("Neuropsydia_PSY_blue", 
                            global_,
                            extension = ".png", 
                            y= -2.5, 
                            size=14, 
                            cache = preloaded, 
                            path = Path.logo())
        preloaded = preload("Neuropsydia_TEXT_white", 
                            global_,
                            extension = ".png",
                            y= 7,
                            size=5, 
                            cache = preloaded, 
                            path = Path.logo())
        preloaded = preload("Neuropsydia_HEAD_white",
                            global_,
                            extension = ".png", 
                            y= -2.5, 
                            size=14, 
                            cache = preloaded, 
                            path = Path.logo())

        newpage("black", auto_refresh=False)
        image("Neuropsydia_TEXT_white",
              global_, 
              extension = ".png", 
              y= 7,
              size=5,
              cache = preloaded, 
              path = Path.logo())
        image("Neuropsydia_PSY_blue",
              global_, 
              extension = ".png",
              y= -2.5, 
              size=14, 
              cache = preloaded,
              path = Path.logo())
        write('Press ENTRER to continue.', 
              global_,
              size=0.8,
              y=-9, 
              color="white", 
              allow="ENTER")

        # Fade
        for i in range(0,100,2):
            newpage("black", 
                    auto_refresh=False)
            image("Neuropsydia_HEAD_white",
                  global_, 
                  extension = ".png",
                  y= -2.5, 
                  size=14, 
                  cache = preloaded, 
                  path = Path.logo())
            newpage("black",
                    opacity = 100 - i, 
                    auto_refresh=False)
            image("Neuropsydia_TEXT_white", 
                  global_, 
                  extension = ".png", 
                  y= 7, 
                  size=5, 
                  cache = preloaded, 
                  path = Path.logo())
            image("Neuropsydia_PSY_blue",
                  global_,  
                  extension = ".png",
                  y= -2.5, 
                  size=14, 
                  cache = preloaded,
                  path = Path.logo())
            refresh()
            
        time.wait(800)
        newpage("white", fade=True)
        refresh()
        
        return global_
        
        
def close(global_):
    
    """
    A clean closing of all the components of Neuropsydia. Always at the end of a neuropsydia script.

    Parameters
    ----------
    None

    Returns
    ----------
    None

    Example
    ----------
    >>> import neuropsydia as n
    >>> n.start()
    >>> n.close()

    Authors
    ----------
    Dominique Makowski

    Dependencies
    ----------
    - pygame 1.9.2
    """
    
    
    screen = global_['screen']
    screen_width = global_['screen_width']
    screen_height = global_['screen_height']
    Font = global_['font']
    time = global_['time']
    
    newpage("black", auto_refresh=False)
    write("Please wait...", global_,
          color="white")
    refresh()

    preloaded = {}
    preloaded = preload("Neuropsydia_TEXT_white", 
                        global_,
                        extension = ".png", 
                        y= 5.5, size=4, 
                        cache = preloaded, 
                        path = Path.logo())
    preloaded = preload("Neuropsydia_HEAD_white",  
                        global_,
                        extension = ".png", 
                        y= -3, size=12.5, 
                        cache = preloaded, 
                        path = Path.logo())
    preloaded = preload("Neuropsydia_PSY_blue", 
                        global_,
                        extension = ".png", 
                        y= -3, size=12.5, 
                        cache = preloaded, 
                        path = Path.logo())
    preloaded = preload('N', 
                        global_,
                        extension = ".png", 
                        x=7, y=-8, size=2.5, 
                        cache = preloaded, 
                        path = Path.logo())
    preloaded = preload("Python", 
                        global_,
                        extension = ".png", 
                        x=-7, y=-8, size=2.5, 
                        cache = preloaded, 
                        path = Path.logo())

    for i in range(0,100,2):
        newpage("black", auto_refresh=False)
     
        write("Thank you for using", 
              global_,
              style="light", 
              y=8.75, 
              size=1, 
              color="white")
        
        image("Neuropsydia_TEXT_white",
              global_, 
              extension = ".png", 
              y= 5.5, 
              size=4, 
              cache = preloaded,
              path = Path.logo())
        image("Neuropsydia_HEAD_white", 
              global_, 
              extension = ".png", 
              y= -3, 
              size=12.5, 
              cache = preloaded,
              path = Path.logo())
        image("Neuropsydia_PSY_blue",
              global_, 
              extension = ".png", 
              y= -3, 
              size=12.5, 
              cache = preloaded, 
              path = Path.logo())
        image('N', 
              global_, 
              extension = ".png",
              x=7, y=-8, size=2.5, 
              cache = preloaded, 
              path = Path.logo())
        image("Python", 
              global_, 
              extension = ".png", 
              x=-7, y=-8, 
              size=2.5, 
              cache = preloaded, 
              path = Path.logo())
        newpage("black", 
                opacity = 100-i, 
                auto_refresh=False)
        refresh()
    time.wait(1500)

    pygame.event.set_allowed(pygame.KEYDOWN)
    pygame.mouse.set_visible(True)
    pygame.quit()
    sys.exit()
    
   




