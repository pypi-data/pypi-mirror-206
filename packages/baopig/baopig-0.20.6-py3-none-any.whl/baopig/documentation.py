from typing import Iterable

import pygame


class Communicative:
    """
    Class for objects who need to emit signals

    :Example:
    ---------
        class Transmitter(bp.Communicative):
            def __init__(self, message):
                bp.Communicative.__init__(self)
                self.message = message
                self.create_signal("EMISSION")
            def transmit(self):
                self.signal.EMISSION.emit(self.message)

        class Listener(bp.Communicative):
            def receive(self, message):
                print(f"Message received: {message}")

        my_transmitter = Transmitter("Hello world !")
        my_listener = Listener()
        my_transmitter.signal.EMISSION.connect(my_listener.receive, owner=my_listener)
        my_transmitter.transmit()  # prints : 'Message received: Hello world !'
        my_listener.disconnect()
        my_transmitter.transmit()  # prints nothing

    :Attributes:
    ------------
        signal: object -> an object containing all the signals

    :Methods:
    ---------
        create_signal(signal_id) -> creates a signal accessible via 'signal_id'
        disconnect()             -> kills all the connections owned by this object
    """

    def create_signal(self, signal_id: str):
        """
        Creates a signal accessible via 'signal_id'
        'signal_id' must be an uppercase string

        After obj.create_signal("EMISSION"), the created signal is accessed this way:
            obj.signal.EMISSION
        """

    def disconnect(self):
        """ Kills all the connections owned by this object """


class ProtectedRect:
    pass


class Widget(Communicative):
    """
    Abstract class for the graphical elements of the screen
    A widget can be visible, hidden, awake, sleeping, alive, or dead
    A widget has only one parent (baopig bio-logic, hmmm...)
    A widget has to initialize its surface at its creation

    WARNING : A widget's surface is not connected to its widget (that is way too hard)
              Any change on the surface has to come with :
                  - a signal emission : widget.signal.NEW_SURFACE.emit()
                  - a display request : widget.send_display_request()
              This is not required when you use the set_surface() method

    :Constructor:
    -------------
        parent: Container       -> the widget's parent
        surface: pygame.Surface -> the widget's image
        visible: bool           -> if False, the widget's hide() method is called
        sticky: Location        -> if set, overrides 2 style attributes : pos_loc & refloc
        **style: keyword args   -> the widget's style attributes

    :Signals:
    ---------
        HIDE: emitted when the widget's visibility state goes from visible to hidden
        KILL: emitted when the widget gets killed
        SHOW: emitted when the widget's visibility state goes from hidden to visible
        SLEEP: emitted when the widget's sleeping state goes from awake to asleep
        WAKE: emitted when the widget's sleeping state goes from asleep to awake

    :Attributes:
    ------------

        :Style attributes:
        -----------------------
            pos: Iterable[int]         -> the position
            loc: Location              -> the position's location on the widget's rect
            ref: Container | None      -> the position's position reference, if None, set to parent
            refloc: Location           -> the position's position reference location, from the reference's rect
            referenced_by_hitbox: bool -> if True, position is referenced by the ref's hitbox  # TODO : tests

        parent: Container -> the manager

        surface: pygame.Surface -> the widget's image
        rect: pygame.Rect       -> the widget's size
        hitbox: pygame.Rect     -> the widget's size on the screen
        pos_manager: object     -> the widget's position manager. See documentation at TODO

        is_alive: bool   -> True if the widget has not been killed
        is_asleep: bool  -> True if the widget is asleep
        is_awake: bool   -> True if the widget is not asleep
        is_dead: bool    -> True if the widget has been killed
        is_hidden: bool  -> True if the widget is not visible
        is_visible: bool -> True if the widget is visible

    :Methods:
    ---------
        set_pos(pos=None, pos_loc=None, refloc=None) -> moves the widget  # TODO
            # pos = pos + ref.abs_rect.refloc - parent.abs_rect.topleft
            # rect.pos_loc = pos
            # signal.MOTION.emit()

        set_size(width, height) -> resizes the widget  # TODO
            # rect.size = width, height
            # signal.RESIZE.emit()

        set_surface() TODO

        hide()  -> the widget is no longer visible
        kill()  -> the widget is permanently deleted
        show()  -> the widget is visible again
        sleep() -> the widget is detached from its parent
        wake()  -> the widget is reattached to its parent

        send_display_request(rect=None) -> sends a request who will update the display
    """

    application: ...
    is_alive: bool
    is_asleep: bool
    is_awake: bool
    is_dead: bool
    is_hidden: bool
    is_touchable_by_mouse: bool
    is_visible: bool
    parent: ...
    pos_manager: ...
    scene: ...
    surface: pygame.Surface

    # HITBOX
    abs_hitbox: ProtectedRect
    abs_rect: ProtectedRect
    auto_hitbox: ProtectedRect
    auto_rect: ProtectedRect
    hitbox: ProtectedRect
    rect: ProtectedRect
    window: ProtectedRect

    def hide(self):
        """
        Stop displaying the widget

        Behaviour:
        ----------
            Sets visibility to False
            Sends a display request
            Emits the HIDE signal
        """

    def kill(self):
        """
        Kills the widget
        A killed widget should not be used ever again

        Behaviour:
        ----------
            Detaches the widget from its parent
            Emits the KILL signal
            Kills all the connections owned by the widget
            Kills the widget's weakref
        """

    def send_display_request(self, rect: Iterable[int] | None = None):
        """
        Sends a request who will update the display
        The request is executed by a thread dedicated to the screen's display
        rect represents a pygame.Rect object
        rect must be referenced by the widget's parent
        If rect is not set, the widget's hitbox will be used
        Only the screen's portion corresponding to rect will be updated
        """

    def show(self):
        """
        Starts to display the widget again

        Behaviour:
        ----------
            Sets visibility to True
            Sends a display request
            Emits the SHOW signal
        """

    def sleep(self):
        """
        Detaches the widget from its parent
        A sleeping widget cannot move

        Behaviour:
        ----------
            Detaches the widget from its parent
            Emits the SLEEP signal
        """

    def wake(self):
        """
        Reattaches the widget to its parent

        Behaviour:
        ----------
            If the parent got killed:
                Kills the widget
            Attaches the widget to its parent
            Updates the widget's size & position
            Emits the WAKE signal
        """

    # TODO : merge
    """
    Class for widgets who may need to update their surface.

    Attribute dirty means the widget's surface has to be updated.
    The widget's surface is updated through the paint() method.
    The paint() method is executed by a thread dedicated to the screen's display.
    If an asleep widget is dirty, the paint() method is called when the widget awakes.
    WARNING : It is deprecated to call paint() yourself, use send_paint_request() instead.

    :Attributes:
    ------------
        dirty: int
            -> if 0, paint() is not requested
            -> if 1, paint() is called at next frame rendering, then dirty will be set to 0 again
            -> if 2, paint() is called at each frame rendering

    :Methods:
    ---------
        paint()              -> abstract - updates the widget's surface
        send_paint_request() -> sends a request who will execute once the widget's paint() method
        set_dirty(val)       -> sets the widget's dirty attribute
    """
    def paint(self):
        """
        Abstract - called at a frame rendering, if the widget is dirty.

        WARNING : NEVER CALL paint() YOURSELF !! Use send_paint_request() instead.

        When called by a paint_request, paint() is followed by these 2 events:
            - widget's signal NEW_SURFACE is emitted
            - a display_request is sent

        :Examples:

            def paint(self):
                surf = get_the_new_surface()
                self.set_surface(surf)

            def paint(self):
                self.surface.blit(another_surface, (0, 0))
        """

    def send_paint_request(self):
        """
        Sends a request who will execute once the widget's paint() method
        The request is executed by a thread dedicated to the screen's display
        Acts almost like set_dirty(1)
        """

    def set_dirty(self, val: int):
        """
        Sets the widget's dirty attribute

        Paintable.dirty:
            if 0, paint() is not requested
            if 1, paint() is called at next frame rendering, then dirty will be set to 0 again
            if 2, paint() is called at each frame rendering
        """


class HoverableByMouse(Widget):
    """
    Class for widgets who need to handle when they are hovered or unhovered by the mouse.

    A HoverableByMouse can have an Indicator, i.e. a Text that appears when the HoverableByMouse is hovered.
    For more details, see TODO : link to Indicator documentation

    TODO : test : a disabled HoverableByMouse cannot be hovered
    TODO : test : an enabled HoverableByMouse can grab the hover
    TODO : test : a disabled & hovered HoverableByMouse drops the hover

    :Signals:
    ---------
        HOVER: emitted when the widget gets hovered by the mouse
        UNHOVER: emitted when the widget gets unhovered from the mouse

    :Attributes:
    ------------
        is_hovered: bool     -> True if the mouse is hovering the widget
        indicator: Indicator -> the widget's indicator, not always set
        # TODO : why is there a ref ? cannot have multiple indicators ?

    :Methods:
    ---------
        handle_hover()   -> abstract - called when the widget gets hovered by the mouse
        handle_unhover() -> abstract - called when the widget gets unhovered from the mouse
    """

    def handle_hover(self):
        """ Abstract - called when the widget gets hovered by the mouse """

    def handle_unhover(self):
        """ Abstract - called when the widget gets unhovered from the mouse """


class Paintable(Widget):  # TODO : remove
    pass


class Runable(Widget):
    """
    Class for widgets who need to execute their run() method as much as possible.

    By default, is_running is set to False.

    :Attributes:
    ------------
        is_running: bool -> True if the widget is running

    :Methods:
    ---------
        run() -> abstract - called as much as possible, while the object is running

        set_running(val) -> starts or stops to run the widget
    """

    is_running: bool

    def run(self):
        """ Abstract - called as much as possible, while the object is running """

    def set_running(self, val):
        """ Starts or stops to run the widget """


# ...


"""

                                      Widget   -> set_touchable_by_mouse()
                                 
                                         |
                                 
                                 HoverableByMouse
                                 
                                         |
                                 
                                 LinkableByMouse       
                                 
                                          \
                                 
                                           Focusable  ( KeyEventsListener )
                                 
                                                \     
                                                 \    
                    Clickable                     \     
                                                   \  
                                                    \ 
                                         --------------------------------------
                                         |                                    |
                                     
                                       Button                             Selector
                                       
                                                                              |
                                                                              
                                                                          TextEdit
                                                                          LineEdit
                                                                          Entry
                                                                          NumEntry
                                                                          ColorEntry


"""


class Validable:
    pass


class ScrollableByMouse(Widget):

    def handle_mouse_scroll(self, scroll_event):
        """TODO"""


class LinkableByMouse(HoverableByMouse):
    """
    Class for widgets who need to capture mouse clicks

    A LinkableByMouse is linked when a mouse LEFT BUTTON DOWN collide with it,
    and unlinked when the LEFT BUTTON UP occurs

    It has no 'link' or 'link_motion' method since it is the mouse who manages links.
    However, it can unlink itself

    WARNING : If a LinkableByMouse parent contains a LinkableByMouse child, and the LEFT BUTTON
              DOWN has occured on the child, then only the child will be linked

    NOTE : when a widget is linked, you can access it via mouse.linked_widget
    """


class Focusable(LinkableByMouse):
    """
    Class for widget who listen to keyboard input, when it has the focus. Only one
    widget can be focused in the same time. When a new clic occurs, and it doesn't collide
    this widget, it is defocused.

    It has no 'focus' method since it is the application who decide who is focused or not.
    However, it can defocus itself.

    When the mouse click on a Text inside a Button inside a focusable Zone inside a Scene,
    then only the youngest Focusable is focused
    Here, it is the Button -> scene.focused_widget = Button
    """

    def handle_keydown(self, key: int):
        """ Called when a key is pressed """

    def handle_keyup(self, key: int):
        """ Called when a key is released """


class Container(Widget):
    """
    Widgets parent

    Attributes:
    -----------
        children: list -> the list of all the children
    """

    layers_manager: ...


class Selector(Container, Focusable):
    """
    Class for containers who need to handle when they are linked
    and then, while the mouse is still pressed, to handle the mouse drag in
    order to simulate a rect from the link origin to the link position and
    select every SelectableWidget object who collide with this rect
    """


class Layout(Container):
    """
    Widgets's size and position manager

    Attributes:
    -----------
        padding: Margin
        spacing: Margin

        content_rect: pygame.Rect -> the space for children

    """


class Zone(Container):
    """
    Convenient Widgets manager

    Attributes:
    -----------
        background: Layer
        content: Layer
        foreground: Layer
    """


class Scene(Zone):
    """
    An application frame

    Methods:
        open
    """


class ApplicationExit(Exception):
    pass
