{ pkgs ? import <nixpkgs> {} }:

let
    pythonEnv = pkgs.python3.withPackages (ps: with ps; [ typer ]);
in
    pkgs.mkShell {
        buildInputs = [
            pythonEnv.python
        ];

        shellHook = ''
          export PATH=${pythonEnv}/bin:$PATH
          export PYTHONPATH=${pythonEnv}/lib/python3.13/site-packages
          export PYTHONNOUSERSITE=1
        '';
    }
