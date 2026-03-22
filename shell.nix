{ pkgs ? import <nixpkgs> {} }:
pkgs.mkShell {
  buildInputs = [
    (pkgs.python311.withPackages (ps: with ps; [
      pyside6
      opencv-python
    ]))
  ];
  
  shellHook = ''
  '';
}
