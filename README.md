easygames — Página temporária

Este repositório contém uma página "em construção" para o domínio easygames.co.mz.
O arquivo CNAME já foi adicionado com o domínio: easygames.co.mz

Publicar no GitHub Pages (passos rápidos)

1) Inicializar o repositório local (se ainda não existir) e enviar para o GitHub
   - Substitua USERNAME e REPO pelo seu usuário e nome do repositório.

   No PowerShell:
   git init; git add .; git commit -m "Site em construção"; git branch -M main; git remote add origin https://github.com/USERNAME/REPO.git; git push -u origin main

   Ou, se preferir usar a GitHub CLI (recomendado se ainda não criou o repositório):
   gh repo create USERNAME/REPO --public --source=. --remote=origin --push

2) Ativar o GitHub Pages
   - Vá a https://github.com/USERNAME/REPO/settings/pages
   - Em "Source" selecione a rama "main" e o diretório "/ (root)" e salve.
   - O site estará disponível em https://easygames.co.mz (ou no subdomínio github.io enquanto o DNS não propagar).

Observações
- O arquivo `CNAME` já está presente com o domínio `easygames.co.mz`.
- Se usar GitHub Actions ou workflows para deploy automático, não é necessário fazer mais nada além de push para a rama configurada.
- Se o GitHub Pages não refletir as alterações, aguarde alguns minutos e limpe o cache do navegador.

Se quiser, eu posso:
- Criar um workflow GitHub Actions para deploy automático; ou
- Atualizar o README com instruções específicas para o seu repositório.
