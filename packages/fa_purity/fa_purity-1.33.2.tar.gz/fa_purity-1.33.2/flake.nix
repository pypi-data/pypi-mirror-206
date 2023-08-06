{
  description = "Pure functional and typing utilities";
  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs";
    nix_filter.url = "github:numtide/nix-filter";
  };
  outputs = {
    self,
    nixpkgs,
    nix_filter,
  }: let
    metadata = (builtins.fromTOML (builtins.readFile ./pyproject.toml)).project;
    path_filter = nix_filter.outputs.lib;
    src = path_filter {
      root = self;
      include = [
        "mypy.ini"
        "arch.cfg"
        "arch_test.cfg"
        "pyproject.toml"
        (path_filter.inDirectory metadata.name)
        (path_filter.inDirectory "tests")
      ];
    };
    out = system:
      import ./build {
        inherit src;
        nixpkgs = nixpkgs.legacyPackages."${system}";
      };
    systems = [
      "aarch64-darwin"
      "aarch64-linux"
      "x86_64-darwin"
      "x86_64-linux"
    ];
    forAllSystems = nixpkgs.lib.genAttrs systems;
  in {
    packages = forAllSystems out;
    defaultPackage = self.packages;
  };
}
