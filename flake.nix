{
  description = "Music CLI";

  inputs.nixpkgs.url = "github:NixOS/nixpkgs";

  outputs = { nixpkgs, ... }: let
    system = "aarch64-darwin"; #Only for Apple Silicon
    pkgs = import nixpkgs { inherit system; };
  in {
    packages.${system}.default = pkgs.stdenv.mkDerivation {
      pname = "music-cli";
      version = "0.1";

      src = ./.;
      nativeBuildInputs = [ pkgs.makeWrapper pkgs.zsh ];

      installPhase = ''
        mkdir -p $out/bin
        cp bin/* $out/bin/
      '';

      meta = with pkgs.lib; {
        description = "CLI for music downloading and playback";
        license = licenses.mit;
        #platforms = pkgs.platforms.unix;
      };
    };
  };
}
