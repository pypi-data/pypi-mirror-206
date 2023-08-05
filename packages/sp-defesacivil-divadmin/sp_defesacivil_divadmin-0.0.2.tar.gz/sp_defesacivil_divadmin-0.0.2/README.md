# Defesa Civil do Estado de São Paulo

<img align="right" src="./docs/imgs/logo_defesacivil.png?raw=true" width="120" height="100%" />

_Script_ que atualiza a divisão administrativa das Coordenadorias Regionais de Proteção e Defesa Civil - REPDEC da Defesa Civil do Estado de São Paulo, gerando uma tabela em _csv_ com a indicação dos 645 munícipios paulistas a partir dos mapas obtidos no [_site_ da instituição](http://www.defesacivil.sp.gov.br/coordenadores-regionais-de-defesa-civil/).

> **Data de Atualização**: 01.05.2023

<br>

---

## Geo

Inicialmente eu não tinha material de referência. O _site_ da Defesa Civil não apresentava informações etc. Dai usei uma monografia, em PDF, para pegar os limites administrativos das REPDECs.

![Defesa Civil](https://github.com/michelmetran/sp_defesacivil/blob/main/data/rasters/geo_defesacivil.jpg?raw=true)

<br>

Em abril de 2023 acessei o _site_ da Defesa Civil e vi que é apresentado um [Mapa das Regionais de Defesa Civil](http://www.defesacivil.sp.gov.br/mapa-das-regionais-de-defesa-civil/). Olhando o código da página, notei que há um redireciomaneto para a um _leaflet_ da [Casa Militar](http://datageo.casamilitar.sp.gov.br/grd/embedded.html#/375)

- [Geonetwork da Casa Militar](http://datageo.casamilitar.sp.gov.br/geonetworkgrd/srv/por/catalog.search#/metadata/%7B70951E2A-E0C2-470F-BE8E-126DE4A3BF74%7D)
- [Geoserver do Datageo](http://datageo.ambiente.sp.gov.br/geoserver/datageo/RegionaisdaDefesaCivil/wfs?version=1.0.0&request=GetFeature&outputFormat=SHAPE-ZIP&typeName=RegionaisdaDefesaCivil)

<br>

---

## _TODO_

- Outros dados que poderão ser explorados no futuro estão em: https://s2id.mi.gov.br/paginas/series/
