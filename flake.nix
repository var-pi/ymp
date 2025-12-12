{
  description = "Music CLI";

  inputs.nixpkgs.url = "github:NixOS/nixpkgs";

  outputs = { nixpkgs, ... }: let
    pkgs = import nixpkgs { system = "aarch64-darwin"; };
  in {
    packages.x86_64-darwin.music-cli = pkgs.stdenv.mkDerivation {
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
        platforms = pkgs.platforms.unix;
      };
    };
  };
}
