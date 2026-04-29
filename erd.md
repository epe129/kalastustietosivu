```mermaid
---
title:  Kalastus ER-kaavio
config:
    layout: elk
---
erDiagram
    direction RL
    TARPPI {
        int id PK
        datetime aika
        int kalastaja_id
        int viehe_id
        int vapa_id
        string paikka
    }
    KALASTAJA ||--o{ TARPPI: saa
    KALASTAJA {
        int id PK
        string nimi
    } 
    VIEHE ||--o{ TARPPI: liittyy
    VIEHE {
        int id PK
        string viehe
    }
    VAPA ||--o{ TARPPI: liittyy
    KALA ||--|| TARPPI: saa
    LAJI ||--o{ KALA: liittyy

    
    
    
    KALA {
        int id PK
        int tarppi_id
        float pituus
        float paino
        int laji_id
    }

   

    VAPA {
        int id PK
        string vapa
    }
    
    LAJI {
        int id PK
        string laji
    }