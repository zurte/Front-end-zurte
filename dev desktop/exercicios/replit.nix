{ pkgs }: {
  deps = [
    pkgs.python311
    pkgs.python311Packages.tkinter
    pkgs.xorg.libX11
    pkgs.xorg.libXext
  ];
}
