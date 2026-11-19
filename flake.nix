# ffp: FFP-NIX-FLAKE declarative nix
{
  description = "Build-Law v1.4.0 — Build Law Deterministic 14-Gate AI Engineering Verifier, Multi-Tool Provisioner & MCP Server";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-25.05";
  };

  outputs = { self, nixpkgs, ... }:
    let
      supportedSystems = [ "x86_64-linux" "aarch64-linux" ];
      forAllSystems = nixpkgs.lib.genAttrs supportedSystems;
      artifactMeta = {
        "x86_64-linux" = {
          url = "https://github.com/Tianxia-Core/Build-Law/releases/download/v1.4.0/build-law-v1.4.0-linux-x86_64";
          sha256 = "142b0bb5f081403d9683780f0634a45e74c5887154b97e57219f8b60e8101415";
        };
        "aarch64-linux" = {
          url = "https://github.com/Tianxia-Core/Build-Law/releases/download/v1.4.0/build-law-v1.4.0-linux-aarch64";
          sha256 = "46813327bbcabfdf910625d4e358a5ec85ccb59d3fed255ae54d59d72aed78a9";
        };
      };
      mkSovereignPkg = pkgs: system:
        let
          metaInfo = artifactMeta.${system};
        in
        pkgs.stdenvNoCC.mkDerivation {
          pname = "build-law";
          version = "1.4.0";
          src = pkgs.fetchurl {
            inherit (metaInfo) url sha256;
          };
          dontUnpack = true;
          installPhase = ''
            runHook preInstall
            mkdir -p $out/bin
            install -m 0755 $src $out/bin/build-law
            runHook postInstall
          '';
          meta = with pkgs.lib; {
            description = "Build Law Deterministic 14-Gate AI Engineering Verifier, Multi-Tool Provisioner & MCP Server";
            homepage = "https://rasaxmachina.com";
            platforms = supportedSystems;
            mainProgram = "build-law";
          };
        };
    in {
      packages = forAllSystems (system:
        let
          pkgs = import nixpkgs { inherit system; };
          pkg = mkSovereignPkg pkgs system;
        in {
          default = pkg;
          "build-law" = pkg;
        }
      );

      apps = forAllSystems (system: {
        default = {
          type = "app";
          program = "${self.packages.${system}.default}/bin/build-law";
        };
      });

      overlays.default = final: prev: {
        "build-law" = mkSovereignPkg final final.stdenv.hostPlatform.system;
      };

      nixosModules.buildlaw = { config, lib, pkgs, ... }:
        let
          cfg = config.services.buildlaw;
        in {
          options.services.buildlaw = {
            enable = lib.mkEnableOption "Build-Law Sovereign Service";
            package = lib.mkOption {
              type = lib.types.package;
              default = self.packages.${pkgs.stdenv.hostPlatform.system}.default;
              description = "Package providing build-law.";
            };
          };
          config = lib.mkIf cfg.enable {
            environment.systemPackages = [ cfg.package ];
          };
        };
    };
}
