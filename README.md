# Danahe's Magical Crafts - DevOps

Proyecto Flask desplegado con Docker, GitHub Actions, GitHub Container Registry y Traefik.

## Datos del proyecto

- Repositorio sugerido: `danahe-magical-crafts-devops`
- Package / imagen GHCR: `danahe-magical-crafts`
- Imagen completa: `ghcr.io/larissaguaman1/danahe-magical-crafts:1.0.0`
- Subdominio: `larissa.byronrm.com`
- Stack: `danahecrafts`

## Ejecutar localmente

```bash
docker compose up -d --build
```

Abrir:

```txt
http://localhost:5000
```

## Detener localmente

```bash
docker compose down
```

## Subir a GitHub

```bash
git init
git add .
git commit -m "Proyecto DevOps Danahe Magical Crafts"
git branch -M main
git remote add origin https://github.com/larissaguaman1/danahe-magical-crafts-devops.git
git push -u origin main
```

## Secrets necesarios en GitHub

En el repositorio, ir a Settings > Secrets and variables > Actions y agregar:

```txt
GHCR_TOKEN
VPS_HOST
VPS_USER
VPS_PASSWORD
VPS_PORT
```

## Verificar el package con descarga

Cuando GitHub Actions haga `docker push`, se crea el package en GHCR.
Cuando el VPS ejecute `docker pull ghcr.io/larissaguaman1/danahe-magical-crafts:1.0.0`, el package debe reflejar al menos una descarga.

## Comandos útiles en el VPS

```bash
docker service ls
docker service logs danahecrafts_danahecrafts -f
docker pull ghcr.io/larissaguaman1/danahe-magical-crafts:1.0.0
```
