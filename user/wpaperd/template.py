pkgname = "wpaperd"
pkgver = "1.0.1"
pkgrel = 1
build_style = "cargo"
hostmakedepends = [
    "cargo-auditable",
    "pkgconf",
    "scdoc",
]
makedepends = ["mesa-devel", "rust-std", "wayland-devel"]
pkgdesc = "Wallpaper daemon for Wayland"
maintainer = "tulilirockz <tulilirockz@outlook.com>"
license = "GPL-3.0-or-later"
url = "https://github.com/danyspin97/wpaperd"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "4ed30c90dc14fa629ac977ace3ca4a146a33d85f73d2d49915643fbb9ea53ab9"
# check: no meaningful tests
options = ["!check"]


def post_build(self):
    with open(f"{self.cwd}/man/wpaperd-output.5.scd", "rb") as i:
        with open(f"{self.cwd}/wpaperd-output.5", "w") as o:
            self.do("scdoc", input=i.read(), stdout=o)


def install(self):
    self.install_bin(f"target/{self.profile().triplet}/release/wpaperd")
    self.install_bin(f"target/{self.profile().triplet}/release/wpaperctl")
    self.install_completion(f"target/{self.profile().triplet}/release/completions/wpaperd.bash", "bash")
    self.install_completion(f"target/{self.profile().triplet}/release/completions/wpaperctl.bash", "bash")
    self.install_completion(f"target/{self.profile().triplet}/release/completions/wpaperd.zsh", "zsh")
    self.install_completion(f"target/{self.profile().triplet}/release/completions/wpaperctl.zsh", "zsh")
    self.install_completion(f"target/{self.profile().triplet}/release/completions/wpaperd.elv", "evilsh")
    self.install_completion(f"target/{self.profile().triplet}/release/completions/wpaperctl.elv", "evilsh")
    self.install_completion(f"target/{self.profile().triplet}/release/completions/wpaperd.fish", "fish")
    self.install_completion(f"target/{self.profile().triplet}/release/completions/wpaperctl.fish", "fish")
    self.install_completion(f"target/{self.profile().triplet}/release/completions/_wpaperd.ps1", "pwsh")
    self.install_completion(f"target/{self.profile().triplet}/release/completions/_wpaperctl.ps1", "pwsh")
    self.install_license("LICENSE.md")
    self.install_man("wpaperd-output.5")
