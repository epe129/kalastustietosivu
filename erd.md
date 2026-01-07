```mermaid
---
title:  Kalastustieto sivu database
config:
    layout: elk
---
erDiagram
    KALASTAJA {
        int id PK
        string name
    } 

    TARPPI {
        int id PK
        datetime aika
        int kalastaja_id
        int viehe_id
        int vapa_id
        string paikka
    }
    
    KALA {
        int id PK
        int tarppi_id
        float pituus
        float paino
        string laji
    }

    VIEHE {
        int id PK
        string viehe
    }

    VAPA {
        int id PK
        string vapa
    }
    


    KALASTAJA ||--o{ TARPPI: saa
    VIEHE ||--o{ TARPPI: liittyy
    VAPA ||--o{ TARPPI: liittyy
    KALA ||--|| TARPPI: saa