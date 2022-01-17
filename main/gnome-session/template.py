pkgname = "gnome-session"
pkgver = "41.3"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-Dsystemd_journal=false", "-Dsystemd_session=disable"
]
hostmakedepends = [
    "meson", "pkgconf", "glib-devel", "xmlto", "gettext-tiny",
]
makedepends = [
    "libglib-devel", "gtk+3-devel", "elogind-devel", "gnome-desktop-devel",
    "json-glib-devel", "libice-devel", "libsm-devel", "libx11-devel", "xtrans"
]
pkgdesc = "GNOME session management utilities"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://gitlab.gnome.org/GNOME/gnome-session"
source = f"$(GNOME_SITE)/{pkgname}/{pkgver[:-2]}/{pkgname}-{pkgver}.tar.xz"
sha256 = "ee4a229053f522624054889609335b885287cf67bbde0dc9fd882b01ec9b5b39"
