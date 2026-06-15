#!/usr/bin/env bash
# setup.sh — Configura o ambiente Nix, VNC e força o download das dependências

echo "1/4 Limpando scripts antigos (removendo run.sh)..."
rm -f run.sh

echo "2/4 Configurando o ambiente Nix (replit.nix)..."
cat > replit.nix << 'EOF'
{ pkgs }: {
  deps = [
    pkgs.python311
    pkgs.python311Packages.tkinter
    pkgs.xorg.libX11
    pkgs.xorg.libXext
  ];
}
EOF

echo "🖥️ 3/4 Configurando o Workflow e VNC nativo (.replit)..."
cat > .replit << 'EOF'
run = "python3 main.py"

[nix]
channel = "stable-23_11"

[env]
DISPLAY = ":0"

[vnc]
env = { DISPLAY = ":1" }
command = ["python3", "main.py"]
EOF

echo "4/4 Arquivos criados com sucesso!"
echo "---------------------------------------------------"
echo " ATENÇÃO: O container será reiniciado AGORA."
echo "Sua conexão neste terminal vai cair por cerca de 2 segundos."
echo "Assim que a tela piscar, o Replit começará a baixar os pacotes."
echo "Quando o download terminar, basta clicar no botão verde RUN."
echo "---------------------------------------------------"

# Pausa de 3 segundos para você ler a mensagem
sleep 3

# Força o reboot do container para o Nix ler os novos arquivos e baixar as bibliotecas
kill 1