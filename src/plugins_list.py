# plugins_list.py
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

import sys
import os
import importlib
import pkgutil

from gi.repository import Gtk, Adw, Gio, Gdk
import pluggy

from pathlib import Path
from .modules.utils import buglog
from .plugin_row import GradiencePluginRow
from plugins.hookspec import GradienceHooks


class GradiencePluginsList:
    def __init__(self, win):

        self.win = win

        self.plugins = win.settings.get_list("plugins-enabled")
        buglog(self.plugins)

        self.pm = pluggy.PluginManager("gradience")
        self.pm.add_hookspecs(GradienceHooks)

    def load_all_custom_settings(self, settings):
        for plugin_id, plugin in self.plugins.items():
            plugin.load_custom_settings(settings)

    def get_all_custom_settings_for_preset(self):
        custom_settings = {}
        for plugin_id, plugin in self.plugins.items():
            custom_settings[plugin_id] = plugin.get_custom_settings_for_preset()

    def to_group(self):
        group = Adw.PreferencesGroup()
        group.set_title(_("Plugins"))
        group.set_description(
            _("Plugins add additional features to Gradience, plugins are made by Gradience community and can make issues."))
        if self.plugins:
            for plugin_id, plugin in self.plugins.items():
                row = GradiencePluginRow(plugin.title, plugin_id)
                self.rows[plugin_id] = row
                group.add(row)
        else:
            row = Adw.ActionRow()
            row.set_title(_("No plugins found"))
            group.add(row)
        return group
