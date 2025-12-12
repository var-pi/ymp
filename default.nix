{ pkgs }:
pkgs.stdenv.mkDerivation {
  pname = "my-music-cli";
  version = "0.1";

  src = ./.;

  nativeBuildInputs = with pkgs; [ makeWrapper zsh ];

  installPhase = ''
    mkdir -p $out/bin
    cp bin/* $out/bin/
  '';

  meta = with pkgs.lib; {
    description = "Simple CLI for music downloading and playback";
    license = licenses.mit;
    platforms = platforms.unix;
  };
}
