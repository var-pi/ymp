{
    description = "Music CLI.";

    inputs = {
        nixpkgs.url = "github:NixOS/nixpkgs";
    };

    outputs = { self, nixpkgs }:
        let
            system = "aarch64-darwin"; # change if needed
            pkgs = import nixpkgs { inherit system; };
        in {
            packages.${system}.default =
                pkgs.stdenv.mkDerivation {
                    pname = "ymp";
                    version = "0.1";

                    src = ./.;

                    nativeBuildInputs = [ pkgs.makeWrapper ];

                    buildInputs = [
                        (pkgs.python3.withPackages (ps: with ps; [ typer ]))
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
                            pkgs.fzf
                            pkgs.ffmpeg
                            pkgs.yt-dlp
                        ]}
                    '';
                };

            devShells.${system}.default = pkgs.mkShell {
                packages = [
                    # Your runtime dependencies
                    self.packages.${system}.default  # include your wrapped script itself
                ];
            };
        };
}
