<img align="left" alt="Icon" src="https://github.com/GradienceTeam/Gradience/blob/main/data/icons/hicolor/scalable/apps/com.github.GradienceTeam.Gradience.svg">

# Gradience

Change the look of Adwaita, with ease

![Screenshot of interface with Adwaita light theme](https://github.com/GradienceTeam/Design/blob/main/Screenshots/main_screenshot.png)

Gradience is a tool for customizing Libadwaita applications and the adw-gtk3 theme.

<details>
  <summary>More screenshots</summary>
  
  ![Screenshot of interface of Monet Tab](https://github.com/GradienceTeam/Design/blob/main/Screenshots/monet_purple.png)
  
  ![Screenshot of proof that this actually works](https://github.com/GradienceTeam/Design/blob/main/Screenshots/proof_of_work_screenshot.png)
</details>

[![Build flatpak](https://github.com/GradienceTeam/Gradience/actions/workflows/flatpak.yml/badge.svg)](https://github.com/GradienceTeam/Gradience/actions/workflows/flatpak.yml)
[![Build flatpak nightly](https://github.com/GradienceTeam/Gradience/actions/workflows/flatpak-nightly.yml/badge.svg)](https://github.com/GradienceTeam/Gradience/actions/workflows/flatpak-nightly.yml)
[![Copr build status](https://img.shields.io/badge/dynamic/json?color=blue&label=copr&query=builds.latest.state&url=https%3A%2F%2Fcopr.fedorainfracloud.org%2Fapi_3%2Fpackage%3Fownername%3Dlyessaadi%26projectname%3Dgradience%26packagename%3Dgradience%26with_latest_build%3DTrue)](https://copr.fedorainfracloud.org/coprs/lyessaadi/gradience/package/gradience/)
[![Translate on Weblate](https://hosted.weblate.org/widgets/GradienceTeam/-/svg-badge.svg)](https://hosted.weblate.org/engage/GradienceTeam)
[![Chat on Matrix](https://matrix.to/img/matrix-badge.svg)](https://matrix.to/#/#Gradience:matrix.org)
[![Chat on Discord](https://img.shields.io/discord/1013779899821064202)](https://discord.com/invite/rwNDGPJf)

## Download

Gradience is available on Flathub.

<a href="https://flathub.org/apps/details/com.github.GradienceTeam.Gradience">
    <img width="200" alt="Download on Flathub" src="https://flathub.org/assets/badges/flathub-badge-i-en.svg"/>
</a>

## Building and Installing

### Requirements

- Python 3 `python`
- PyGObject `python-gobject`
- Blueprint [`blueprint-compiler`](https://jwestman.pages.gitlab.gnome.org/blueprint-compiler/setup.html)
- GTK4 `gtk4`
- libadwaita (>= 1.2.alpha) `libadwaita`
- Meson `meson`
- Ninja `ninja`

### Building from source

Install required Python libraries:

```sh
pip install -r requirements.txt
```

### Global installation

```sh
git clone https://github.com/GradienceTeam/Gradience.git
cd Gradience
meson builddir --prefix=/usr/local
sudo ninja -C builddir install
```

### Local build (for testing and development purposes)

```sh
git clone https://github.com/GradienceTeam/Gradience.git
cd Gradience
meson builddir
meson configure builddir -Dprefix="$(pwd)/builddir/testdir"
ninja -C builddir install
ninja -C builddir run
```

**[NOTE]** During testing and developement, as a convenience, you can use the `local.sh` script to quickly rebuild local builds.

### Building using flatpak-builder

1. Open Terminal
2. Run `git clone https://github.com/GradienceTeam/Gradience.git && cd Gradience`
3. Install the `42` version of GNOME SDK: `flatpak install org.gnome.Sdk/x86_64/42 org.gnome.Platform/x86_64/42`
4. Run: `flatpak-builder --install --user --force-clean repo/ build-aux/flatpak/com.github.GradienceTeam.Gradience.Devel.json`

Alternatively, open the project with GNOME Builder, then build and run it.

## Setup Tutorial

### Libadwaita applications

No additional setup is required for native Libadwaita applications.

For Flatpak Libadwaita applications, you need to override their permissions:

- Run `sudo flatpak override --filesystem=xdg-config/gtk-4.0` or
- Use [Flatseal](https://github.com/tchx84/Flatseal) and adding `xdg-config/gtk-4.0` to **Other files** in the **Filesystem** section of **All Applications**

### Vanilla GTK 4 applications

Use [this guide](https://github.com/lassekongo83/adw-gtk3/blob/main/gtk4.md) to theme vanilla GTK 4 applications.

### GTK 3 applications

- Install and apply the [adw-gtk3](https://github.com/lassekongo83/adw-gtk3#readme) theme (don't forget to install the Flatpak package!)
- For Flatpak applications, you need to override their permissions:
  - Run `sudo flatpak override --filesystem=xdg-config/gtk-3.0` or
  - Use [Flatseal](https://github.com/tchx84/Flatseal) and adding `xdg-config/gtk-3.0` to **Other files** in the **Filesystem** section of **All Applications**

## Roadmap

This tool is currently WIP, but it already has a plenty of features and is very usable. Below is the roadmap, where all the checked features are already implemented:

<details><summary>Show roadmap</summary>

### <!-- GapTool Turbo 3000 -->

- [x] Customize named colors, either with a color picker or with text
- [x] Explanations for some named colors
- [x] Partial theme preview
- [x] Built-in presets for Adwaita and Adwaita Dark (based on default libadwaita colors)
- [x] Apply changes to libadwaita, GTK4 (with extracted libadwaita theme) and GTK3 (with the adw-gtk3 theme) applications
- [x] Load and create custom presets
- [x] View adw-gtk3's support of variables
- [x] View parsing errors
- [x] Customize palette colors
- [x] Add custom CSS code
- [x] Localization support
- [x] Normalize color variables
- [x] Make the code more secure
- [x] Add preset manager with option to download other users presets
- [x] Release on Flathub
- [ ] Add plugin support. Will help integration with others tools. (WIP)
- [ ] Full theme preview
- [ ] Customize GNOME Shell
- [ ] Customize GDM
- [ ] Customize KvLibadwaita
- [ ] Customize Firefox GNOME theme

</details>

## Contribute

See [`CONTRIBUTING.md`](CONTRIBUTING.md) for more informations and a list of contributors

## About Name

Gradience was originally named Adwaita Manager.

You can see the meaning of Gradience on [Wiktionary](https://en.wiktionary.org/wiki/gradience).

The icon represents: _A Paint Roller repainting an Adwaita window, keeping it's functionality and improving it's looks_
