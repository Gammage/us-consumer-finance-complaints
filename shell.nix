let
  pkgs = (builtins.getFlake "/home/ben/nixos").inputs.nixpkgs.legacyPackages.${builtins.currentSystem};
in
pkgs.mkShell {
  packages = with pkgs; [
    (python3.withPackages (ps: with ps; [
      jupyterlab
      jupytext
      ipykernel
      numpy
      pandas
      matplotlib
      plotly
    ]))
  ];
}
