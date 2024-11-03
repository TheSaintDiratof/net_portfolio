{ pkgs ? import <nixpkgs> {}, pythonPackages ? pkgs.python3Packages }:

pkgs.mkShell {
  buildInputs = [
    pythonPackages.jupyterlab pkgs.nodejs
    pythonPackages.notebook
    pythonPackages.scapy
    pythonPackages.cryptography
    pythonPackages.grpcio-tools
    pkgs.tcpdump
  ];

  shellHook = ''
    TEMPDIR=$PWD/tmp
    mkdir -p $TEMPDIR
    cp -r ${pythonPackages.jupyterlab}/share/jupyter/lab/* $TEMPDIR
    chmod -R 755 $TEMPDIR
    echo "$TEMPDIR is the app directory"

    #jupyter lab build --app-dir=$TEMPDIR
    
    # start jupyterlab
    #jupyter lab --app-dir=$TEMPDIR
  '';

}

