# Station qualité d'air — ESPHome

Station de mesure de la qualité de l'air sur ESP32, affichage e-paper autonome (fonctionne sans Home Assistant).

## Matériel
- **ESP32** (esp32dev)
- **SCD30** — CO2, humidité (I2C bus_a, 0x61)
- **SGP41** — indice COV / NOx (I2C bus_a, 0x59)
- **MS5611** — pression, température (I2C bus_a, 0x77)
- **SPS30** — particules fines PM1/2.5/4/10 (I2C bus_b, 0x69 — **seul sur son bus**, il perturbe le bus partagé ; alim **5V**, broche SEL→GND)
- **WeAct Studio 4.2" e-paper 3 couleurs** (400x300, SSD1683) en SPI

## Câblage
| Fonction | GPIO |
|---|---|
| I2C bus_a SDA / SCL | 21 / 22 |
| I2C bus_b SDA / SCL (SPS30) | 32 / 33 |
| e-paper CLK / MOSI | 18 / 23 |
| e-paper CS / DC / RST / BUSY | 5 / 19 / 15 / 4 |
| GPIO2 | inutilisé (LED bleue forcée éteinte) |

## Affichage
Grille 2×4 = 8 mini-graphes (30 min d'historique) : CO2, Temp, Hum, Press, COV, NOx, PM2.5, PM10.
Courbes rouges, texte noir qui passe en rouge quand un seuil est dépassé, + flèches de tendance.

## Composant custom
`components/epaper_spi/` est une copie modifiée du composant ESPHome qui ajoute un **fast refresh** (~10 s au lieu de ~20 s) pour le panneau WeAct 3C (astuce de température façon GxEPD2).

## Secrets
Les identifiants ne sont **pas** dans le dépôt. Crée un fichier `secrets.yaml` à la racine :

```yaml
wifi_ssid: "TonWiFi"
wifi_password: "TonMotDePasse"
ap_password: "MotDePasseHotspot"
api_key: "CleApiHomeAssistant"
```

## Compilation / flash
```bash
esphome run livingroom.yaml
```
