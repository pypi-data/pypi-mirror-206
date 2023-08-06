from baopig import *


class UT_Sleep_Zone(Zone):
    def __init__(self, *args, **kwargs):
        Zone.__init__(self, *args, **kwargs)

        Layer(self, name="zones_layer", spacing=10)
        z1 = Zone(self, size=("100%", 50), background_color=(150, 150, 150), padding=10, spacing=5)
        z2 = Zone(self, size=("100%", 250), background_color=(150, 150, 150))
        z3 = Zone(self, size=("100%", 335), background_color=(150, 150, 150))
        self.default_layer.pack()

        # Z1
        def tog(widg):
            clicked_button = mouse.hovered_widget
            if widg.is_dead:
                clicked_button.text_widget.set_text("state:DEAD")
            elif widg.is_asleep:
                widg.wake()
                if widg.is_dead:
                    clicked_button.text_widget.set_text("state:DEAD")
                else:
                    clicked_button.text_widget.set_text("state:AWAKE")
            else:
                if widg.is_alive:
                    widg.sleep()
                    clicked_button.text_widget.set_text("state:ASLEEP")

        main = Text(z1, text="sleepy Text", font_color="blue", background_color="blue4", padding=5, size=(100, 30))
        Button(z1, text="state:AWAKE", command=PrefilledFunction(tog, main), height=30)
        r2 = Rectangle(z1, color="red")
        main.signal.SLEEP.connect(lambda: r2.set_color("black"), owner=r2)
        main.signal.WAKE.connect(lambda: r2.set_color("red3"), owner=r2)
        z1.default_layer.pack(axis="horizontal")

        # Z2
        def add():
            if z2.test_zone.texts.is_dead:
                z2.test_zone.texts = Zone(z2.test_zone, size=(z2.rect.w - 100, "100%"))
                z2.test_zone.togglers.default_layer.clear()
                z2.test_zone.default_layer.pack(axis="horizontal")
            t = Text(z2.test_zone.texts, text=f"index:{z2.index}",
                     border_width=2, padding=5, align_mode="center", pos=(0, z2.index * 35))
            Button(z2.test_zone.togglers, text="state:AWAKE", command=PrefilledFunction(tog, t), pos=t.rect.topleft)
            z2.index += 1

        z2.index = 0
        z2.param_zone = Zone(z2, size=("100%", 35))
        z2.test_zone = Zone(z2, size=("100%", z2.rect.h - z2.param_zone.rect.h), background_color=(130, 130, 130))
        z2.default_layer.pack()
        z2.test_zone.texts = Zone(z2.test_zone, size=(z2.rect.w - 100, "100%"))
        z2.test_zone.togglers = Zone(z2.test_zone, size=(100, "100%"))
        z2.test_zone.default_layer.pack(axis="horizontal")
        b = Button(z2.param_zone, "ADD", command=add)
        DynamicText(z2.param_zone, get_text=lambda: f"LEN:{len(z2.test_zone.texts.children)}",
                    size=b.rect.size, align_mode="center", padding=(0, b.text_widget.rect.top))

        def clear():
            if z2.test_zone.texts.is_alive:
                z2.test_zone.texts.default_layer.clear()
            z2.test_zone.togglers.default_layer.clear()
            z2.index = 0

        Button(z2.param_zone, "CLEAR", command=clear)

        def kill():
            if z2.test_zone.texts.is_alive:
                z2.test_zone.texts.kill()
                z2.index = 0

        Button(z2.param_zone, "KILL", command=kill)
        z2.param_zone.default_layer.pack(axis="horizontal")

        # Z3
        class DraggableRectangle(Rectangle, DraggableByMouse):
            def __init__(self, parent, **kwargs2):
                Rectangle.__init__(self, parent, **kwargs2)
                DraggableByMouse.__init__(self, parent, **kwargs2)

        z3.set_style_for(Rectangle, color=(110, 80, 90))
        clone_zone = Zone(z3, size=("100%", 150))
        original_zone = Zone(z3, size=("100%", 150))
        original = DraggableRectangle(original_zone, color=(116, 0, 32))
        clone = Rectangle(clone_zone, size=original.rect.size, pos=(0, - 150 - 35), ref=original)
        clone2 = Rectangle(clone_zone, size=clone.rect.size, pos=(50, 0), ref=clone, color=(110, 100, 100))
        # TODO : solve: an adaptable size is not linked to the ref but to the parent
        b = Button(z3, text="state:AWAKE", width="25%", command=PrefilledFunction(tog, clone))
        b.move_behind(original_zone)
        z3.default_layer.pack()

        def handle_resize():
            clone.resize(*original.rect.size)

        original.signal.RESIZE.connect(handle_resize, owner=clone)

        def handle_new_surface():
            cloned_color = original.color.copy()
            cloned_color.s -= 50
            clone.set_color(cloned_color)

        original.signal.NEW_SURFACE.connect(handle_new_surface, owner=clone)
        handle_new_surface()

        def handle_resize():
            clone2.resize(*clone.rect.size)

        clone.signal.RESIZE.connect(handle_resize, owner=clone2)

        def handle_new_surface():
            cloned_color = clone.color.copy()
            cloned_color.s -= 10
            clone2.set_color(cloned_color)

        clone.signal.NEW_SURFACE.connect(handle_new_surface, owner=clone2)
        handle_new_surface()

        def resize():
            if original.rect.width == 30:
                original.resize(40, 40)
            elif original.rect.width == 40:
                original.resize(20, 20)
            else:
                original.resize(30, 30)

        b2 = Button(z3, text="Resize", width="25%", ref=b, refloc="topright", command=resize)

        def toggle_visibility():
            clicked_button = mouse.hovered_widget
            if clone.is_visible:
                clone.hide()
                clicked_button.text_widget.set_text("state:HIDDEN")
            else:
                clone.show()
                clicked_button.text_widget.set_text("state:VISIBLE")

        b3 = Button(z3, text="state:VISIBLE", width="25%", ref=b2, refloc="topright", command=toggle_visibility)

        def toggle_color():
            clicked_button = mouse.hovered_widget
            text = clicked_button.text_widget.text
            if text == "state:RED":
                clicked_button.text_widget.set_text("state:GREEN")
            elif text == "state:GREEN":
                clicked_button.text_widget.set_text("state:BLUE")
            else:
                clicked_button.text_widget.set_text("state:RED")
            original.color.h = (original.color.h + 120) % 360
            original.send_paint_request()

        Button(z3, text="state:RED", width="25%", ref=b3, refloc="topright", command=toggle_color)

        # Z5
        # TODO : try to asleep a widget from a BoxLayout, and then wake it up

    def load_sections(self):
        """
        If the parent got killed:
            Kills the widget
        Attaches the widget to its parent
        Updates the widget's size & position
        Emits the WAKE signal
        """

        self.parent.add_section(
            title="Sleeping state",
            tests=[
                "When a sleeping widget wakes up, the signal WAKE is emitted",
                "When a widget goes to sleep, the signal SLEEP is emitted",
                "A sleeping widget is not inside its parent",
                "When a sleeping widget wakes up, if its parent is dead, the widget dies",
                "When a sleeping widget wakes up, if its parent got resized, the widget reacts",
                "When a sleeping widget wakes up, if its parent moved, the widget reacts",
                "Widget.hide() & Widget.show() are alright with sleepy widgets",
            ]
        )


# For the PresentationScene import
ut_zone_class = UT_Sleep_Zone

if __name__ == "__main__":
    from baopig.prefabs.testerscene import TesterScene
    app = Application()
    TesterScene(app, ut_zone_class)
    app.launch()
