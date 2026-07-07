# Site do TCC — Diagnóstico do risco

Site estático do Trabalho de Conclusão de Licenciatura de **Rodrigo Antonio Devellis**
(Ciências Sociais, UFSC, 2026): *"Diagnóstico do risco: o paciente parcial e a
expansão do acesso à PrEP no Brasil"*. Traz os mapas visuais e as sínteses da
introdução, dos cinco capítulos e da conclusão.

## Estrutura

| Caminho | O que é |
|---|---|
| `site_tcc/index.html` | O site — arquivo único, autossuficiente (mapas SVG embutidos inline) |
| `flask_app.py` | App WSGI mínimo que serve o site (usado no PythonAnywhere) |
| `requirements.txt` | Dependência (Flask) |
| `*_mapa.svg` | Mapas visuais em SVG (fontes; já embutidos no `index.html`) |
| `tcc_schema.json` / `tcc_exemplo.json` | Esquema JSON do TCC e exemplo preenchido |
| `TCL FORMATADO - RODRIGO (4).pdf` | Versão final do trabalho |

## Rodar localmente

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python flask_app.py
# abra http://localhost:5000
```

> O `index.html` também abre direto no navegador (duplo clique) — o Flask só é
> necessário para o deploy no PythonAnywhere.

## Deploy no PythonAnywhere (plano gratuito)

Substitua `SEU_USUARIO` pelo seu usuário do PythonAnywhere em todos os passos.

1. **Clonar o repositório.** No painel: *Consoles → Bash*. No console:
   ```bash
   git clone https://github.com/antoniodevellisneto991-collab/site-tcc-rodrigo.git
   ```
2. **Criar o web app.** *Web → Add a new web app* → domínio `SEU_USUARIO.pythonanywhere.com`
   → framework **Flask** → versão de Python mais recente disponível → aceite o caminho padrão.
3. **Apontar para este projeto.** Ainda na aba *Web*, edite o **WSGI configuration file**
   e substitua todo o conteúdo por:
   ```python
   import sys
   path = "/home/SEU_USUARIO/site-tcc-rodrigo"
   if path not in sys.path:
       sys.path.insert(0, path)
   from flask_app import app as application
   ```
4. **Reload.** Clique no botão verde **Reload** no topo da aba *Web*.
5. Acesse `https://SEU_USUARIO.pythonanywhere.com` — o site estará no ar.

### Atualizar o site depois

```bash
cd site-tcc-rodrigo && git pull
```
Depois clique em **Reload** na aba *Web*.
