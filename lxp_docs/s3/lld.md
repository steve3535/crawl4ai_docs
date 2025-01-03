```mermaid
flowchart TD
    %% Client Layer Details
    subgraph Clients["Client Components"]
        direction TB
        C1[s3cmd]
        C2[aws cli]
        C3[CyberDuck]
        C4[Python Boto3]
        C5[Custom S3 Clients]
    end

    %% Authentication & Authorization Details
    subgraph AAA["Authentication & Authorization"]
        direction TB
        AA1[Access Key Verification]
        AA2[Secret Key Validation]
        AA3[ACL Manager]
        AA4[Permission Resolver]
        
        AA1 --> AA2
        AA2 --> AA3
        AA3 --> AA4
    end

    %% S3 Gateway Implementation
    subgraph Gateway["DDN S3DS Gateway"]
        direction TB
        G1[HTTPS Endpoint]
        G2[Request Parser]
        G3[Operation Router]
        G4[ACL Enforcer]
        G5[Storage Manager]
        
        G1 --> G2
        G2 --> G3
        G3 --> G4
        G4 --> G5
    end

    %% Storage System Details
    subgraph Storage["Storage Systems"]
        direction TB
        subgraph Tier1["Tier1/Scratch"]
            T1_1[NVMe Storage Pool]
            T1_2[400GB/s Bandwidth]
            T1_3[0.6PB Capacity]
        end
        
        subgraph Tier2["Tier2/Project"]
            T2_1[HDD Storage Pool]
            T2_2[180GB/s Bandwidth]
            T2_3[12.5PB Capacity]
        end
    end

    %% Cross-component Interactions
    Clients --> |HTTPS Requests| AAA
    AAA --> |Validated Requests| Gateway
    Gateway --> |Read/Write Operations| Storage

    %% Data Flow Examples
    DF1[("Bucket Creation\nFlow")] --> |1. Client Request| AAA
    DF1 --> |2. Auth Check| Gateway
    DF1 --> |3. Storage Allocation| Storage

    DF2[("Data Access\nFlow")] --> |1. Access Request| AAA
    DF2 --> |2. ACL Check| Gateway
    DF2 --> |3. Data Retrieval| Storage

    %% Styling
    classDef component fill:#f9f,stroke:#333,stroke-width:2px
    classDef flow fill:#bbf,stroke:#333,stroke-width:2px
    classDef storage fill:#bfb,stroke:#333,stroke-width:2px

    class Clients,AAA,Gateway component
    class DF1,DF2 flow
    class Storage,Tier1,Tier2 storage
