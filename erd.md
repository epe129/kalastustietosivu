```mermaid
---
title:  Kalastustieto sivu database
config:
    layout: elk
---
erDiagram
    KALASTAJA {
        int id PK
        string nimi
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
        int laji_id
    }

    VIEHE {
        int id PK
        string viehe
    }

    VAPA {
        int id PK
        string vapa
    }
    
    LAJI {
        int id PK
        string laji
    }


    KALASTAJA ||--o{ TARPPI: saa
    VIEHE ||--o{ TARPPI: liittyy
    VAPA ||--o{ TARPPI: liittyy
    KALA ||--|| TARPPI: saa
    LAJI ||--o{ KALA: liittyy