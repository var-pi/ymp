{
    description = "Music CLI.";

    inputs = {
        nixpkgs.url = "github:NixOS/nixpkgs";
    };

    outputs = { self, nixpkgs }:
        let
            system = "aarch64-darwin"; # change if needed
            pkgs = import nixpkgs { inherit system; };
            pythonEnv = pkgs.python3.withPackages (ps: with ps; [ typer pip ]);
        in {
            packages.${system}.default =
                pkgs.stdenv.mkDerivation {
                    pname = "ymp";
                    version = "0.1";

                    src = ./.;

                    nativeBuildInputs = [ pkgs.makeWrapper ];

                    buildInputs = [
                        pythonEnv
                        pkgs.fzf
                        pkgs.ffmpeg
                        pkgs.yt-dlp
                    ];

                    installPhase = ''
                    mkdir -p $out/bin
                    cp $src/ymp.py $out/bin/ymp
                    chmod +x $out/bin/ymp

                    wrapProgram $out/bin/ymp \
                        --prefix PATH : ${pkgs.lib.makeBinPath [
                            pythonEnv
                            pkgs.fzf
                            pkgs.ffmpeg
                            pkgs.yt-dlp
                        ]}
                    '';
                };
        };
}
