pkgname = "dash"
version = "0.5.11.3"
revision = 0
build_style = "gnu_configure"
pkgdesc = "POSIX-compliant Unix shell, much smaller than GNU bash"
maintainer="q66 <daniel@octaforge.org>"
license="BSD-3-Clause"
homepage="http://gondor.apana.org.au/~herbert/dash"
sources = [f"http://gondor.apana.org.au/~herbert/dash/files/{pkgname}-{version}.tar.gz"]
sha256 = ["62b9f1676ba6a7e8eaec541a39ea037b325253240d1f378c72360baa1cbcbc2a"]

options = ["bootstrap", "!check"]

def post_install(self):
    self.install_license("COPYING")
    self.install_link("dash", "usr/bin/sh")
