
import httpx

from pydantic import BaseModel
from typing import Optional

class LocationCodes(BaseModel):
    admin_district: str
    admin_county: str
    admin_ward: str
    parish: str
    parliamentary_constituency: str
    parliamentary_constituency_2024: str
    ccg: str
    ccg_id: str
    ced: str
    nuts: str
    lsoa: str
    msoa: str
    lau2: str
    pfa: str
    nhs_region: str
    ttwa: str
    national_park: str
    bua: str
    icb: str
    cancer_alliance: str
    lsoa11: str
    msoa11: str
    lsoa21: str
    msoa21: str
    oa21: str
    ruc11: str
    ruc21: str
    lep1: str
    # Handled as Optional because the value is null in the sample payload
    lep2: Optional[str] = None 

class PostcodeResult(BaseModel):
    postcode: str
    quality: int
    eastings: int
    northings: int
    country: str
    nhs_ha: str
    longitude: float
    latitude: float
    european_electoral_region: str
    primary_care_trust: str
    region: str
    lsoa: str
    msoa: str
    incode: str
    outcode: str
    parliamentary_constituency: str
    parliamentary_constituency_2024: str
    admin_district: str
    parish: str
    date_of_introduction: str
    index_of_multiple_deprivation: int
    admin_ward: str
    ccg: str
    nuts: str
    pfa: str
    nhs_region: str
    ttwa: str
    national_park: str
    bua: str
    icb: str
    cancer_alliance: str
    lsoa11: str
    msoa11: str
    lsoa21: str
    msoa21: str
    oa21: str
    ruc11: str
    ruc21: str
    lep1: str
    
    # Nullable text properties mapped safely using Optional fields
    senedd_constituency: Optional[str] = None
    senedd_constituency_no: Optional[str] = None
    admin_county: Optional[str] = None
    date_of_termination: Optional[str] = None
    ced: Optional[str] = None
    lep2: Optional[str] = None
    
    # Nested components map directly to our child model configuration
    codes: LocationCodes

class PostcodeApiResponse(BaseModel):
    status: int
    result: PostcodeResult





import pickle
class PostCodeLookUp():

    def __init__(self, base_url:str = "https://api.postcodes.io"):
        self.base_url = base_url

    def call(self, post_code: str):
        with httpx.Client(base_url=self.base_url, timeout=5.0) as client:            
            try:
                response = client.get(f"/postcodes/{post_code}")
                response.raise_for_status() 
                data = response.json()
                response = PostcodeApiResponse(**data)
                with open(f"{post_code}.pkl", "wb") as f:
                    pickle.dump(response.result, f)
            except Exception as e:
                raise e

looker = PostCodeLookUp()
looker.call("BS15 4XX")
