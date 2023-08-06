import pygame
from .utilities import paint_lock
from .widget import Widget
from .container import Container


class Zone(Container):
    STYLE = Container.STYLE.substyle()
    STYLE.modify(
        width=100,
        height=100,
    )

    def divide(self, side, width):
        # TODO : rework this function
        if side == "left":
            self.rect.left = width
            self.rect.w -= width
            if self.rect.w <= 0:
                raise ValueError("the new zone shouldn't completly override the central zone")
            zone = Zone((width, self.rect.h))
        else:
            return
        return zone


class SubZone(Zone):  # TODO : SubScene ? with rects_to_update ?
    # TODO : solve : when update on a SubZone whose parent is a scene, the display isn't updated
    """A SuzZone is an optimized Zone, its surface is a subsurface of its parent (cannot have transparency)"""

    def __init__(self, parent, **kwargs):

        Zone.__init__(self, parent, **kwargs)
        try:
            self._surface = self.parent.surface.subsurface(self.rect.topleft + self.rect.size)
        except ValueError:
            assert not self.parent.auto_rect.contains(self.rect)
            raise PermissionError("A SubZone must fit inside its parent")

        self.parent.signal.NEW_SURFACE.connect(self._update_subsurface, owner=self)
        self.signal.MOTION.connect(self._update_subsurface, owner=self)

    def _update_subsurface(self):

        with paint_lock:
            try:
                Widget.set_surface(self, self.parent.surface.subsurface(self.rect.topleft + self.rect.size))
            except ValueError:
                assert not self.parent.auto_rect.contains(self.rect)
                Widget.set_surface(self, self.parent.surface.subsurface(
                    pygame.Rect(self.rect).clip(self.parent.auto_rect)))  # resize the subzone

    def _flip(self):  # TODO : check with new padding & etc
        """Update all the surface"""

        if self.is_hidden:
            return

        with paint_lock:  # TODO : usefull ?

            self._flip_without_update()

            # optimization
            if self.parent is self.scene:
                pygame.display.update(self.hitbox)
            else:
                self.parent.send_display_request(
                    rect=(self.parent.left + self.hitbox.left, self.parent.top + self.hitbox.top) + self.hitbox.size
                )

    def _update_surface_from_resize(self, asked_size):

        with paint_lock:
            try:
                Widget.set_surface(self, self.parent.surface.subsurface(self.rect.topleft + asked_size))
            except ValueError:
                assert not self.parent.auto_rect.contains(self.rect)
                raise PermissionError("A SubZone must fit inside its parent")
            self._flip_without_update()

    def _warn_parent(self, rect):
        """Request updates at rects referenced by self"""

        rect = (self.rect.left + rect[0], self.rect.top + rect[1]) + tuple(rect[2:])

        # because of subsurface, we can skip self.parent._update_rect()
        if self.parent is self.scene:
            pygame.display.update(rect)
        else:
            self.parent._warn_parent(rect)
