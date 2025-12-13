{
    description = "Music CLI.";

    inputs = {
        nixpkgs.url = "github:NixOS/nixpkgs";
    };

    outputs = { self, nixpkgs }:
        let
            system = "aarch64-darwin";
            pkgs = import nixpkgs { inherit system; };
        in {
            packages.${system}.default =
                pkgs.python3Packages.buildPythonApplication {
                    pname = "ymp";
                    version = "0.1";
                    src = ./.;

                    pyproject = true;
                    build-system = [ pkgs.python3Packages.setuptools ];
                    propagatedBuildInputs = [ 
                        pkgs.python3Packages.typer
                        pkgs.fzf
                        pkgs.ffmpeg
                        pkgs.yt-dlp
                    ];

                    extraWrapperArgs = [
                        "--prefix" "PATH" ":" "${pkgs.lib.makeBinPath [ pkgs.fzf pkgs.ffmpeg pkgs.yt-dlp ]}"
                    ];
                };
        };
}
