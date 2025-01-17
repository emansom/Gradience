# preset_row.py
#
# Change the look of Adwaita, with ease
# Copyright (C) 2022  Gradience Team
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.

import json
import os

from gi.repository import Gtk, Gdk, Adw

from .constants import rootdir
from .modules.utils import to_slug_case, buglog


@Gtk.Template(resource_path=f"{rootdir}/ui/preset_row.ui")
class GradiencePresetRow(Adw.ActionRow):
    __gtype_name__ = "GradiencePresetRow"

    name_entry = Gtk.Template.Child("name_entry")
    value_stack = Gtk.Template.Child("value_stack")
    name_entry_toggle = Gtk.Template.Child("name_entry_toggle")
    apply_button = Gtk.Template.Child("apply_button")
    remove_button = Gtk.Template.Child("remove_button")

    def __init__(self, name, win, author="", **kwargs):
        super().__init__(**kwargs)

        self.name = name
        self.old_name = name

        self.set_name(name)
        self.set_title(name)
        self.set_subtitle(author)
        self.name_entry.set_text(name)

        self.app = Gtk.Application.get_default()
        self.win = win
        self.toast_overlay = self.win.toast_overlay

        apply_button = Gtk.Template.Child("apply_button")
        rename_button = Gtk.Template.Child("rename_button")

    @Gtk.Template.Callback()
    def on_apply_button_clicked(self, *_args):
        buglog("apply")

        self.app.load_preset_from_file(os.path.join(
            os.environ.get("XDG_CONFIG_HOME",
                           os.environ["HOME"] + "/.config"),
            "presets",
            to_slug_case(self.name) + ".json",
        ))

    @Gtk.Template.Callback()
    def on_name_entry_changed(self, *_args):
        self.name = self.name_entry.get_text()
        self.set_name(self.name)
        self.set_title(self.name)

    @Gtk.Template.Callback()
    def on_name_entry_toggled(self, *_args):
        if self.name_entry_toggle.get_active():
            self.value_stack.set_visible_child(self.name_entry)
        else:
            self.update_value()
            self.value_stack.set_visible_child(self.apply_button)

    @Gtk.Template.Callback()
    def on_remove_button_clicked(self, *_args):
        self.toast_overlay.add_toast(
            self.win.delete_toast
        )

        self.win.old_name = self.name

        self.win.reload_pref_group()

    def update_value(self):
        os.remove(os.path.join(
            os.environ.get("XDG_CONFIG_HOME",
                           os.environ["HOME"] + "/.config"),
            "presets",
            to_slug_case(self.old_name) + ".json",
        ))
        with open(
            os.path.join(
                os.environ.get("XDG_CONFIG_HOME",
                               os.environ["HOME"] + "/.config"),
                "presets",
                to_slug_case(self.name) + ".json",
            ),
            "w",
            encoding="utf-8",
        ) as file:
            object_to_write = {
                "name": self.name,
                "variables": self.app.variables,
                "palette": self.app.palette,
                "custom_css": self.app.custom_css,
            }
            file.write(json.dumps(object_to_write, indent=4))
            self.app.clear_dirty()
            self.toast_overlay.add_toast(
                Adw.Toast(title=_("Preset renamed"))
            )
        self.old_name = self.name
