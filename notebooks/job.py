import oci
import requests
import json

# =========================
# CONFIGURAÇÕES
# =========================
DEPLOYMENT_ID = "ocid1.datasciencemodeldeployment.oc1.sa-saopaulo-1.amaaaaaafioir7ia543seeowgit43cge56svfltzzyksnktatgki6dhmtnmq"

# =========================
# Resource Principal
# =========================
signer = oci.auth.signers.get_resource_principals_signer()

ds_client = oci.data_science.DataScienceClient(
    config={},
    signer=signer
)

# =========================
# Obter endpoint
# =========================
deployment = ds_client.get_model_deployment(DEPLOYMENT_ID).data
endpoint = deployment.model_deployment_url.rstrip("/") + "/predict"

print("Endpoint:", endpoint)

# =========================
# Payload (exemplo)
# =========================
payload = {
    "EventName": ["Monaco GP"],
    "Compound": ["SOFT"],
    "Driver": ["VER"],
    "TyreAge": [5],
    "meanAirTemp": [22.0],
    "meanTrackTemp": [38.0],
    "meanHumid": [60.0],
    "Rainfall": [0.0],
    "GridPosition": [1],
    "Position": [1],
    "CircuitLength": [3.337],
    "designedLaps": [78]
}

# =========================
# Chamada do modelo
# =========================
response = requests.post(
    endpoint,
    json=payload,
    auth=signer,
    headers={"Content-Type": "application/json"},
    timeout=60
)

print("Status:", response.status_code)
print("Resultado:", response.json())
