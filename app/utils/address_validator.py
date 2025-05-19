import httpx
from app.core.settings import settings

NOMINATIM_URL = "https://nominatim.openstreetmap.org/search"

async def validate_address_osm(address: dict) -> bool:
    """
    Valida um endereço usando Nominatim (OpenStreetMap)
    """
    params = {
        "street": address["street"],
        "city": address["city"],
        "state": address["state"],
        "postalcode": address["zip_code"],
        "format": "json"
    }

    headers = {
        "User-Agent": f"{settings.USER_AGENT_NAME} ({settings.USER_AGENT_CONTACT})"
    }

    async with httpx.AsyncClient() as client:
        response = await client.get(NOMINATIM_URL, params=params, headers=headers)
        data = response.json()

    return bool(data)
