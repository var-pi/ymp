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
                    pname = "ym";
                    version = "0.1";

                    src = ./.;

                    nativeBuildInputs = [ pkgs.makeWrapper ];

                    buildInputs = [
                        pkgs.python3
                        pkgs.fzf
                        pkgs.ffmpeg
                        pkgs.yt-dlp
                    ];

                    installPhase = ''
                    mkdir -p $out/bin
                    cp $src/ym.py $out/bin/ym
                    chmod +x $out/bin/ym

                     wrapProgram $out/bin/ym \
                          --prefix PATH : ${pkgs.lib.makeBinPath [
                            pkgs.python3
                            pkgs.fzf
                            pkgs.ffmpeg
                            pkgs.yt-dlp
                        ]}
                    '';
                };
        };
}
